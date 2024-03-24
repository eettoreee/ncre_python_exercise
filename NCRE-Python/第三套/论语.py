# Q1：要求去除论语中原文下的注释，仅保留原文部分（包含原文内部的下标序号）
fi = open("论语.txt", "r")
fo = open("论语-原文.txt", "w")
flag = False
for line in fi:
    if "【" in line:
        flag = False
    elif "【原文】" in line:
        flag = True
        continue
    elif flag:
        fo.write(line.lstrip())
fi.close()
fo.close()

# Q2：要求在Q1的基础上，去除掉原文中夹杂的下标序号
fi = open("论语-原文.txt", 'r')
fo = open("论语-提纯原文.txt", 'w')
for line in fi:
    for i in range(1, 23):
        line = line.replace("({})".format(i), "")
        # 此处使用了for遍历多行，按照({})的顺序分别逐一去除不需要的字符
    fo.write(line)
fi.close()
fo.close()
