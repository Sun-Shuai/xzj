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

filename = 'LG-last40-15-deal.csv'
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

temp_list = []

for i in range(l2):

    current_id = data.loc[i][0]
    current_date = data.loc[i][1]

    current_id_date = (current_id, current_date)

    if (current_id_date in dic_a):

        current_date = current_id_date[1]


        last_15_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                       - datetime.timedelta(days=15)).strftime('%Y%m%d')
        last_15_id_date = (current_id, last_15_date)

        if (last_15_id_date in dic_a):
            if (dic_a[last_15_id_date] != '0'):
                temp_list.append(int(dic_a[last_15_id_date]))



        last_16_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                       - datetime.timedelta(days=16)).strftime('%Y%m%d')
        last_16_id_date = (current_id, last_16_date)

        if (last_16_id_date in dic_a):
            if (dic_a[last_16_id_date] != '0'):
                temp_list.append(int(dic_a[last_16_id_date]))

        last_17_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                       - datetime.timedelta(days=17)).strftime('%Y%m%d')
        last_17_id_date = (current_id, last_17_date)

        if (last_17_id_date in dic_a):
            if (dic_a[last_17_id_date] != '0'):
                temp_list.append(int(dic_a[last_17_id_date]))


        last_18_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                       - datetime.timedelta(days=18)).strftime('%Y%m%d')
        last_18_id_date = (current_id, last_18_date)

        if (last_18_id_date in dic_a):
            if (dic_a[last_18_id_date] != '0'):
                temp_list.append(int(dic_a[last_18_id_date]))


        last_19_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                       - datetime.timedelta(days=19)).strftime('%Y%m%d')
        last_19_id_date = (current_id, last_19_date)

        if (last_19_id_date in dic_a):
            if (dic_a[last_19_id_date] != '0'):
                temp_list.append(int(dic_a[last_19_id_date]))

        last_20_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=20)).strftime('%Y%m%d')
        last_20_id_date = (current_id, last_20_date)

        if (last_20_id_date in dic_a):
            if (dic_a[last_20_id_date] != '0'):
                temp_list.append(int(dic_a[last_20_id_date]))

        last_21_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=21)).strftime('%Y%m%d')
        last_21_id_date = (current_id, last_21_date)

        if (last_21_id_date in dic_a):
            if (dic_a[last_21_id_date] != '0'):
                temp_list.append(int(dic_a[last_21_id_date]))

        last_22_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=22)).strftime('%Y%m%d')
        last_22_id_date = (current_id, last_22_date)

        if (last_22_id_date in dic_a):
            if (dic_a[last_22_id_date] != '0'):
                temp_list.append(int(dic_a[last_22_id_date]))

        last_23_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=23)).strftime('%Y%m%d')
        last_23_id_date = (current_id, last_23_date)

        if (last_23_id_date in dic_a):
            if (dic_a[last_23_id_date] != '0'):
                temp_list.append(int(dic_a[last_23_id_date]))

        last_24_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=24)).strftime('%Y%m%d')
        last_24_id_date = (current_id, last_24_date)

        if (last_24_id_date in dic_a):
            if (dic_a[last_24_id_date] != '0'):
                temp_list.append(int(dic_a[last_24_id_date]))

        last_25_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=25)).strftime('%Y%m%d')
        last_25_id_date = (current_id, last_25_date)

        if (last_25_id_date in dic_a):
            if (dic_a[last_25_id_date] != '0'):
                temp_list.append(int(dic_a[last_25_id_date]))

        last_26_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=26)).strftime('%Y%m%d')
        last_26_id_date = (current_id, last_26_date)

        if (last_26_id_date in dic_a):
            if (dic_a[last_26_id_date] != '0'):
                temp_list.append(int(dic_a[last_26_id_date]))

        last_27_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=27)).strftime('%Y%m%d')
        last_27_id_date = (current_id, last_27_date)

        if (last_27_id_date in dic_a):
            if (dic_a[last_27_id_date] != '0'):
                temp_list.append(int(dic_a[last_27_id_date]))

        last_28_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=28)).strftime('%Y%m%d')
        last_28_id_date = (current_id, last_28_date)

        if (last_28_id_date in dic_a):
            if (dic_a[last_28_id_date] != '0'):
                temp_list.append(int(dic_a[last_28_id_date]))

        last_29_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=29)).strftime('%Y%m%d')
        last_29_id_date = (current_id, last_29_date)

        if (last_29_id_date in dic_a):
            if (dic_a[last_29_id_date] != '0'):
                temp_list.append(int(dic_a[last_29_id_date]))

        last_30_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=30)).strftime('%Y%m%d')
        last_30_id_date = (current_id, last_30_date)

        if (last_30_id_date in dic_a):
            if (dic_a[last_30_id_date] != '0'):
                temp_list.append(int(dic_a[last_30_id_date]))

        last_31_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=31)).strftime('%Y%m%d')
        last_31_id_date = (current_id, last_31_date)

        if (last_31_id_date in dic_a):
            if (dic_a[last_31_id_date] != '0'):
                temp_list.append(int(dic_a[last_31_id_date]))

        last_32_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=32)).strftime('%Y%m%d')
        last_32_id_date = (current_id, last_32_date)

        if (last_32_id_date in dic_a):
            if (dic_a[last_32_id_date] != '0'):
                temp_list.append(int(dic_a[last_32_id_date]))

        last_33_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=33)).strftime('%Y%m%d')
        last_33_id_date = (current_id, last_33_date)

        if (last_33_id_date in dic_a):
            if (dic_a[last_33_id_date] != '0'):
                temp_list.append(int(dic_a[last_33_id_date]))

        last_34_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=34)).strftime('%Y%m%d')
        last_34_id_date = (current_id, last_34_date)

        if (last_34_id_date in dic_a):
            if (dic_a[last_34_id_date] != '0'):
                temp_list.append(int(dic_a[last_34_id_date]))

        last_35_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=35)).strftime('%Y%m%d')
        last_35_id_date = (current_id, last_35_date)

        if (last_35_id_date in dic_a):
            if (dic_a[last_35_id_date] != '0'):
                temp_list.append(int(dic_a[last_35_id_date]))

        last_36_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=36)).strftime('%Y%m%d')
        last_36_id_date = (current_id, last_36_date)

        if (last_36_id_date in dic_a):
            if (dic_a[last_36_id_date] != '0'):
                temp_list.append(int(dic_a[last_36_id_date]))

        last_37_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=37)).strftime('%Y%m%d')
        last_37_id_date = (current_id, last_37_date)

        if (last_37_id_date in dic_a):
            if (dic_a[last_37_id_date] != '0'):
                temp_list.append(int(dic_a[last_37_id_date]))

        last_38_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=38)).strftime('%Y%m%d')
        last_38_id_date = (current_id, last_38_date)

        if (last_38_id_date in dic_a):
            if (dic_a[last_38_id_date] != '0'):
                temp_list.append(int(dic_a[last_38_id_date]))

        last_39_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=39)).strftime('%Y%m%d')
        last_39_id_date = (current_id, last_39_date)

        if (last_39_id_date in dic_a):
            if (dic_a[last_39_id_date] != '0'):
                temp_list.append(int(dic_a[last_39_id_date]))

        last_40_date = (datetime.datetime.strptime(current_date, '%Y%m%d').date()
                        - datetime.timedelta(days=40)).strftime('%Y%m%d')
        last_40_id_date = (current_id, last_40_date)

        if (last_40_id_date in dic_a):
            if (dic_a[last_40_id_date] != '0'):
                temp_list.append(int(dic_a[last_40_id_date]))

        mean = sum(temp_list) / len(temp_list)

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
