with open("read.txt", "r", encoding="utf8") as f:
    data = f.read()

newdata = ""
for x in data:
    newdata += chr((((ord(x) - 97) + 2) % 26) + 97)

with open("write.txt", "w", encoding="utf8") as f:
    f.write(newdata)
