import requests 
import json

#25 minutes on API video 

#build out URL was easy as there are filters to put in place on the website
# need ID, Jurisdiction, Decision Date, & court

base_url = "https://api.case.law/v1/cases/?search=prostitution&jurisdiction=ny&decision_date__gte=1970-01-01&decision_date__lte=2020-01-01"

r = requests.get(base_url)

save_data = []

data = json.loads(r.text)

#print(data['results'][1]['name_abbreviation'])

for item in data['results']:
    if 'Buffalo' and 'Syracuse' and 'Rochester' and 'Suffolk' not in (item['court']['name']):
        save_data.append(item)
        print(item['court']['name'])

with open ('CaseLawAPI.json', 'w') as out:
    json.dump(save_data,out,indent=2)

#dont want buffalo, rochester , syracuse 
