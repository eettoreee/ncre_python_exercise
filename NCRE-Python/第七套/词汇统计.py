# coding = utf-8

import jieba as j

with open("data3.txt", "r") as fo:      # 打开文件
    d = {}
    for line in fo:
        ls = j.lcut(line)       # 分词
        for i in ls:
            if len(i) >= 2:
                d[i] = d.get(i, 0) + 1
dl = list(d.items())  # 把字典转换成列表
dl.sort(key=lambda x: x[1], reverse=True)  # 排序，reverse=True表示降序，默认升序
for i in dl[:10]:
    print(i[0] + ":" + str(i[1]), end='\n')
