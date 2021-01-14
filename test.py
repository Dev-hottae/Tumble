import requests
from account.keys import dart_key

url = '	https://opendart.fss.or.kr/api/irdsSttus.json'

query = {
    "crtfc_key": dart_key,
    "corp_code": "00293886",
    "bsns_year": "2015",
    "reprt_code": "11011"
}


res = requests.get(url=url, params=query).json()
print(res)
print(res.keys())