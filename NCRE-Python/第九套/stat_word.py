# coding = utf-8
import jieba as j


def stat(filename):
    """
    统计词频
    :param filename:
    :return:
    """
    fo = open(filename, 'r')
    txt = fo.read()
    ls = j.lcut(txt)
    d = {}
    for i in ls:
        if len(i) >= 2:
            d[i] = d.get(i, 0) + 1
    lt = list(d.items())
    lt.sort(key=lambda x: x[1], reverse=True)

    # 获取年份名称，并且添加冒号输出
    print(filename.split('.')[0][-4::] + ":", end='')
    # 继续输出具体的词频
    for k in range(9):
        print(lt[k][0] + ":" + str(lt[k][1]), sep=',', end=',')
    # 因为最后一个没有冒号，所以单独输出
    print(lt[9][0] + ":" + str(lt[9][1]), sep=',')


stat("data2018.txt")
stat("data2019.txt")
