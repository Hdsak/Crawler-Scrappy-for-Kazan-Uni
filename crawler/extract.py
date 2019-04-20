import json
import os
import matplotlib.pyplot as plt
import numpy as np
import re
import matplotlib.mlab as mlab
import pygal

path = "res.json"
with open(path) as json_data:
    d = json.load(json_data)
uni_name = []
kafedras_numbers = []
for i in range(len(d)):
    name = re.sub("^\s+|\n|\r|\s+$", '', d[i]['title'])
    uni_name.append(name)
    kafedras_numbers.append(len(d[i]['subtitle']))
sizes = kafedras_numbers
for i in range(len(uni_name)):
    uni_name[i] = "{} ({})".format(uni_name[i], kafedras_numbers[i])
# explode = (0.1, 0.1, 0.1)
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=uni_name, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')
# plt.show()


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(kafedras_numbers, autopct=lambda pct: func(pct, kafedras_numbers),
                                  textprops=dict(color="w"))

ax.legend(wedges, uni_name,
          title="Unis",
          loc="center left",
          bbox_to_anchor=(0, 0, 0.5, 0)
          )

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Uni -> kafedras nunmber")

# plt.show()

# Range kaf - employees

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
path = "full.json"
with open(path) as json_data:
    p = json.load(json_data)
kaf_name = []
employee_numbers = []
for i in range(len(p)):
    name = re.sub("^\s+|\n|\r|\s+$", '', p[i]['kaf_name'])
    kaf_name.append(name)
    employee_numbers.append(len(p[i]['employees']))
sizes = employee_numbers
for i in range(len(kaf_name)):
    kaf_name[i] = "{} ({})".format(kaf_name[i], employee_numbers[i])

wedges, texts, autotexts = ax.pie(employee_numbers, autopct=lambda pct: func(pct, employee_numbers),
                                  textprops=dict(color="w"))

ax.legend(wedges, kaf_name,
          title="Kafs",
          loc="center left",
          bbox_to_anchor=(0, 0, 0.5, 0)
          )

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Kafs -> Employees nunmber")

# plt.show()

# hist kafs


results = []
frequences = []
hist = pygal.Bar()
hist.title = "Resul of kafedras"
hist.x_labels = [x for x in kaf_name]
hist.x_title = "Kafedras name"
hist.y_title = "Count sotr"
hist.add("employee numbers", employee_numbers)
hist.render_to_file("histo.svg")
IEE_kafs = []
for i in d[0]['subtitle']:
    IEE_kafs.append(i)
IEE = {d[0]["title"]: IEE_kafs}
IT_kafs = []
for i in d[1]['subtitle']:
    IT_kafs.append(i)
IT = {d[1]["title"]: IT_kafs}
ICTE_kafs = []
for i in d[2]['subtitle']:
    ICTE_kafs.append(i)
ICTE = {d[2]["title"]: ICTE_kafs}
zav_kaf_name = {}
unis = [IEE, IT, ICTE]
for i in range(len(d)):
    for k in p:
        zav_kaf_name[k["kaf_name"]] = k["employees"][0]
with open('zav_name.txt', 'w') as w:
    w.write("\t\t\t\t\tЗаведующие кафедрами в КГЭУ")
    for i in unis:
        name_uni = list(i.keys())
        # name_uni = re.sub("^\s+|\n|\r|\s+$", '', name_uni[-1])
        name_uni=name_uni[-1]
        w.write("\n\n\n"+name_uni)
        for k, v in zav_kaf_name.items():
            key_uni = re.sub("^\s+|\n|\r|\s+$", '', k)
            if key_uni in i[name_uni]:
                #name = re.sub("^\s+|\n|\r|\s+$", '', k)
                w.write(("\r\r\t    {} - {} ").format(key_uni, v))
