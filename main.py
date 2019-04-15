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

for item in (chr(76) + chr(111) + chr(118) + chr(101) + chr(89) + chr(111) + chr(117)).split():
    item = item + ' '
    letterlist = []
    for y in range(12, -12, -1):
        list_X = []
        letters = ''
        for x in range(-30, 30):
            expression = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            if expression <= 0:
                letters += item[(x - y) % len(item)]
            else:
                letters += ' '
        list_X.append(letters)
        letterlist += list_X
    print('\n'.join(letterlist))

repair_len = len(list_id) - len(result)
for i in range(repair_len):
    result.append('null')

data.insert(loc=insert_loc, column=insert_column_name, value=result)
data.to_csv(filename, index=False, )
