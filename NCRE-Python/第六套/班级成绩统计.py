# coding=utf-8

import re

fi = open('data.txt', 'r')
classes = {}
ls = []
for line in fi:
    sliced_line = re.split("[:,\n]", line)
    ls.append(sliced_line)
    # print(len(ls))
    classes[ls[len(ls) - 1][1]] = classes.get(ls[len(ls) - 1][1], 0) + 1
all_eco_score = 0
all_machine_score = 0
all_comp_score = 0
all_eng_score = 0
all_count_score = 0

for i in ls:
    # print(i[2])
    if i[1] == '经济191':
        all_eco_score += int(i[2])
    elif i[1] == '计算191':
        all_comp_score += int(i[2])
    elif i[1] == '机械191':
        all_machine_score += int(i[2])
    elif i[1] == '英语191':
        all_eng_score += int(i[2])
    else:
        all_count_score += int(i[2])

avg_eco_score = all_eco_score / classes["经济191"]
avg_comp_score = all_comp_score / classes["计算191"]
avg_count_score = all_count_score / classes["会计191"]
avg_machine_score = all_machine_score / classes["机械191"]
avg_eng_score = all_eng_score / classes["英语191"]

print("计算191的平均成绩为{:.2f}".format(avg_comp_score))
print("经济191的平均成绩为{:.2f}".format(avg_eco_score))
print("会计191的平均成绩为{:.2f}".format(avg_count_score))
print("机械191的平均成绩为{:.2f}".format(avg_machine_score))
print("英语191的平均成绩为{:.2f}".format(avg_eng_score))

fi.close()
