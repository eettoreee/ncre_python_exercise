# coding=utf-8
import jieba

s = input("请输入一段中文文本，句子之间以逗号或句号分隔：")
slist = jieba.lcut(s)
m = 0
for i in slist:
    if i in "，。":
        continue
    else:
        m += 1
    print(i,end="/")

print("\n中文词语数是：{}\n".format(m))

slist = s.split("，")
output_lines = []
for line in slist:
    line = line.strip("。")
    padding_spaces = (20 - len(line)) // 2
    output_lines.append('{:{align}^{width}}'.format(line, align=' ', width=20))
print("\n".join(output_lines))