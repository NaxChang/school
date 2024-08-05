# 4-8
s1 = input()
s2 = input()
if 3 < len(s1) < 20 and 3 < len(s2) < 20:
    print(len(s1))
    print(len(s2))
    s3 = s1 + s2
    for i in range(len(s3) - 1, -1, -1):
        print(s3[i], end="")
else:
    print("error")
