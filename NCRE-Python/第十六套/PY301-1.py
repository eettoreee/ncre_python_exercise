#
# 在____________上补充代码 （12根短线）
# 在……上补充一行或多行代码 （6个点）
#


fi = open("data301.txt", "r")
f = open("result301.txt", "w")
cnumd = {}
name = ''
count = 0
flag = 1
for line in fi:
    if '"name":' in line:
        name = line.split('"')[-2]
        flag = 1
    elif '"value":' in line and flag == 1:
        dx = line.split(': ')[-1][:-1]
        cnumd[name] = dx
        flag = 0
        count += 1
for d in cnumd.items():
    f.write("{}:{}\n".format(d[0], d[1]))
print("一共有{}个地区".format(count))
f.close()
fi.close()
