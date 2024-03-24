# coding = utf-8

fi = open('data.txt','r')
d = {}
students = fi.readlines()
for i in students:
    i = i.strip().split(':')
    clas,score = i[1].split(',')
    d[clas] = d.get(clas,[])+[eval(score)]

for i in d:
    avg_score = sum(d[i])/len(d[i])
    print('{}:{:.2f}'.format(i, avg_score))
