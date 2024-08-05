def compute(a, b):
    return a + b


x = eval(input())
y = eval(input())
r = compute(x, y)
print(f"total={compute(x, y):.2f}")
