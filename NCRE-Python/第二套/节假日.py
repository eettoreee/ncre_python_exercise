# coding=GBK

# Q1 Ҫ������������ƣ�����������ڷ�Χ
fi = open("PY301-vacations.csv", "r")
ls = []
for line in fi:
    ls.append(line.strip("\n").split(","))
    # strip() ���������Ƴ��ַ���ͷβָ�����ַ���Ĭ��Ϊ�ո���з������ַ�����
    # ע��˴���ls��һ����Ԫ����ɵ��б�tuple��
    # print(ls)
s = input("������ڼ�������:")
for line in ls:
    if s == line[1]:
        print("{}�ļ���λ��{}-{}֮��".format(line[1], line[2], line[3]))
fi.close()

# Q2����һ��ڼ�����ţ����һ��ڼ���ʱ�䷶Χ
fi = open("PY301-vacations.csv", "r")
ls = []
for line in fi:
    ls.append(line.strip("\n").split(","))
s = input("������ڼ������:").split(" ")
while True:
    for i in s:
        for line in ls:
            if i == line[0]:
                print("{}({})������{}��{}����{}��{}��֮��".format((line[1]), (line[0]), line[2][:-2], line[2][-2:],
                                                                  line[3][:-2], line[3][-2:]))
    s = input("������ڼ������:").split(" ")
fi.close()

# Q3�Զ������Ľ���ʹ��źϷ��������Ϸ�������Ϸ���ʾ
fi = open("PY301-vacations.csv", "r")
ls = []
for line in fi:
    ls.append(line.strip("\n").split(","))
s = input("������ڼ������:").split(" ")
while True:
    for i in s:
        flag = False
        for line in ls:
            if i == line[0]:
                print("{}({})������{}��{}����{}��{}��֮��".format((line[1]), (line[0]), line[2][:-2], line[2][-2:],
                                                                  line[3][:-2], line[3][-2:]))
                flag = True
        if not flag:
            print("����ڼ��ձ������")
    s = input("������ڼ������:").split(" ")
fi.close()
