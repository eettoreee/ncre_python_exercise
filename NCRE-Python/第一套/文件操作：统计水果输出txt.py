# 打开文件，以写入模式创建一个名为PY202.txt的文件对象
fo = open("水果统计.txt", "w")

# 提示用户输入类型序列，并将输入的字符串赋值给变量txt
# txt = input("请输入类型序列: ")
txt = "apple apple orange orange orange orange"
# 将输入的字符串按空格分割成一个列表，并赋值给变量fruits
fruits = txt.split(" ")

# 创建一个空字典，用于存储每个水果类型及其出现的次数
d = {}

# 遍历fruits列表中的每个水果类型
for fruit in fruits:
    # 使用字典的get()方法获取当前水果类型的计数，如果不存在则返回0，并将其加1后重新赋值给当前水果类型的计数
    # d.get(如果字典内有则返回的value,如果没有的)
    # 一般只有计数的需要使用字典，如果不是计数也可以使用列表嵌套等等
    d[fruit] = d.get(fruit, 0) + 1

# 将字典d的键值对转换为列表，并赋值给变量ls
# 注意items要有s
ls = list(d.items())
# 使用lambda函数作为排序的key，按照字典的值进行降序排序
# 对于列表ls中的每一个元组x，取其第二个元素作为排序的依据，也就是元组中的value
# 第二个x后面的是索引，索引从0开始，是列表
ls.sort(key=lambda x: x[1], reverse=True)
print(ls[1])
# 遍历排序后的列表ls中的每个键值对
for k in ls:
    # 将键值对格式化为字符串，并写入文件中，每个键值对占一行
    fo.write("{}:{}\n".format(k[0], k[1]))

# 关闭文件
fo.close()
