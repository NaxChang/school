# 6-10
A, B = [], []
ans = []
m, n1 = map(int, input().split())
for i in range(m):
    A.append(list(map(int, input().split())))
n2, p = map(int, input().split())
for i in range(n2):
    B.append(list(map(int, input().split())))
if n1 != n2:
    print("error")
else:
    L = []
    for i in range(m):
        LL = []
        for j in range(p):
            summ = 0
            for k in range(n1):
                summ += A[i][k] * B[k][j]
            LL.append(summ)
        L.append(LL)
# print(L)
for x in L:
    # print(*x)
    for i in range(len(x)):
        if i == len(x) - 1:
            print(x[i])
        else:
            print(x[i], end=" ")
