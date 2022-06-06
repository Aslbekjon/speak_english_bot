import requests
import json
app_id = "93fa9ac9"
app_key = "0db50333df431f74bdc8bc91746e4c35"
language = "en-gb"

def getDefination(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
    ras = r.json()

    if 'error' in ras.keys():
        return False
    
    output = {}
    definations = []
    # print(ras['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])
    # print(ras['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
    for i in ras['results'][0]['lexicalEntries'][0]['entries'][0]['senses']:
        definations.append(f"👉 {i['definitions'][0]}")
    output['definations'] = "\n".join(definations)

    if ras['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']:
        output['audioFile'] = ras['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output