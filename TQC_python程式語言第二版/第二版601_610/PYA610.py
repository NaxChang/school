# 輸入第一個矩陣的維度
a, b = map(int, input().split())

# 初始化第一個矩陣
matrix1 = []
for i in range(a):
    row = list(map(int, input().split()))
    matrix1.append(row)

# 輸入第二個矩陣的維度
c, d = map(int, input().split())

# 初始化第二個矩陣
matrix2 = []
for i in range(c):
    row = list(map(int, input().split()))
    matrix2.append(row)

# 檢查矩陣相乘是否合法
if b != c:
    print("error")
else:
    # 初始化結果矩陣
    result_matrix = []
    for i in range(a):
        result_row = []
        for j in range(d):
            product = 0
            for k in range(b):
                product += matrix1[i][k] * matrix2[k][j]
            result_row.append(product)
        result_matrix.append(result_row)

    # 輸出結果
    for row in result_matrix:
        print(*row)
