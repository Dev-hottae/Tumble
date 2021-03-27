import numpy as np
import pandas as pd
import kss

from konlpy.tag import Mecab
from math import log


class TfIdf:
    def __init__(self, sentence):
        """
        TF-IDF를 계산하는 class입니다.
        String 형태를 입력해주시기 바랍니다.
        """
        document = kss.split_sentences(sentence)
        tokenizer = Mecab()
        using_tag = ["NNP", "NNG", "SL", "VV"]
        self.doc_token = []
        for line in document:
            tokens = []
            for voca in tokenizer.pos(line):
                if voca[1] in using_tag:
                    tokens.append(voca[0])
            self.doc_token.append(tokens)
    
    def make_word2index(self):
        token_list = \
            [item for sublist in self.doc_token for item in sublist]
        word2index = {}
        for voca in token_list:
            if voca not in word2index.keys():
                word2index[voca] = len(word2index)
        return word2index
        
    def make_bow(self, word2index):
        bow = []
        for doc in self.doc_token:
            tmp_bow = [0] * len(word2index)
            for voca in doc:
                voca_index = word2index.get(voca)
                if tmp_bow[voca_index] != 0:
                    tmp_bow[voca_index] += 1
                else:
                    tmp_bow[voca_index] = 1
            bow.append(tmp_bow)
        bow = np.array(bow)
        return bow

    def calculate_tfidf(self):
        word2index = self.make_word2index()
        bow = self.make_bow(word2index)
        tf = []
        for i, doc in enumerate(bow):
            tf.append(np.array(doc) / len(self.doc_token[i]))
        idf = []
        for term in bow.T:
            idf.append(-log((term >= 1).sum()/len(bow)))
        tf_idf = pd.DataFrame(np.array(tf)*np.array(idf), columns = word2index)
        return tf_idf

if __name__ == '__main__':
    sentence = input("입력해주세요 : ")
    tfidf = TfIdf(sentence)
    tf_idf = tfidf.calculate_tfidf()
    print(tf_idf)
