a = int(input())
b = int(input())

for i in range(1, a):
    x = ((i) ** 0.5) // 1
    if x**2 == float(i):
        print(int(x**b))
