import requests
from datetime import datetime, timedelta
import xmltodict
import json
def get_city_data():
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"

    params = {
        'serviceKey':'Jkq4wMWB+1z/BQMq/r65letz0Vae3/xyEFRTPBhe8boljNaZaA7VoWjifS1IskHYQkvymEn7DnIMAif3Z53utg==',
        'pageNo':'1',
        'numOfRows':'10',
        'startCreateDt':'20210312',
        'endCreateDt':'20210313',}

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    
    todayFormat = str(year) + str(month) + str(day)
    yesterDayFormat = datetime.today() - timedelta(1)
    yesterDayFormat = yesterDayFormat.strftime("%Y%m%d")
    

    res = requests.get(url, params = params)
    dict_data = xmltodict.parse(res.text)

    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)
    items = dict_data['response']["body"]["items"]["item"]
    results = []

    yesterDayStandard = items[0]['createDt']
    index = yesterDayStandard.find(":")

    yesterDayStandard = yesterDayStandard[0:index]
    print(yesterDayStandard)

    todayStandard = '{}-{}-{}'.format(year,month,day)
    print(todayStandard)

    for item in items:
        if yesterDayStandard in item['createDt']:
            results.append(item)
        elif todayStandard in items['createDt']:
            results
        if len(results) == 19:
            break


    print(dict_data)
   

    return results