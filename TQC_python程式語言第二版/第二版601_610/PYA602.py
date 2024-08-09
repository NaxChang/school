s=input()# ComPuTer
U=[]#CPT
L=[]#omuer       
for i in range(len(s)):
    if ord(s[i])>=97:
        L.append(s[i])
    else:
        U.append(s[i])

for i in range(len(U)):
    print(U[i],end='')
print()
for i in range(len(L)):
    print(L[i],end='')
print()
print(len(U))


'''
ord('a')=97
ord('A')=65
ord('Z')=90
'''






















# s=input()
# U=[]
# L=[]
# for i in range(len(s)):
#   if (ord(s[i])>=97):
#     L.append(s[i])
#   else:
#     U.append(s[i])
# for i in range(len(U)):
#   print(U[i],end='')
# print()
# for j in range(len(L)):
#   print(L[j], end='')
# print()
# print(len(U))
# # 讀取輸入字串
# input_str = input()

# # 初始化大寫字串和小寫字串
# uppercase_str = ""
# lowercase_str = ""

# # 遍歷輸入字串中的每個字元
# for char in input_str:
#     if char.isupper():
#         uppercase_str += char  # 如果是大寫字母，加入到大寫字串
#     else:
#         lowercase_str += char  # 否則加入到小寫字串

# # 輸出大寫字串、小寫字串和大寫字母的數量
# print(uppercase_str)
# print(lowercase_str)
# print(len(uppercase_str))
