
n,m=map(int,input().split())

array=[]

for i in range(n):
    row=list(map(int,input().split()))
    array.append(row)
    
for j in array:
    print(','.join(map(str,j)))
    































            
# [['1','1','1','1']]

# 1,1,1,1

# print(n,m)
# n,m = map(int, input().split())
# # print(n,m)
# L=[]
# for i in range(n):
#   nn=input().split()
#   L.append(nn)
# # print(L)
# for i in range(n):
#   print(','.join(L[i]))



# n,m = map(int, input().split())
# # print(n,m)
# L=[]
# for i in range(n):
#   nn=input().split()
#   L.append(nn)
# # print(L)
# for i in range(n):
#   print(','.join(L[i]))







# # 讀取兩個正整數n和m
# n,m=map(int,input().split())

# array=[]
# # 創建一個二維陣列，用來存儲輸入的整數
# for i in range(n): 
#     row=list(map(int,input().split()))
#     array.append(row)
# # 輸出二維陣列，以半形逗號隔開的形式
# for j in array:
#     print(",".join(map(str,j)))

# # 讀取兩個正整數n和m
# n, m = map(int, input().split())

# # 創建一個二維陣列，用來存儲輸入的整數
# array = []

# # 讀取n*m個整數並填充到二維陣列中
# for i in range(n):
#     row = list(map(int, input().split()))
#     array.append(row)

# # 輸出二維陣列，以半形逗號隔開的形式
# for row in array:
#     print(",".join(map(str, row)))