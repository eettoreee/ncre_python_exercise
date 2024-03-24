fi = open("data.txt", "r")
[name, score] = [0, 0]
for line in fi:
    if int(line[-4:]) > score:
        name = line[:3]
        score = int(line[-4:])
    else:
        continue

print("{}:{}".format(name, score))
