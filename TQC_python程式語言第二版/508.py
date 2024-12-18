def compute(s):
    L = s.split("/")
    print(" ".join(L))
    total = 0
    for i in L:
        total += int(i)
    print(total)


s = input()
compute(s)
