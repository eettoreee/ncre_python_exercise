# coding=utf-8
import jieba

f = "红楼梦.txt"
sf = "停用词.txt"
f1 = open(f, "r", encoding="utf-8")
datas = f1.read()
f1.close()
f2 = open(sf, "r", encoding="utf-8")
words = f2.read()
f2.close()
data = jieba.lcut(datas)
d = {}
word = ["一个", "如今", "一面", "众人", "说道", "只见", "不知",
        "两个", "起来", "二人", "今日", "听见", "不敢", "不能",
        "东西", "只得", "心中", "回来", "几个", "原来", "进来",
        "出去", "一时", "银子", "起身", "答应", "回去"]
for i in data:
    if len(i) < 2 or i in words or i in word:
        continue
    if i in ["凤姐", "凤姐儿", "凤丫头"]:
        i = "凤姐"
    elif i in ["宝玉", "二爷", "宝二爷"]:
        i = "宝玉"
    elif i in ["黛玉", "颦儿", "林妹妹", "黛玉道"]:
        i = "黛玉"
    elif i in ["宝钗", "宝丫头"]:
        i = "宝钗"
    elif i in ["贾母", "老祖宗"]:
        i = "贾母"
    elif i in ["袭人", "袭人道"]:
        i = "袭人"
    elif i in ["贾政", "贾政道"]:
        i = "贾政"
    elif i in ["贾琏", "琏二爷"]:
        i = "贾琏"
    d[i] = d.get(i, 0) + 1
l = list(d.items())
l.sort(key=lambda x: (x[1], x[0]), reverse=True)
f = open("result.csv", 'w')
for i in l:
    if i[1] < 40:
        break
    f.write(i[0] + ',' + str(i[1]) + '\n')
f.close()
