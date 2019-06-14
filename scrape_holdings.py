import requests
import json
info = []
def parse_response(data, info):
    for row in data["rows"]:
        name = row["holding"].split('>')[1].split('(')[0]
        holding = {
            "name": name,
            "weight": row["weight"]
        }
        info.append(holding)
    return info

for i in range(1,4):
    req_url ='https://etfdb.com/data_set/?tm=40284&cond={%22by_etf%22:783}&no_null_sort=true&count_by_id=&sort=weight&order=desc&limit='+str(15*i)+'&offset='+str(15*(i-1))
    resp = requests.get(req_url)
    data = resp.content
    jsn = json.loads(data)
    info = parse_response(jsn, info)

print("Info is", info)
