input_str=input()
n=eval(input())
if 0<=n<len(input_str):
    char_at_n=input_str[n]
    new_char=char_at_n.swapcase()
    reslut=input_str[:n]+new_char+input_str[n+1:]

print(f'The letter that was selected is: {new_char}')
print(reslut)

#關鍵-----輸入3就是abc+new_char
#找到D(3)加上3+1到最後

'''

'''


















# input_str=input()
# n=eval(input())
# if 0<=n<len(input_str):
#     char_at_n=input_str[n]
#     new_char=char_at_n.swapcase()
#     result=input_str[:n]+new_char+input_str[n+1:]
# #關鍵-----輸入3就是abc+new_char找到D(3)加上3+1到最後
# print(f'The letter that was selected is: {new_char}') 
# print(result)  