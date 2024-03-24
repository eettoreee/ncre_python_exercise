# coding = utf-8

fi = open("data.txt", "r")
f = open("univ.txt", "w")
lines = fi.readlines()
for line in lines:
    if 'alt=' in line:
        uni = (line.split("alt=\""))[1].split("\"")[0]
        f.write(uni+"\n")
f.close()
