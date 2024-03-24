# coding = utf-8

import jieba as j

with open("data3.txt", "r") as fo:      # ���ļ�
    d = {}
    for line in fo:
        ls = j.lcut(line)       # �ִ�
        for i in ls:
            if len(i) >= 2:
                d[i] = d.get(i, 0) + 1
dl = list(d.items())  # ���ֵ�ת�����б�
dl.sort(key=lambda x: x[1], reverse=True)  # ����reverse=True��ʾ����Ĭ������
for i in dl[:10]:
    print(i[0] + ":" + str(i[1]), end='\n')
