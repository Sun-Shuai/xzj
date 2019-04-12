# encoding: utf-8
"""
@author: suns
@contact: sunshuai0518@gmail.com
@time: 2019/4/12 9:10 PM
@file: main.py
@desc: 
"""

import pandas as pd

data = pd.read_csv('dataset.csv')

list_id = data['id2']
list_date = data['date2']
list_short = data['short2']

list_id_date = []
l1 = len(list_id)
for i in range(l1):
    list_id_date.append(str(str(list_id[i]) + '_' + list_date[i]))

dic_a = dict(zip(list_id_date, list_short))


result = []
l2 = len(data['id'])
for i in range(l2):
    current_id = int(data.loc[i].values[0:1])
    current_date = data.loc[i].values[1:2]

    current_id_date = str(current_id) + '_' + current_date
    if (current_id_date[0] in dic_a):
        result.append(dic_a[current_id_date[0]])


print(result)

dataframe = pd.DataFrame({'result':result})
dataframe.to_csv("dataset.csv",index=False,sep=',')