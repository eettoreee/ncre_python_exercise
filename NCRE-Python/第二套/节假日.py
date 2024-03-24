# coding=GBK

# Q1 要求输入节日名称，输出节日日期范围
fi = open("PY301-vacations.csv", "r")
ls = []
for line in fi:
    ls.append(line.strip("\n").split(","))
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    # 注意此处的ls是一个由元组组成的列表（tuple）
    # print(ls)
s = input("请输入节假日名称:")
for line in ls:
    if s == line[1]:
        print("{}的假期位于{}-{}之间".format(line[1], line[2], line[3]))
fi.close()

# Q2输入一组节假日序号，输出一组节假日时间范围
fi = open("PY301-vacations.csv", "r")
ls = []
for line in fi:
    ls.append(line.strip("\n").split(","))
s = input("请输入节假日序号:").split(" ")
while True:
    for i in s:
        for line in ls:
            if i == line[0]:
                print("{}({})假期是{}月{}日至{}月{}日之间".format((line[1]), (line[0]), line[2][:-2], line[2][-2:],
                                                                  line[3][:-2], line[3][-2:]))
    s = input("请输入节假日序号:").split(" ")
fi.close()

# Q3对二做出改进，使序号合法化，不合法输出不合法提示
fi = open("PY301-vacations.csv", "r")
ls = []
for line in fi:
    ls.append(line.strip("\n").split(","))
s = input("请输入节假日序号:").split(" ")
while True:
    for i in s:
        flag = False
        for line in ls:
            if i == line[0]:
                print("{}({})假期是{}月{}日至{}月{}日之间".format((line[1]), (line[0]), line[2][:-2], line[2][-2:],
                                                                  line[3][:-2], line[3][-2:]))
                flag = True
        if not flag:
            print("输入节假日编号有误！")
    s = input("请输入节假日序号:").split(" ")
fi.close()
