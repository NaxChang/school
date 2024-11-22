def compute(n):
    L = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                L.append(str(i))
                n = n // i
                break
    if len(L) == 1:
        print(-1)  # 2*2*2*3*3*5
    else:
        print("*".join(L))


n = int(input())
compute(n)
