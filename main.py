# encoding: utf-8
"""
@author: suns
@contact: sunshuai0518@gmail.com
@time: 2019/4/12 9:10 PM
@file: main.py
@desc: 
"""

import pandas as pd

filename = 'i-5-2.csv'
insert_loc = 2
insert_column_name = 'result'
colunms_name = ('id', 'date', 'id2', 'date2', 'i2')

# --------------------------------------------以下内容不需要改动--------------------------------------------

data = pd.read_csv(filename,
                   dtype={colunms_name[0]: str, colunms_name[1]: str, colunms_name[2]: str, colunms_name[3]: str,
                          colunms_name[4]: str})

# print(data)

list_id = data[colunms_name[2]]
list_date = data[colunms_name[3]]
list_short = data[colunms_name[4]]

list_id_date = []
l1 = len(list_id)
for i in range(l1):
    id_data = (list_id[i], list_date[i])
    list_id_date.append(id_data)

dic_a = dict(zip(list_id_date, list_short))

print(dic_a)

result = []

l2 = len(data[data[colunms_name[0]].notnull()])

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
