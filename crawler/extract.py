import json
import os
import matplotlib.pyplot as plt
import numpy as np
import re


path = "res.json"
with open(path) as json_data:
    d = json.load(json_data)
uni_name = []
kafedras_numbers = []
for i in range(len(d)):
    name=re.sub("^\s+|\n|\r|\s+$", '', d[i]['title'])
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

plt.show()

#Range kaf - employees

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
path = "full.json"
with open(path) as json_data:
    d = json.load(json_data)
kaf_name = []
employee_numbers=[]
for i in range(len(d)):
    name=re.sub("^\s+|\n|\r|\s+$", '', d[i]['kaf_name'])
    kaf_name.append(name)
    employee_numbers.append(len(d[i]['employees']))
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

plt.show()
