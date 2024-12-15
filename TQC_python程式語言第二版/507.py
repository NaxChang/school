ans = input()
L = []
for i in range(3):
    L.append(input())


def compute(s, ans):
    a, b = 0, 0
    for i in range(len(ans)):
        if s[i] == ans[i]:
            a += 1
        elif s[i] in ans:
            b += 1
    print(f"{a}A{b}B")


for i in range(3):
    compute(L[i], ans)
