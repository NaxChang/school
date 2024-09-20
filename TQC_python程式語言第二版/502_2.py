n = input()
total = 1
L = []
for i in n:
    total *= int(i)
    L.append(i)
print(f'{"*".join(n)}={total}')
# print(L)
# print(total)
