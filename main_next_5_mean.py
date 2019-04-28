# encoding: utf-8
"""
@author: suns
@contact: sunshuai0518@gmail.com
@time: 2019/4/12 9:10 PM
@file: main.py
@desc: 
"""

import datetime
import pandas as pd

filename = 'EG-next5-deal.csv'
insert_loc = 2
insert_column_name = 'deal'
colunms_name = ('id', 'date', 'id2', 'date2', 'deal2')

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

temp_five_list = []

for i in range(l2):

    current_id = data.loc[i][0]
    current_date = data.loc[i][1]

    current_id_date = (current_id, current_date)

    if (current_id_date in dic_a):

        current_date = current_id_date[1]

        last_1_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                       + datetime.timedelta(days=1)).strftime('%Y%m%d')
        last_1_id_date = (current_id, last_1_date)

        last_2_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                       + datetime.timedelta(days=2)).strftime('%Y%m%d')
        last_2_id_date = (current_id, last_2_date)

        last_3_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                       + datetime.timedelta(days=3)).strftime('%Y%m%d')
        last_3_id_date = (current_id, last_3_date)

        last_4_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                       + datetime.timedelta(days=4)).strftime('%Y%m%d')
        last_4_id_date = (current_id, last_4_date)

        last_5_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                       + datetime.timedelta(days=5)).strftime('%Y%m%d')
        last_5_id_date = (current_id, last_5_date)


        if (last_1_id_date in dic_a):
            if (dic_a[last_1_id_date] != '0'):
                temp_five_list.append(int(dic_a[last_1_id_date]))
        if (last_2_id_date in dic_a):
            if (dic_a[last_2_id_date] != '0'):
                temp_five_list.append(int(dic_a[last_2_id_date]))
        if (last_3_id_date in dic_a):
            if (dic_a[last_3_id_date] != '0'):
                temp_five_list.append(int(dic_a[last_3_id_date]))
        if (last_4_id_date in dic_a):
            if (dic_a[last_4_id_date] != '0'):
                temp_five_list.append(int(dic_a[last_4_id_date]))
        if (last_5_id_date in dic_a):
            if (dic_a[last_5_id_date] != '0'):
                temp_five_list.append(int(dic_a[last_5_id_date]))

        mean = sum(temp_five_list) / len(temp_five_list)
        result.append(mean)
    else:
        result.append(' ')

for item in (chr(76) + chr(111) + chr(118) + chr(101)).split():
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
    result.append(' ')

data.insert(loc=insert_loc, column=insert_column_name, value=result)
data.to_csv(filename, index=False, )
