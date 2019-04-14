# encoding: utf-8
"""
@author: suns
@contact: sunshuai0518@gmail.com
@time: 2019/4/12 9:10 PM
@file: main.py
@desc: 
"""

import pandas as pd

filename = 'old.xlsx'
insert_sheet_name = 'Sheet1'
insert_loc = 3
insert_column_name = 'result'

data = pd.read_excel(filename, sheet_name=insert_sheet_name,
                     dtype={'id': str, 'date': str, 'short': str, 'id2': str, 'date2': str,
                            'short2': str})

# print(data)

list_id = data['id2']
list_date = data['date2']
list_short = data['short2']

# print(list_id)
# print(list_date)
# print(list_short)

list_id_date = []
l1 = len(list_id)
for i in range(l1):
    # print(type(list_id[i]))
    # print(type(list_date[i]))
    list_id_date.append(list_id[i] + '_' + list_date[i])

dic_a = dict(zip(list_id_date, list_short))

print(dic_a)

result = []

l2 = len(data[data['id'].notnull()])

for i in range(l2):
    current_id = data.loc[i].values[0:1].tolist()[0]
    current_date = data.loc[i].values[1:2]

    current_id_date = str(current_id) + '_' + current_date

    if (current_id_date[0] in dic_a):
        result.append(dic_a[current_id_date[0]])
    else:
        result.append('null')

print(result)

repair_len = len(list_id) - len(result)
for i in range(repair_len):
    result.append('null')

data.insert(loc=insert_loc, column=insert_column_name, value=result)
data.to_excel(filename, sheet_name=insert_sheet_name, index=False, )
