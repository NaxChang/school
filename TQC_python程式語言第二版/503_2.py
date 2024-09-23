def compute(i, b):
    ans = (i) ** 0.5
    if int(ans) == float(ans):
        print(int((i**0.5) ** b))


a = int(input())
b = int(input())
for i in range(1, a):
    compute(i, b)
