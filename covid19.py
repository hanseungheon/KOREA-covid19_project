import requests
from bs4 import BeautifulSoup

def get_corona_summary():
    res = requests.get("http://ncov.mohw.go.kr/")

    soup = BeautifulSoup(res.text , 'lxml')

    dusts = soup.select('.liveNumOuter .liveNum .num')

    results={
        '확진환자' : int(dusts[0].text.replace(',','').replace('(누적)','')),
        '완치' : int(dusts[1].text.replace(',','')),
        '치료중' : int(dusts[2].text.replace(',','')),
        '사망' : int(dusts[3].text.replace(',',''))
    }

    return results
    





