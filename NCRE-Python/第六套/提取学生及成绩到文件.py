fi = open("data.txt", "r")
fo = open("studs.txt", "w")
for line in fi:
    fo.write("{}:{}".format(line[:3], line[-4:]))
fi.close()
fo.close()
