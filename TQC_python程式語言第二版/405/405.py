L = [int(input()) for i in range(3)]

with open("read.txt", "r", encoding="utf8") as f:
    data = f.read().split()


for i in range(3):
    s1 = str(L[i]) * L[i]
    s2 = data[i][L[i] :]
    print(s1 + s2)

"""
perseverance
determination
insistence
"""
