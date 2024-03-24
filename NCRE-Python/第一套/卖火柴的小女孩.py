fi = open("小女孩.txt", "r")
fo = open("小女孩1.txt", "w", encoding="utf-8")
txt = fi.read()
d = {}
exclude = "，。！？、（）【】<>《》=：+-*—“”…"
for word in txt:
    if word in exclude:
        continue
    else:
        d[word] = d.get(word, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)
fo.write("{}:{}".format(ls[0][0], ls[0][1]))
fo.close()

# 第三问，要求包括标点进行字符统计，字频从高到低排序
fi = open("小女孩.txt", "r")
fo = open("小女孩-频次排序.txt", "w")
txt = fi.read()
d = {}
for word in txt:
    d[word] = d.get(word, 0) + 1
del d[" "]
del d["\n"]
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)  # 此行可以按照词频由高到低排序
for i in range(len(ls)):
    ls[i] = f"{ls[i][0]}:{ls[i][1]}"
fo.write(",".join(ls))
fi.close()
fo.close()
