# coding=utf-8
f = open('data.txt','r')
d = {}
for line in f:
    ls = line.strip().split(",")
    if len(ls) < 3:
        continue
    d[ls[2]] = d.get(ls[2], []) + [ls[1]]
f.close()
unis = list(d.items())
for d in unis:
    print('{:>4}: {:>4} : {}'.format(d[0],len(d[1])," ".join(d[1])))