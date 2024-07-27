def compute(a, b, c):
    total = a + b + c
    average = total / 3
    return total, average


x = int(input())
y = int(input())
z = int(input())
summ, aver = compute(x, y, z)
print(f"{x}+{y}+{z}={summ}")
print(f"{aver:.2f}")
