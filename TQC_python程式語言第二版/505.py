import math

L = [eval(input()) for i in range(6)]
ans = (
    abs(L[0]) * math.floor(L[1])
    + pow(L[2], L[3]) * math.sqrt(L[4])
    + math.log(L[5], 10)
)

print(f"{ans:.2f}")
