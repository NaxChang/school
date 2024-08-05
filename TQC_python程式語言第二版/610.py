L1, L2 = [], []
a, b1 = map(int, input().split())
for i in range(a):
    L1.append(list(map(int, input().split())))

b2, c = map(int, input().split())
for i in range(b2):
    L2.append(list(map(int, input().split())))
ans = []
if b1 != b2:
    print("error")
else:
    # print(L1,L2)
    for i in range(a):
        L = []

        for j in range(c):
            summ = 0
            for k in range(b1):
                summ += L1[i][k] * L2[k][j]
            L.append(summ)
        ans.append(L)
# print(ans)
for i in range(len(ans)):
    print(*ans[i])
