import jieba
txt = input("请输入一段中文文本:")
ls = jieba.lcut(txt)
print(ls)
for i in ls[::-1]:
    print(i, end='')
