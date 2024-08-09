
card1,card2=input().split()

suits={'S':4,'H':3,'D':2,'C':1}

num1,num2=int(card1[1:]),int(card2[1:])

if suits[card1[0]]>suits[card2[0]]:
    result=f'{card1} > {card2}'
elif suits[card1[0]]<suits[card2[0]]:
    result=f'{card1} < {card2}'
elif num1>num2:
    result=f'{card1} > {card2}'
elif num1<num2:
    result=f'{card1} < {card2}'
else:
    result=f'{card1} = {card2}'
print(result)



















# card1,card2=input().split()

# suits={'S':4,'H':3,'D':2,'C':1}



# num1,num2=int(card1[1:]),int(card2[1:])
# if suits[card1[0]]>suits[card2[0]]:
#     result=f'{card1} > {card2}'
# elif suits[card1[0]]<suits[card2[0]]:
#     result=f'{card1} < {card2}'

# elif num1>num2:
#     result=f'{card1} > {card2}'
# elif num1<num2:
#     result=f'{card1} < {card2}'
# else:
#     result=f'{card1} = {card2}'    
# print(result)








# elif num1>num2:
#     result=f'{card1} > {card2}'
# elif num1<num2:
#     result=f'{card1} < {card2}'
# else:
#     result=f'{card1} = {card2}'

# print(result)

# card1,card2=input().split()
# # 定義撲克牌的花色順序
# suits={'S':4,'H':3,'D':2,'C':1}
# # # 將撲克牌轉換成比較用的數字
# num1,num2=int(card1[1:]),int(card2[1:])
# #比較花色和數字，並輸出結果
# #先比花色第0項,再比數字第1項
# if suits[card1[0]]>suits[card2[0]]:
#     result=f'{card1} > {card2}'
# elif suits[card1[0]]<suits[card2[0]]:
#     result=f'{card1} < {card2}'
# elif num1>num2:
#     result=f'{card1} > {card2}'
# elif num1<num2:
#     result=f'{card1} < {card2}'
# else:
#     result=f'{card1} = {card2}'
# #輸出結果
# print(result)
    



































# # 讓使用者輸入兩張撲克牌
# card1, card2 = input().split()

# # 定義撲克牌的花色順序
# suits = {'S': 4, 'H': 3, 'D': 2, 'C': 1}

# # 將撲克牌轉換成比較用的數字
# num1, num2 = int(card1[1:]), int(card2[1:])

# # 比較花色和數字，並輸出結果
# if suits[card1[0]] > suits[card2[0]]:
#     result = f'{card1} > {card2}'
# elif suits[card1[0]] < suits[card2[0]]:
#     result = f'{card1} < {card2}'
# elif num1 > num2:
#     result = f'{card1} > {card2}'
# elif num1 < num2:
#     result = f'{card1} < {card2}'
# else:
#     result = f'{card1} = {card2}'

# # 輸出比較結果
# print(result)