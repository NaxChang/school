def compute(word):
    s0=ord(word[0])
    s1=ord(word[1])
    s2=ord(word[2])
    s3=ord(word[3])
    s4=ord(word[4])
    s5=ord(word[5])-ord('A')+1
    if ((s0+s2+s4)+(s1+s3)*5)%26==s5:
        return True
    return False
    
    #(1+3+5+(6*5)) 39%26=13 
    #ord('0')=48
    #ord('A')=65 +1 是因為要包含本身
    #ord('M')=77 第十三個數字 
for i in range(3):
    id=input()
    if compute(id):
        print('Pass')
    else:
        print('Fail')
'''       
12345M
55237B
03805A

22222A
'''












# def compute(word):
#     s0 = ord(word[0]) - ord('0')
#     s1 = ord(word[1]) - ord('0')
#     s2 = ord(word[2]) - ord('0')
#     s3 = ord(word[3]) - ord('0')
#     s4 = ord(word[4]) - ord('0')
#     s5 = ord(word[5]) - ord('A') + 1


#     if (s0 + s2 + s4 + (s1 + s3) * 5) % 26 == s5:
#         return True
#     else:
#         return False

# for i in range(3):
#     student_id = input()
#     if compute(student_id):
#         print("Pass")
#     else:
#         print("Fail")
