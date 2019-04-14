# encoding: utf-8
"""
@author: suns
@contact: sunshuai0518@gmail.com
@time: 2019/4/12 9:10 PM
@file: main.py
@desc: 
"""

import pandas as pd

filename = '控制变量.csv'
insert_loc = 4
insert_column_name = 'result3'

data = pd.read_csv(filename, dtype={'id': str, 'date': str, 'id2': str, 'date2': str,
                                    'size2': str})

# print(data)

list_id = data['id2']
list_date = data['date2']
list_short = data['size2']

list_id_date = []
l1 = len(list_id)
for i in range(l1):
    id_data = (list_id[i], list_date[i])
    list_id_date.append(id_data)

dic_a = dict(zip(list_id_date, list_short))

print(dic_a)

result = []

l2 = len(data[data['id'].notnull()])

for i in range(l2):

    current_id = data.loc[i][0]
    current_date = data.loc[i][1]

    current_id_date = (current_id, current_date)

    if (current_id_date in dic_a):
        result.append(dic_a[current_id_date])
    else:
        result.append('null')

print(result)

repair_len = len(list_id) - len(result)
for i in range(repair_len):
    result.append('null')

data.insert(loc=insert_loc, column=insert_column_name, value=result)
data.to_csv(filename, index=False, )
