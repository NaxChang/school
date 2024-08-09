# 輸入,並給予初始值
y,m,d=map(int,input().split())
leap=False
valid=True
days=0
# # 先判斷閏年的部份
if y%400==0 or(y%4==0 and y%100!=0):
    feb=29
else:
    feb=28
 # # 驗證和月份天數：
md=[0,31,feb,31,30,31,30,31,31,30,31,30,31]
    # 日期驗證：
if d<=md[m]:
    pass 
else:
    valid=False
# # 累積天數: #假設2012 年就是31+29天
for i in range(1,m):
    days+=md[i]
#假設 3月7日 就是60+7=67
if valid:
    print(days+d)
else:
    print('error')
# # 輸出結果或錯誤




























# y,m,d = map(int, input().split())
# leap=False
# va=True
# days=0

# # 先判斷閏年的部份
# if y%400==0 or (y%4==0 and y%100!=0):
#   feb=29
# else:
#   feb=28
# # 驗證和月份天數：
# md = [0,31,feb,31,30,31,30,31,31,30,31,30,31]
# # 日期驗證：
# if d<=md[m]:
#   pass
# else:
#   va=False
# # 累積天數： 
# for i in range(1,m):
#   days +=md[i]
# # 輸出結果或錯誤
# if va:
#   print(days+d)
# else:
#   print('error')