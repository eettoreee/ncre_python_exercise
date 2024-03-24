#PY301-1.py
#请在.....处填写多行表达式或语句
#可以修改其他代码

def ravg(lst):
    sum=0
    for i in lst:
        sum+=i
    return round(sum/len(lst),1)

qzlst=[]
swlst=[]
zylst=[]
with open("data2.csv","r") as f:
    datas=f.readlines()
    for i in datas:
        if i in datas[:5]:
            print(i,end='')
        if i in datas[1:]:
            ls=i.strip().split(',')
            qzlst.append(eval(ls[1]))
            swlst.append(eval(ls[2]))
            zylst.append(eval(ls[3]))
avglst=["平均值",ravg(qzlst),ravg(swlst),ravg(zylst)]
maxlst=["最大值",max(qzlst),max(swlst),max(zylst)]
minlst=["最小值",min(qzlst),min(swlst),min(zylst)]

with open("tongji.csv","w") as f:
    f.write('统计,报名,弃考,有效\n')
    f.write('{},{},{},{}'.format(*avglst)+'\n')
    f.write('{},{},{},{}'.format(*maxlst)+'\n')
    f.write('{},{},{},{}'.format(*minlst))
