t = int(input("输入需要的数列总元素数:"))
ls = []
a = 0
b = 1
for i in range(t):
    c = a + b
    ls.append(c)
    a = b
    b = c

# 下面是另外一种方法
a = 0
b = 1
ts = 0
while ts <= t:
    a, b = b, a + b
    print(a, end=',')
    ts += 1
