import requests

class Dart:

    HOST = 'https://opendart.fss.or.kr'

    def __init__(self, api_key):
        self.api_key = api_key

    # 공시검색
    def search_gongsi(self, corp_code, page_no=1, page_count=100, pblntf_ty=None, pblntf_detail_ty=None, bgn_de=None, end_de=None, last_reprt_at=None):

        '''
        :str corp_code: 회사코드
        :int page_no: 받아온 데이터 페이지번호
        :int page_count: 페이지 당 데이터 갯수(max=100)
        :list pblntf_ty: config 참고
        :list pblntf_detail_ty: config 참고
        :str(YYYYMMDD) bgn_de: 데이터 시작일
        :str(YYYYMMDD) end_de: 데이터 종료일
        :str("Y"or"N") last_reprt_at: 최종보고서만 검색여부(Y or N)
        :return: json
        '''

        url = "/api/list.json"
        query = {
            "crtfc_key": self.api_key,
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
            "last_reprt_at": last_reprt_at,
            "pblntf_ty": pblntf_ty,
            "pblntf_detail_ty": pblntf_detail_ty,
            "page_no": page_no,
            "page_count": page_count,
        }

        res = requests.get(url=url, params=query).json()
        return res

    # 기업개황
    def company_overview(self, corp_code):
        '''
        :str corp_code: 회사코드
        :return: json
        '''

        url = "/api/company.json"
        query = {
            "crtfc_key": self.api_key,
            "corp_code": corp_code,
        }

        res = requests.get(url=url, params=query).json()
        return res

    # 공시서류원본파일
    def d_raw_gongsi(self):
        pass

    # 고유번호(기업 정보 파일다운로드)
    def d_company_datafile(self):
        pass

    # 증자(감자)현황
    def capital_change(self, corp_code, bsns_year, reprt_code):
        '''
        :str corp_code: 회사 고유번호
        :str bsns_year: 사업연도
        :str reprt_code: {1q: 11013, 2q: 11012, 3q: 11014, 사업보고서: 11011}
        :return:
        '''

        url = "/api/irdsSttus.json"
        query = {
            "crtfc_key": self.api_key,
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code
        }

        res = requests.get(url=url, params=query).json()
        return res

    # 배당에 관한 사항
    def dividend_status(self):
        pass

    # 자기주식 취득 및 처분 현황
    def self_acquisition_status(self):
        pass

    # 최대주주 현황
    def