import json

with open('nobel_lectures.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    print(i['birth_country'])
