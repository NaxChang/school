with open('read.txt','r',encoding='utf8')as f: #首先讀檔,變數存放
    data=f.read() #讀出來的檔案也給它變數data存放

newdata = ""
for x in data:
    newdata+=(chr( (ord(x)-97+2)%26 +97 ) )

with open('write.txt','w',encoding='utf8')as f: # 寫檔
    f.write(newdata)