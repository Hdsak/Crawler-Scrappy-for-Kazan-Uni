import json
url_list=[]
path = "res.json"
with open(path) as json_data:
    d = json.load(json_data)
for k in d:
    for j in k["kaf"]:
        newx=j.replace("Home","Employee")
        newx=newx.replace("Unit","List")
        url_list.append("https://kgeu.ru"+newx)
print(url_list)