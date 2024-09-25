def compute(s):
    ss = ""
    for i in range(len(s) - 1, -1, -1):
        ss += s[i]

    if s == ss:
        print("Yes")
    else:
        print("No")


s = input()
compute(s)
