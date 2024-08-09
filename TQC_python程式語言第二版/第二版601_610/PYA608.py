bases=[0,0,0,0]
scores=0
for _ in range(10):
    hit=int(input())
    if hit!=0:
        bases[0]=1
        
        for _ in range(hit):
            for i in range(3,-1,-1):
                if bases[i]==1:
                    if i+1>=4:
                        scores+=1
                    else:
                        bases[i+1]=1
                    bases[i]=0
print(f'score = {scores}')


























# bases=[0,0,0,0]
# #計算壘包 本壘,1,2,3,4
# scores=0
# # 記錄得分的初始值

# for _ in range(10):
#     #x 變數不重要
#     hit=int(input())
# #用者輸入十個0~4之間的整數    
#     if hit!=0: #不是三振的情況下
# #這是一個迴圈，迴圈的次數由之前用戶輸入的 hit 值來決定。
# #每一次迴圈模擬一個打擊的結果。        
#         for _ in range(hit):
# #這是另一個巢狀的迴圈，用來對每個跑者進行移動。
# # 它從最右邊的位置開始（bases[3]，本開始的位置），
# # 向左遍歷到最左邊的位置（bases[0]，本壘的位置）。
#             for i in range(3,-1,-1):
#                 if bases[i]==1:
# #檢查當前位置是否有跑者。如果 bases[i] 為 1，表示這個位置有跑者。
#                     if i+1>=4:
#                         scores+=1
# #檢查跑者是否已經到達本壘（bases[0]），
# #即最最左邊的位置。如果 i + 1 大於或等於 4，表示跑者到達本壘   
#                     else:
#                         bases[i+1]=1
# #跑者還沒有到達本壘，則將跑者移動到右邊一個位置（bases[i + 1] = 1）
# #表示跑者向下一個壘包移動                        
#                     bases[i]=0
# #最後，不論跑者是否已經到達本壘，都將當前位置的跑者清零，表示這個位置沒有跑者了。
# print(f'score = {scores}')
     








# bases=[0,0,0,0]
# score=0

# for _ in range(4):
#     hit=int(input())
    
#     if hit!=0:
#         bases[0]=1
        
#         for _ in range(hit):
#             for i in range(3,-1,-1):
#                 if bases[i]==1:
#                     if i+1>=4:
#                         score+=1
#                     else:
#                         bases[i+1]=1
#                     bases[i]=0
# print(f'score = {score}')







# # 讓使用者輸入十個0~4之間的整數
# for _ in range(10):
#     hit = int(input())
    
#     if hit != 0:
#         # 將本壘有跑者
#         bases[0] = 1

#         for _ in range(hit):
#             # 對每個跑者進行移動，從右至左
#             for i in range(4, -1, -1):
#                 if bases[i] == 1:
#                     if i + 1 >= 4:
#                         # 如果跑者從本壘出局，得分加一
#                         score += 1
#                     else:
#                         bases[i + 1] = 1
#                     bases[i] = 0

# # 輸出得分
# print(f'score = {score}')

