# coding=utf-8

import jieba

with open("data2.txt", "w") as fi:
    s = input("请输入一个中文字符串，包含逗号和句号：")
    # 分词
    k = jieba.lcut(s)
    # 初始化字典
    d1 = {}
    for i in k:
        if len(i) >= 2:     # 2个字以上的词
            d1[i] = d1.get(i, 0) + 1
    for j in d1:
        fi.write(j+':'+str(d1[j])+'\n')
