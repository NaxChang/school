---
title: Python筆記本
tag: python
---

# python記事本


## 簡介

非本科系學程式找工作
https://www.youtube.com/@pygit-docker/playlists

- **Python**：基礎與進階
- **NumPy**：數值運算與處理
- **Pandas**：資料處理與分析
- **爬蟲**：網頁資料擷取
- **資料視覺化**：使用 Matplotlib、Seaborn 等工具進行視覺化分析
- **Django**：網站開發框架
- ------------------
- **SQL/MySQL**
- **Linux/Docker**:Linux初階
- **Git**

- [基礎語法](#2025/02/06)
- [TQC-python](#2025/04/03)
- [檔案讀取與寫入](2025/03/31)
- [Tkinter模組](#2025/01/20)
- [數據資料的儲存與讀取](#2025/01/31)
- [猜數字遊戲](#2025/04/02)
- [錯誤處理](#2025/04/05)
- [類別與物件](#2025/01/16)
- [建立自己的模組](#2025/02/06)
- [函式（Function）](#2025/03/27)
- [numpy](#2025/01/25)
- [Django](#2025/02/07)
- [Django-ubantu環境](#2025/02/07)

# 基礎語法

## 字串的格式化操作

```python=
name = "nameless"
age = 30
# "I'am nameless, and 30 years old."

print("I'am " + name + ", and " + str(age) + " years old.")

print("I'am %s, and %d years old." % (name, age))

# age = "30"
print("I'am %s, and %s years old." % (name, age))
# 上面%d要改為%s

print("I'am {}, and {} years old.".format(name, age))

print("I'am {name}, and {age} years old.".format(name=name, age=age))

print("I'am {1}, and {0} years old.".format(age, name))

print(f"I'am { name}, and {age} years old.") # 推薦做法
```

## if判斷式
如何在判斷語句中來判斷True或False
bool 是一種資料類型，用來表示布林值
bool(1) 任何 非零數字（正數或負數）都會轉換為 True。
那在python中有那些布林值是False
它是空的列表與布林值無關,所以回傳False

```python=
fales_value = [False, [], {}, "", 0, 0.0, None]
for val in fales_value:
    print(True if val else False)
    # if val:
    #     print(True)
    # else:
    #     print(False)
    # print(f"{val} is {bool(val)}")
    # 全部都是False
```
我們知道 Python 內置了一些常見的數據類型
如果說我們有一個自定義的數據類型
可以表示True或False
```python=
class MyType:
    def __init__(self):
        self.value = []

    def add(self, x):
        self.value.append(x)

    def __bool__(self):
        return bool(self.value)


my_type = MyType()
bool(my_type)  # False
my_type.add(1)
bool(my_type)  # True
print(True if my_type else False) # True
```

### 如何正確使用返回值 None
如何正確使用返回值 None，
並了解它在程式中的應用。下面的範例包含了三個函式
我們將透過這些函式來模擬連線測試和用戶資料的獲取。

```python=
def test_connection():
    return True


def get():
    return []
    # return ["user1", "user2", "user3"]


def get_user_list():
    if not test_connection():
        return None
    else:
        return get()


user_list = get_user_list()
# if not user_list:
if user_list is None:
    print("Connection error")
# if not user_list:
else:
    print(user_list)
```

最後做法
```python=
def test_connection():
    return True


def get():
    return []


def get_user_list():
    if not test_connection():
        return None
    return get()


user_list = get_user_list()
if user_list is None:
    print("Connection error")
print("user_list:", user_list)
```
user_list是False的原因是什麼?因為它是一個空的list
可是呢?我們一開始給它test_connection
是回傳True,它是成功的,表示邏輯上的錯誤
它的布林值有多種返回值而且是相同的
例如說:None,返回False,而且return get()
是空的list,返回也是False
這樣就不好區分了,所以為了做區分
我們要重新修改,去明確的定義

### if判斷式優化
今天來介紹if判斷式,大家可以複製我的程式碼就可以了
主要是介紹如何修改,打字不是重點
當我的判斷條件較多的時候,那代碼要怎麼優化

這個value假設是1,那就是Condition.A以此類推
如果choice等於condition.A或等於
condition.B 或等於condition.C的情況下
印出結果1,否則呢?印出結果2
可是這樣寫可能有點問題?
這個choice一共就四種選擇,if判斷式A,B,C
剩下的條件就等D,對吧!它不可能等於其它的值
```python=
import random
from enum import Enum


class Condition(Enum):
    A = 1
    B = 2
    C = 3
    D = 4


print(repr(Condition.A))
print(Condition.A.name)
print(Condition.A.value)

values = [1, 2, 3, 4]
choice = Condition(random.choice(values))
if choice == Condition.D:
    print("result_2")
else:
    print("result_1")
# if choice == Condition.A or choice == Condition.B or choice == Condition.C:
#     print("result_1")
# else:
#     print("result_2")
```

- 用list的方式最好
```python=
values = [1, 2, 3, 4]
choice = Condition(random.choice(values))
option = [Condition.A, Condition.B]
if choice in option:
    # if choice == Condition.A or choice == Condition.B:
    print("result_1")
else:
    print("result_2")
```

## 串列
這裡簡單做一個購物清單.先定義一個空列表,中括號表示
我要附加東西進去,可以用append
方法一般在操作對象後面加點方法名,小括號(),就可以被調用

```python=
shopping_list = []
# shopping_list.append("滑鼠")
# shopping_list.append("鍵盤")
# shopping_list.append("螢幕")
# shopping_list.append("音響")
shopping_list.extend(["滑鼠", "鍵盤", "螢幕", "音響"])
print(shopping_list)
```

extend() 方法是用來將一個可迭代對象,（例如另一個列表）中的元素添加到原來的列表中或者是用運算符
```python=
shopping_list += ["滑鼠", "鍵盤", "螢幕", "音響"]
print(shopping_list)
```

```python=
print(len(shopping_list)) # 印出長度
print(shopping_list[0]) # 找索引值
shopping_list[1] = "主機" # 將鍵盤替換成主機
shopping_list # 將結果印出
```


### 列表解析

```python=
a = [1, 2, 3, 4, 5, 6, 7]
b= []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)
```

```python=
可以改寫為
a = [1, 2, 3, 4, 5, 6, 7]
b= [i for i in a if i % 2 == 0]
print(b)
```

- 測試用1
```python=
import time

start = time.time()
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(time.time() - start)
```

- 測試用2
```python=
import time

start = time.time()
b = [i for i in a if i % 2 == 0]
print(time.time() - start)
print(type(b))
```
可以比較測試1還有測試2的執行速度

### 串列操作
list1 = [1, 2, 3, 4, 5, 6]

```python= 
print(len(list1)) # 長度 6
print(max(list1)) # 最大值 6
print(min(list1)) # 最小值 1
print(list1.index(3)) # 查看3的索引值 2
print(list1.count(3)) # 查看3出現的次數 1次
```
假設串列重複兩次
```python= 
list2 = list1 * 2
list2 # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
```
### 以串列計算班級成績
學生成績須輸入串列中,變成串列元素
如果輸入[-1],表示成績結束,最後顯示班上總成績和平均成績
總成績與平均成績至小數點第二位
![image](https://hackmd.io/_uploads/ByqCHlBvkl.png)
<details>
<summary>點此展開程式碼</summary>

```python=
score = []
total = incore = 0
while incore != -1:
    incore = int(input("請輸入分數: "))
    score.append(incore)
print(f"共有幾位學生: {len(score) - 1}")
for i in range(0, len(score) - 1):
    total += score[i]
    avg = total / (len(score) - 1)
print(f"總成績為: {total:.2f},平均成績為: {avg:.2f}")
```
</details>


## 字典

字典（Dictionary）是一種無序的資料結構，用來儲存由鍵（Key）與對應的值（Value）組成的對。你可以透過鍵來快速查詢相關聯的值。

字典的主要特點包括：

無序性（Unordered）：字典內的元素並沒有特定的順序，因此無法像串列那樣使用索引來存取。必須根據鍵來獲取相應的值。
可變性（Mutable）：字典是可變的，這表示可以對字典中的內容進行修改、刪除或新增元素。
唯一鍵（Unique Keys）：字典中的鍵必須是唯一的，不能出現重複的鍵。每個鍵只能對應到一個值。


```python=

l = [1, 2, 3, 4]

a = {
    "one": 1,  
    "two": 2,  
    "three": 3,
    "four": 4,   
}
```

何謂唯一值
```python=
a = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "one": 11,
    "one": 111,
}

print(a["one"])
# 111
```

```python=
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print(my_dict)
# {'three': 3, 'one': 1, 'four': 4, 'two': 2}
```

### 字典的建立：

透過 {} 來建立字典並透過 : 分隔鍵與值

```python=
person = {
    "姓名": "Nameless",
    "年齡": 30,
    "職業": "找工作",
}
```
字典的查詢：

取得字典值的方法與串列的類似，只是 [] 中傳入的不是索引值而是鍵

```python=
print("姓名：", person["姓名"])  # 輸出：姓名：Nameless
print("年齡：", person["年齡"])  # 輸出：年齡：30
print("職業：", person["職業"])  # 輸出：職業：找工作
```

要注意的是如果使用 [] 訪問值，如果指定的鍵不存在則會引發 KeyError 錯誤，這時可以透過 get() 進行查詢，這樣如果找不到指定鍵的值則會回傳 None。

```python=
print(person.get("地址"))  # 輸出：None
你也可以透過指定預設值的方式，讓 get() 在找不到對應的值時回傳預設值給你
```
那你可能會說,我不要它回傳None
你可以這樣做

```python=
print(person.get("地址", "無地址"))
```

```python=
print(person.get("性別", "未知"))  # 輸出：未知
```

取得所有的key,values,可以這樣做
```python=
print(person.keys())  # 取得所有鍵
print(person.values())  # 取得所有值
```

### 字典與迴圈有三種搭配方式
```python=
person = {
    "姓名": "Nameless",
    "年齡": 30,
    "職業": "找工作",
}

for key, value in person.items():
    print(key, ":", value)

# for value in person.values():
#     print(value)
# 印出value
# for key in person.keys():
#     print(key)
# 印出key
```
## 元組/數組（Tuple）
在 Python 中，元組（Tuple）是一種不允許變更的資料結構，用來儲存一系列有順序的元素。雖然元組與串列非常相似，但其最大的不同在於，元組中的元素一旦設置後，就無法再進行修改、刪除或新增，因此元組的內容是固定的。

以下是元組的主要特點：

- 不可變性（Immutable）：一旦元組被創建，它的內容無法進行任何更改，也不能添加或刪除元素。這使得元組屬於不可變資料結構。
- 有序性（Ordered）：元組中的元素是依照插入的順序進行排列的，並且這個順序會保持不變。
- 多樣性（Heterogeneous）：元組可以包含不同類型的元素，像是整數、浮點數、字串等，可以用來儲存各種不同的資料類型。

```python=
my_tuple = (1, "二", 3, 4.0, 5)

my_tuple[1] = "三",

print(my_tuyple[1])
# 'tuple' object does not support item assignment 
```



```python=
# 訪問元組中的元素

my_tuple = (1, "二", 3, 4.0, 5)

print(my_tuple[0]) # 1
print(my_tuple[1]) # "二"


# 可以支援字串切片

my_tuple = (1, "二", 3, 4.0, 5)

slice_tuple = my_tuple[1:4]

print(slice_tuple)
# ('二', 3, 4.0)

# 可以尋找長度
print(len(my_tuple))
# 5
```
```python=
test = (1)
print(type(test))
# 會印出整數int
# <class 'int'>

```
印出型態之後.會發現是整數 
原因是小括號除了代表tuple宣告的值以外
它還代表了四則運算的優先運算

那你可能會說,我就是只想要有一個tuple
裡面有一個值,要怎麼做?
```python=
test = (1,)
<class 'tuple'>
```

改為一個逗號,再執行一次就會變成tuple了

```python=
test = [1]

print(type(test))
# <class 'list'>
```

要特別注意的是在宣告元組時如果只有一個元素要記得加上逗號，不然 Python 不會將他視為元組。


```python=
a = (1)
print(type(a))  # 輸出：<class 'int'>

b = (1,)
print(type(b))  # 輸出：<class 'tuple'>
```

元組（tuple）也可以使用 count() 和 index() 方法，這些方法的使用方式與串列（list）相同。

然而，若想要將元素新增到元組中，可以透過 += 來達成類似的效果。不過需要注意，這樣的操作會創建一個新的元組，並將原來的元組與新元素結合，而不是直接修改原有的元組。這點與串列的 append() 方法不同，因為 append() 會直接修改原串列。



```python=
my_tuple += (1,)
```

```python=
test_02 = ()

print(id(test_02))

test_02 += (1,)

print(test_02)

print(id(test_02))
```
會看到不同id

以下我再做個實驗,改為list
```python=
test_03 = []
print(id(test_03))
test_03.append(1)
print(id(test_03))
```
會看到相同id

## 集合

集合是一種無序、可變的資料結構，用來儲存一組唯一的元素。集合中的元素不允許重複，且沒有固定的順序。集合常用於去除重複元素，並且支援一些數學運算，例如聯集、交集和差集等。

以下是集合的主要特點：


- 1.無序性（Unordered）：集合中的元素是無序的，因此你不能通過索引來訪問集合中的元素。
- 2.不允許重複（No Duplicates）：集合中的元素是唯一的，不允許有重複的元素。
- 3.可變性（Mutable）：集合是可變的，你可以添加或刪除元素

### 建立集合

```python=
# 創建一個集合
my_set = {1, 2, 3, 4, 5}
print(my_set)  # 輸出：{1, 2, 3, 4, 5}

# 添加元素到集合
my_set.add(6)
print(my_set)  # 輸出：{1, 2, 3, 4, 5, 6}

# 刪除元素從集合
my_set.remove(3)
print(my_set)  # 輸出：{1, 2, 4, 5, 6}

# 集合的長度
print("集合長度：", len(my_set))  # 輸出：集合長度：5
```

有時候,會遇到一種情況,就是將list中的重複資料去除

```python=
a = ["a", "b", "a", "a", "c"]
print(list(set(a))) # ['b', 'a', 'c']
print(sorted(list(set(a)))) # ['a', 'b', 'c']
```

#### 實驗
在python中,當我宣告一個大括號裡面空的
裡面沒有任何值,它無從判斷,它會優先認為是dictionary
```python=
my_set = {}
print(type(my_set ))
# <class 'dict'>
```

檢查型態
```python=
fruits = {"香蕉", "蘋果", "橘子"}
print(fruits)
type(fruits)
```
那集合的元素是不可重複的,如果資料重複,多於的元素會被捨去

```python=
fruits = {"香蕉", "蘋果", "橘子", "香蕉",}
print(fruits) # {'香蕉', '蘋果', '橘子'}
```
香蕉因為重複,因此只保留一筆香蕉的資料

可以使用不同類別的集合元素
```python=
fruits = {"香蕉", "蘋果", "橘子", "香蕉", 100, (1, 2)}
```

但是不可以使用串列,字典集合,下面範例中使用串列當作集合的元素,將會報錯

```python=
fruits = {"香蕉", "蘋果", "橘子", "香蕉", 100, [1, 2]}
```

**使用set()函式建立集合**
set函式的參數內容可以是字串,串列,元組,這些參數都會轉換成集合元素,例如:將串列轉換成集合

```python=
fruits = set(["香蕉", "蘋果", "橘子", "香蕉"])
print(fruits)
print(type(fruits))
```
`{'蘋果', '橘子', '香蕉'}`
`<class 'set'>`

如果集合的參數是字串,集合元素將轉換成字元,同時會去除重複的字元

```python=
s = set("good day!!")
print(s)
print(type(s))
```

``{'y', '!', 'd', 'g', 'o', 'a', ' '}``
``<class 'set'>``


### 集合的操作
|   運算子|   意義   |
|--------|--------|
|&  |交集  |
|  |聯集  |
|- |差集  |
|^  |對稱差集  |
|==  |等於  |
|!=  |不等於  |
|in  |是成員  |
|not in  |不是成員  |


![image](https://hackmd.io/_uploads/HJ90mcAnJe.png)



```python=
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
```
#### 聯集
```python=
union_set = set1.union(set2)
print(union_set)  # 輸出：{1, 2, 3, 4, 5, 6}
```

#### 交集
```python=
intersection_set = set1.intersection(set2)
print(intersection_set)  # 輸出：{3, 4}
```

#### 差集
```python=
difference_set = set1.difference(set2)
print(difference_set)  # 輸出：{1, 2}
```

#### 對稱差集
```python=
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # 輸出：{1, 2, 5, 6}
```

#### 改寫為符號
```python=
union_set = set1 | set2
print(union_set)  # 輸出：{1, 2, 3, 4, 5, 6}

intersection_set = set1 & set2
print(intersection_set)  # 輸出：{3, 4}

difference_set = set1 - set2
print(difference_set)  # 輸出：{1, 2}

symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # 輸出：{1, 2, 5, 6}
```


## random模組
random.random()函數可以生成0~1的隨機浮點數

```python=
import random

num = random.random()

print(num) # 產生0-1的隨機
print(round(num, 2)) # 讓它小數點第二位
```

那你可能會說,我要1到5的隨機浮點數,可以這樣做
```python=
import random

num = random.uniform(1,5)
print(num)

```
### random.randint()
random.randint()函數可以生成一個
指定範圍內的整數,語法如下:
```python=
randint(值1, 值2)
```
如此可以產生隨機取得值1到值2之間的一個整數,包含值1和值2

### random.randrange()
randrange()函數可以生成指定範圍的整數,但不包含結尾
```python=
random.randrange(起點, 終點, 間隔):
```
```python=
import random

num = random.randrange(1, 10, 2)
print(num)
```
多執行幾次,可以看到每次都產生不同的數字

### random.choice()

choice()函數可以從指定的序列中隨機選擇一個元素,語法如下:
```python=
choice(序列資料)
```
各位,請注意
random.choice() 只接受一個參數，這個參數必須是可迭代的物件

```python=
import random

result = random.choice([10, 20, 30, 40, 50])
print(result)
```
random.choice() 只接受一個參數。Python 無法將這些獨立的數值組合成一個序列，這樣就會導致錯誤。正確的做法是將這些數值包裝在一個序列（例如列表或元組）中，再傳入函數中。

## math 模組
math模組是python內建的數學運算模組,提供大量數學函數,math模組可以方便地進行數學計算,math模組中常用的函式如下:
**1.求平方根**
sqrt(x)函式返回x的平方根
```python=
import math


```
**2.pow(x,y)的函式返回x的y次方**

```python=
import math

result = math.pow(3, 3)
print(result) #
```


## 連接與字串分割
join函式可以將串列中元素連接成一個字串,語法如下:
`連接字串.join(串列)`
```python=
list1 = ["I", "am", "Nameless."]
print(" ".join(list1))
print("|".join(list1))
# I am Nameless. 空白做結合
# I|am|Nameless. | 做結合
```
split函式的功能與join相反,是將一個字串以指定方式分割為串列,語法如下:
`字串.split([分隔字串])`

```python=
str1 = "This is a book."
print(str1.split(" "))
print(str1.split())
# ['This', 'is', 'a', 'book.']
# ['This', 'is', 'a', 'book.']
```
分隔字串可有可無,若未傳入分隔字串,預設為1個空白字元
例如說:我以下有yyy,那我以它做分隔
```python=
str2= "Thisyyyisyyyayyybook."
print(str2.split("yyy"))
# ['This', 'is', 'a', 'book.']
```
就可以看到結果與上述相同
### 檢查起始或結束字串
**startswith**
startswith函式是檢查字串是否以指定字串開頭
語法如下:
```python=
字串.startswith(起始字串)
```
如果字串式以[起始字串]開頭,則回傳true
否則回傳false
```python=
str3 = "email:python.com.tw"
print(str3.startswith("email")
# True
print(str3.startswith("tw"))
# False
```
endswith函式的功能與starstwith類似
差異在endswith函式檢查的是字串是否以指定結束字串,語法如下
```python=
字串.endswith(起始字串)
```
如果字串式以[結尾字串]結束,則回傳true
否則回傳false
```python=
str3 = "email:python.com.tw"
print(str3.endswith("tw"))
# True
print(str3.endswith("email"))
# False
```
### 範例練習

**如果是http://或者 https:// 開頭
則輸出:("輸入網址格式正確")
否則輸出:("輸入網址格式錯誤")**

結果如下:
![image](https://hackmd.io/_uploads/HkMHvmXKkl.png)
![image](https://hackmd.io/_uploads/r12UPQQYJg.png)


<details>
<summary>點此展開程式碼</summary>

web_str = input("請輸入網址: ")
if web_str.startswith("http://") or web_str.startswith("https://"):
    print("輸入網址格式正確")
else:
    print("輸入網址格式錯誤")
</details>

http://www.python.com.tw

## 指數,商數,餘數及四捨六入

### pow函式

pow函式不但可以做指數運算,還可以計算餘數,語法如下:
```python=
pow(x, y[, z])
```
如果只有x及y參數,傳回值為x的y次方,例如:
```python=
pow(3 ,4) # 81 
```
若有z參數,意義為x的y次方除以z的餘數
```python=
pow(3 ,4 ,5) # 1 
```
3的4次方為81,81除以5為16剩餘1

如果傳入三個參數 x, y, z，則會先計算 x 的 y 次方，
再對 z 取餘數（也就是求 (x ** y) % z 的結果）
### divmod函式
**divmod函式會同時回傳商數與餘數**
divmod() 的返回結果是元組（tuple）
語法如下:
```python=
divmod(x, y)
```
```python=
result = divmod(11, 3)
print(result)
# (3, 2)
```
商數為3, 餘數為2
```python=
print(result[0])
print(result[1])
```
### round函式
round函式以四捨六入的方法取得x近似值,語法如下
```python=
round(x [, y])
```

```python=
print(round(3.4)) # 3
print(round(3.6)) # 4
print(round(3.5)) # 4
print(round(2.5)) # 2
```
四捨六入是4以下(包含4)的數字捨去,6以上(包含6)以上的數字進位
那5呢?就必須視前一個位數而定,前一位是偶數就將5捨去
前一位是奇數,就將其進位

換個例子,現在加入y參數
```python=
print(round(3.95, 1)) # 4
print(round(3.855, 2)) # 3.85
print(round(3.845, 2)) # 3.85
```

說明:
偶數四捨五入,小數點後三位是5
那前面的的小數點第2位是奇數,不進位所以是3.85
最後一個3.845,第2位是偶數,所以會進位 3.85

#### 綜合驗收
**輸入人數與麵包總數,將麵包平均分給學生
每個人分到的麵包必須是相同的
1.計算麵包平均分配到多少學生
2.計算剩餘麵包數量
假設人數為12人,麵包總數為:100,會剩下4個麵包**

<details>
<summary>點此展開程式碼</summary>

```python=
person = int(input())
bread = int(input())
result= divmod(bread, person)
print(f'分配: {result[0]} 人')
print(f'剩餘: {result[1]} 個麵包')
```
</details>

結果如下:
![image](https://hackmd.io/_uploads/SJ89hjeKyx.png)

## 檔案讀取與寫入

### 檔案讀取
在 Python 中，您可以使用內建的 open() 函式來開啟檔案，並指定不同的模式（如讀取模式、寫入模式、附加模式等）來進行相應的操作。

使用 open() 函式以讀取模式（'r'）開啟檔案，然後使用 read() 方法讀取檔案內容：
```python=
file_path = "example.txt"
file = open(file_path, "r")
content = file.read()
print(content)
file.close()
```

在此範例中，我們以讀取模式 'r' 開啟名為 example.txt 的檔案，使用 read() 方法取得檔案內容並儲存至變數 content，接著輸出內容，最後使用 close() 關閉檔案。

只是每次都要關檔有點麻煩，而且有可能因為還沒執行到關檔就發生錯誤，所以沒有正確關閉檔案。為了解決這些問題我們將上方範例改寫



```python=
file_path = "example.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)
```

在此範例中，with 陳述式會在程式碼區塊結束時自動關閉檔案，無需手動呼叫 close()。

若需逐行讀取檔案內容，特別是在處理大型檔案時，以下範例示範如何逐行讀取並處理每一行


```python=
with open(file_path, "r") as file:
    for line in file:
        print(line.strip())  # 刪除每行末尾的換行符號
```
除了 "r" 模式外，open() 函式還支援其他模式，如 "w"（寫入模式）、"a"（附加模式） 等。如果在寫入或附加模式下，如果指定的檔案不存在，Python 會自動創建該檔案。


## 函式（Function）

函式是一個可以重複使用的程式區塊，通常用來執行特定的任務或操作。使用函式能讓程式碼結構變得更簡潔，且易於理解和維護。

### 定義一個簡單的函式

首先，我們來定義一個基本的函式，這個函式會輸出 "Hello World!"：

```python=
def greet():
    print("Hello World!!!")
```
接著，我們可以呼叫這個函式：

```python=
greet()
```
讓函式根據參數進行動作
如果希望函式能根據不同的呼叫者輸出不同的訊息，可以讓函式接受一個參數：

```python=
def greet(name):
    print(f"Hello, {name}!!!")
```

然後可以這樣呼叫：

```python=
greet("Tom")  # 輸出：Hello, Tom!!!
greet("Sam")  # 輸出：Hello, Sam!!!
```
函式回傳運算結果
有時候，我們希望函式進行一些計算並回傳結果，可以使用 return：

```python=
def add(a, b):
    return a + b
```

```python=
print(add(1, 2))  # 輸出：3
```
位置與名稱傳遞參數
在 Python 中，傳遞參數有兩種方式：依照位置或依照名稱傳入。這兩種方式可以混合使用，但要注意位置參數必須在名稱參數之前傳入：

```python=
print(add(1, 2))        # 依位置傳參數
print(add(b=2, a=1))    # 依名稱傳參數
```

混合位置參數與名稱參數
以下是合法與不合法的呼叫範例：

```python=
add(1, 2)        # 合法
add(b=2, a=1)    # 合法
add(1, b=2)      # 合法
add(a=1, 2)      # 不合法，名稱參數不能在位置參數前
add(1, a=1)      # 不合法，名稱參數不能指定已經傳入的參數
```

回傳多個值
有時我們希望函式回傳多個結果，可以直接回傳一個元組：

```python=
def add_and_subtract(a, b):
    return a + b, a - b
```
可以這樣使用：

```python=
result = add_and_subtract(1, 2)
print(result)  # 輸出：(3, -1)

sum_result, diff_result = add_and_subtract(1, 2)   
# 拆解元組
print(sum_result, diff_result)  # 輸出：3 -1
```
提前退出函式
有時候，當某些條件成立時，我們希望函式提前退出並不執行後續的程式碼，可以使用 return：

```python=
def shop(money):
    if money <= 0:
        return
    print("購物中...")
```

如果傳入 money <= 0，則函式會提前返回，後面的程式不會被執行。

預設參數值
如果希望函式的某些參數具有預設值，這樣在呼叫時如果未傳入對應的參數，會使用預設值：

```python=
def greet(name="World"):
    print(f"Hello, {name}!!!")
```
呼叫函式時：

```python=
greet()       # 輸出：Hello, World!!!
greet("Ruby") # 輸出：Hello, Ruby!!!
```

接受不定數量的參數
若希望函式接受不確定數量的參數，可以使用 *args 和 **kwargs：

```python=
def func(*args, **kwargs):
    print(args, kwargs)
*args：接收依照位置傳遞的多個參數，並將它們組成元組。

**kwargs：接收依照名稱傳遞的多個參數，並將它們組成字典。
```

範例：

```python=
func()  # 輸出：() {}
func(1, 2, 3)  # 輸出：(1, 2, 3) {}
func(a=1, b=2, c=3)  # 輸出：() {'a': 1, 'b': 2, 'c': 3}
func(1, 2, x=3)  # 輸出：(1, 2) {'x': 3}
```


# TQC-python

## 第一版

### 701-710
#### 703


![image](https://hackmd.io/_uploads/S1U8lYiT1x.png)


![image](https://hackmd.io/_uploads/HJUPgYiTkl.png)

海象運算子(python ver_3.8) 解法

<details>
<summary>點此展開程式碼</summary>

```python
words = ()

while (word := input()) != "end":
    words += (word,)
print(words)
print(words[:3])
print(words[-3:])

```
</details>






### 寫入檔案
```python=
with open("output.txt", "w") as file:
    file.write("這是寫入的內容\n")
```
### 附加到檔案
```python=
with open("output.txt", "a") as file:
    file.write("這是附加的內容\n")
```

上方提到的模式都只能進行單一行為操作，如果有需要同時寫入跟讀取可以直接在現有模式後方加上 + 即可。

下方是對 r、r+、w、w+、a 和 a+ 模式進行比較的表格：


| 模式  | 讀取 | 寫入 | 清空檔案 | 檔案不存在時的行為 |
|-------|------|------|----------|---------------------|
| `r`   | 可   | 不可 | 不會     | 錯誤                |
| `r+`  | 可   | 可   | 不會     | 錯誤                |
| `w`   | 不可 | 可   | 會       | 創建新檔案          |
| `w+`  | 可   | 可   | 會       | 創建新檔案          |
| `a`   | 不可 | 可   | 不會     | 創建新檔案          |
| `a+`  | 可   | 可   | 不會     | 創建新檔案          |


# Tkinter模組

## 視窗區塊

當我們元件數量增加時.許多元件
都集中再主視窗,看起來會很亂
視窗區塊也是一個容器,可以將元件分類置不同區塊中
![image](https://hackmd.io/_uploads/ry_GPqiv1l.png)

* 建立視窗區塊的語法為:

```python=
視窗區塊變數 = tk.Frame(容器名稱, 參數1, 參數2....)
```
在主視窗 win 中創建一個名為 frame1 的視窗區塊，可以這樣寫：
```pytohn=
frame1 = tk.Frame(win)
```

標籤是使用 tk.Label 類別創建的。通常，標籤顯示的文字或圖片會在同時使用配置選項時指定：

```python=
label = tk.Label(parent, text='Full name:')
```
參考文件 Label
* https://tkdocs.com/tutorial/widgets.html#label

```python=
entry = tk.Entry(parent, textvariable=username)
```
參考文件 Entry
https://tkdocs.com/tutorial/widgets.html#entry

* 關於.grid(),標籤與文字框可以理解為位置

|        |   column 0|   column 1    |
|--------|--------|--------|
| row0   |label1  |entry1  |
* 這讓視窗持續顯示，並等候用戶操作
```python=
win.mainloop() 
```
<details>
<summary>點此展開程式碼</summary>

```python=
import tkinter as tk

win = tk.Tk()
win.title("標題")

# 第一種視窗區塊

frame1 = tk.Frame(win)
frame1.pack()

label1 = tk.Label(frame1, text="文字標籤", font=("Arial", 16))
entry1 = tk.Entry(frame1)
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
# 第二種視窗區塊
frame2 = tk.Frame(win)
frame2.pack()
button1 = tk.Button(frame2, text="確定", font=("Arial", 16), padx=20)
button2 = tk.Button(frame2, text="取消", font=("Arial", 16), padx=20)
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)

win.mainloop()

```
</details>

*執行結果如下:*

![image](https://hackmd.io/_uploads/H1T-P9ow1e.png)



# 數據資料的儲存與讀取
## csv資料的儲存與讀取
常聽到CSV檔案,那它的全名是什麼?
Comma(ˈkämə)-separated values
就是以逗號分隔值的資料格式並以純文字的方式儲存檔案

csv檔案是純文字檔案,編輯時可以直接使用文字編輯器
例如說:windows內建的記事本,但閱讀上比較不方便
大多數的人會用EXCEL來使用csv檔案

csv檔是許多資料編輯,讀取,儲存時很喜歡的格式
因為是純文檔案,操作方便且輕量
python,可以使用csv模組輕鬆來存取.csv檔案

### csv檔案儲存
可以使用串列或字典資料類型,將資料寫入csv檔案
而串列的寫入方式
**1.csv寫入物件.writerow():寫入一維串列**
__2.csv寫入物件.writerows():寫入二維串列__
```python=
import csv 
# 開啟輸出的csv檔案
with open("我要建立的檔名.csv","寫入w",newline="") as 檔案:
# 記得冒號和縮排
，
# 建立csv檔寫入物件
    變數存放 = csv.writer(檔案)
# 再拿變數去寫入一維串列
    變數.writerow([.., ..., ...])

```

w:表示如果檔案已經存在會覆蓋它。如果檔案不存在則會創建新檔案。
newline="": 這個參數告訴 Python 不要自動處理行尾的換行符號

<font size="5">將一維串列資料寫入csv檔案</font>
利用csv.writer方法,可以建立一個寫入csv檔案的物件,再利用writerow方法就可以寫入一維的串列資料

<details>
<summary>點此展開程式碼</summary>

```python=
import csv

with open("test01.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["姓名", "身高", "體重"])
    writer.writerow(["Nameless", "173", "76"])
    writer.writerow(["Joanna", "164", "76"])
```
</details>

製作結果如下:
![image](https://hackmd.io/_uploads/BJFKZAY_1x.png)


<font size="5">將二維串列資料寫入csv檔案</font>
除了一維的串列資料
也可以用writerows方法寫入二維的串列資料

```python=
import csv

csv_table = [
    ["姓名", "身高", "體重"],
    ["Nameless", "173", "76"],
    ["Joanna", "164", "76"],
]

with open("test02.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_table)
```
</details>

### 將字典資料寫入csv檔案
可以使用csv.DictWriter直接將字典類型的資料
寫入csv檔案中



```python=
import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

```
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
它的fieldnames是指欄位名稱
它的csv.DictWriter接收兩個參數,前面csvfile:將csvfile寫入
後面的fieldnames:是指欄位名稱
writer.writeheader():
是csv.DictWriter 物件中的一個方法，
它的作用是將 fieldnames 中定義的欄位名稱寫入 CSV 檔案的第一行，也就是標題行。

<details>
<summary>點此展開程式碼</summary>

```python=
import csv

filednames = ["姓名", "身高", "體重"] 

with open("test03.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, filednames) 

    writer.writeheader() 
    writer.writerow({"姓名": "Nameless", "身高": 173, "體重": 76}) 
    writer.writerow({"姓名": "Joanna", "身高": 164, "體重": 76}) 

```
</details>

結果如下:
![image](https://hackmd.io/_uploads/Hy9jnl5uyl.png)



官方文件參考:
**https://docs.python.org/3/library/csv.html**



# 猜數字遊戲



讓電腦隨機選擇一個介於 1 和 100 之間的數字（包含 1 和 100）。
接著，提示使用者猜測一個數字。系統會檢查使用者輸入的數字是否有效，並確認其在合法範圍內。

如果使用者猜的數字大於電腦選擇的數字，範圍會調整為 1 到使用者猜的數字減 1。
如果使用者猜的數字小於電腦的數字，範圍會調整為使用者猜的數字加 1 到 100。
這個過程會持續進行，直到使用者猜中正確的數字為止。

```python=
"""
讓電腦隨機選擇一個介於 1 和 100 之間的數字（包含 1 和 100）。
接著，提示使用者猜測一個數字。系統會檢查使用者輸入的數字是否有效，並確認其在合法範圍內。

如果使用者猜的數字大於電腦選擇的數字，範圍會調整為 1 到使用者猜的數字減 1。
如果使用者猜的數字小於電腦的數字，範圍會調整為使用者猜的數字加 1 到 100。
這個過程會持續進行，直到使用者猜中正確的數字為止。
"""

import random


def guess_number_game():
    start = 0
    end = 100
    guess_count = 0
    ans = random.randint(start, end)
    print(ans)

    while True:
        user_input = input(f"請輸入一個 {start} ~ {end}的數字: ")

        try:
            user_input = int(user_input)
        except ValueError:
            print("請輸入一個整數")
            continue
        if not (start <= user_input <= end):
            print(f"請輸入介於 {start} 與 {end} 之間的數字")
            continue
        guess_count += 1
        if user_input == ans:
            print(f"恭喜答對,共猜了{guess_count}次")
            break
        if user_input < ans:
            start = user_input + 1
        if user_input > ans:
            end = user_input - 1


guess_number_game()

```
## 解法二
```python=
import random


class GuessNumberGame:
    def __init__(self):
        self.start = 1
        self.end = 100
        self.guess_count = 0
        self.ans = random.randint(self.start, self.end)

    def user_input(self):
        return int(input(f"請輸入 {self.start} ~ {self.end} 的數字: "))

    def play_game(self):
        print(f"目前的答案為: {self.ans}")
        while True:
            user_input = self.user_input()
            if user_input == self.ans:
                print(f"恭喜答對,共猜了{self.guess_count}")
                break
            self.guess_count += 1

            if user_input < self.ans:
                self.start = user_input + 1
            if user_input > self.ans:
                self.end = user_input - 1


game = GuessNumberGame()
game.play_game()
```
# 錯誤處理
錯誤處理是用來處理程式在執行過程中可能出現的錯誤或異常情況的一種方法。透過錯誤處理，我們可以防止程式因錯誤而中斷，並提供更穩定的用戶體驗。

在 Python 中，try 和 except 語句用來實現錯誤處理。這些語句讓你能夠捕獲並處理異常，從而確保程式在遇到錯誤時能繼續運行，而不會停止。

```python=
try:
    n = 100 / int(input())
except ValueError:
    print("請輸入數字")
except ZeroDivisionError:
    print("請勿除以0")
except Exception as e:
    print("發生未知的錯誤", e, type(e))
print("OK")
```

```python=
try:
    # 嘗試執行可能引發異常的程式碼
    result = 10 / 0  # 這個操作會引發 ZeroDivisionError
except ZeroDivisionError:
    # 在捕獲到指定類型的異常時執行這裡的程式碼
    print("發生了除以零的錯誤")
```

在這個範例中，我們使用 try 塊來包裹可能引發異常的程式碼。如果 try 塊中的程式碼引發了指定的異常（例如這裡的 ZeroDivisionError），程式會跳轉到對應的 except 塊來處理該異常。

你可以使用多個 except 塊來處理不同類型的異常，此外，還可以使用 else 塊來處理在沒有異常發生時執行的程式碼，並利用 finally 塊來執行無論是否發生異常都需要執行的清理操作。

```python=
try:
    result = 10 / 0
except ZeroDivisionError:
    print("發生了除以零的錯誤")
except ArithmeticError:
    print("發生了算術錯誤")
else:
    print("沒有發生異常")
finally:
    print("無論是否有異常，都執行此處的程式碼")
```   
通過適當的錯誤處理，你可以更好地控制程式的執行，並在發生異常時提供有用的訊息，從而提高程式的可靠性。

```python=
try:
    n = 100 / int(input())
except ValueError:
    print("請輸入數字")
except ZeroDivisionError:
    print("請勿除以0")
# else:
#     print(n)
# finally:
#     # 無論是否發生例外都會執行
#     print("這是finally區塊")
print("OK")
```

# 類別與物件

## 類別與物件


完整的應用程式通常由許多類別組成。Python是一種物件導向的程式語言，可以使用類別來定義物件的結構和行為。

在 Python 中，使用 class 關鍵字來定義一個類別。類別是一個藍圖或模板，用來創建物件（也稱為實例）。根據這些類別，可以建立不同的物件，並且每個物件都可以擁有獨立的屬性和方法。
類別的命名：按照 Python 的命名慣例，類別名稱的第一個字母通常會使用大寫字母（這是一種稱為「駝峰式命名法」的命名規範），例如:MyClass 或 Car。
```python= 
class 類別名稱(): 定義類別
    定義屬性
    定義方法
    建立物件
    
# 以類別名稱即可建立物件(object)
物件 = 類別()    
# 然後以物件執行其屬性和方法

物件.屬性
物件.方法()
    
```


類別中通常會建立屬性和方法,提供物件使用,類別中的屬性
其實就是一般的變數,方法則是指函式,但在類別中不會以變數
和函式稱呼,而是稱為屬性與方法,我這邊舉個例子

```python=
class Animal:
    name = "小鳥"

    def sing(self):
        print("很愛唱歌")


bird = Animal()
bird.name
bird.sing()

```
執行結果:
![image](https://hackmd.io/_uploads/BkpDnYDvkg.png)


## 類別的建構式

建立類別時,必須對類別初始化,因此必須建立一個特殊的方法, __init__,這個初始化的方法稱為建構式
建立建構式的語法:

```python=
class 類別():
    def __init__(self[參數1, 參數2....]):

```
建構式必須使用__init__()函式,參數self是必須的,同時要放在最前面
其餘的參數式可選擇性的,如此在類別中就可以用self.屬性,self.方法執行類別的屬性與方法

```python=
class Animal:
    def __init__(self, name):
        self.name = name

    def sing(self):
        print(f"{self.name}, 很愛唱歌")


bird = Animal("鴿子")
print(bird.name)
bird.sing()


# def __init__(self):
#     pass  # 預設的建構式，什麼都不做
```

![image](https://hackmd.io/_uploads/B1b0hTwP1g.png)

結論:每個物件有自己的初始化屬性（如物件的名字）。
不使用 __init__ 時，屬性是固定的，所有物件共享同一屬性值。

## 多重繼承
子類別也可以繼承多個父類別,語法如下:
class 子類別名稱(父類別1, 父類別2, 父類別n):
如果父類別擁有相同名稱的屬性或方法時,就要注意搜尋的順序 是從子類別開始,接著是同一階層父類別由左至右搜尋


```python=
class Father:
    def say(self):
        print("yes")

class Mother:
    def say(self):
        print("no")

class Child(Father, Mother):
    pass

child = Child()
child.say()
```



## 計算面積
定義 Rectangle,Triangle,兩個類別,父類別Rectangle
定義共同屬性width,height,和area()方法計算矩形面積
Triangle子類別繼承Rectangle類別並增加一個計算三角形
面積的方法area2()

![image](https://hackmd.io/_uploads/SJeO2RHvyg.png)


<details> 
<summary>程式碼: class_area.py (點此展開)</summary>
    
```python=
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Rectangle):
    def area2(self):
        return (self.width * self.height) / 2


triangle = Triangle(10, 5)
print(f"三角形的面積為: {triangle.area2()}")
print(f"矩形的面積為: {triangle.area()}")

```
</details> 
    
說明:
當創建 triangle = Triangle(10, 5) 物件時，
Triangle 類別會初始化 weight 和 height 屬性，
並且可以使用來自父類別 Rectangle 的 area() 方法來計算矩形的面積。triangle.area2() 計算的是三角形的面積，
使用的是子類別 Triangle 的 area2() 方法。
## class複習
```python=
class Student:
    def __init__(self, name, age, sch, dept, add):
        self.name = name
        self.age = age
        self.sch = sch
        self.dept = dept
        self.add = add

    def say_hello(self):
        print("Hello")


std = Student("xxx", 30, "sc", "py", "tpe")
print(std.name)
std.say_hello()

# xxx
# Hello
```

各位注意,明明有五個參數,但我只給四個,結果沒有報錯
原因是右下角type checking沒有選擇standard
![image](https://hackmd.io/_uploads/HJg1cjjuJx.png)

# 建立自己的模組
一個較大型專案,程式是由許多類別與函式組成,為了程式分工與維護
可以適度的將程式分割成許多模組
再匯入並呼叫這些模組

## 準備工作
下列程式包含計算兩數相加,兩數相減的兩個函式,可以直接呼叫add,sub函式來執行兩數相加,相減的運算,檔名:**module_1.py**
```python=
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


print(add(7, 3))
print(sub(7, 3))
```
有時為了程式的分工和維護,我們會將程式分割成模組
那我再建立一個獨立模組名: <b>calculate.py</b> 

```python=
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2

```

## import模組名稱

那完成模組之後我要匯入自己的模組

```python=
import 模組名稱
```
例如: 匯入calculate模組
```python=
import calculate
```
這種方式呼叫函式時,必須加上模組名稱,語法:
```python=
calculate.函式名稱
```
**module_2.py**
```python= 
import calculate

print(calculate.add(7, 3)) # 10
print(calculate.sub(7, 3)) # 4
```
<b>功能分離：</b>
你可以將不同的程式邏輯分開，讓每個檔案專注於做某一個工作。
<b>重複利用：</b>
如果在其他地方也需要進行加減法運算，只需要導入 calculate.py，
就可以直接使用裡面的 add 和 sub 函式，而不用每次都重寫相同的程式碼。

## 匯入模組內函式
每次使用模組內的函式都要輸入模組名稱非常麻煩,下面import的方式可以改善情況,語法
```python=
from 模組 import 函式名稱1[,函式名稱2.......]
```
這種方式呼叫函式,可以省略模組名稱,直接以函式名稱呼叫
**檔名:module_3.py**
```python=
from calculate import add, sub

print(add(7, 3)) # 10
print(sub(7, 3)) # 4

```
各位我換一個例子,建立**module_4.py**
我故意不import sub,來看一下會有什麼樣的結果

```python=
from calculate import add

print(add(7, 3))
print(sub(7, 3))
```
它會出現,name 'sub' is not defined. 
這是因為只有被列出的函式會被導入，其他函式就無法使用。

## 匯入模組內所有函式
建立**module_5.py**
```python=
from calculate import *

print(add(7, 3))
print(sub(7, 3))
```
* 表示全部的意思,這個方法比較方便
但這樣做比較不好,原因是因為每一個模組
都有眾多函式,如果我有兩個模組都導入add函式
那後面導入的add,就會覆蓋前面的

這什麼意思呢?我解釋一下喔!
例如我去新增一個**calculate1.py**
故意去修改add的函式
```python=
def add(n1, n2):
    return n1 + n2 * 2


def sub(n1, n2):
    return n1 - n2
```
再回到**module_5.py**

```python=
from calculate import *
from calculate1 import *

print(add(7, 3))
# 13
```
會得到13,這不是我們要的結果
可以看到後面導入的add函式,就會覆蓋前面的函式

## 使用as指定函式別名
如果不同模組中的函式名稱相同,或是函式名稱太長
我們可以自行指定別名

語法如下:
```python=
from 模組名稱 import 函式名稱 as 函式別名
```
建立 **module_6.py**
這個時候,我們就可以函式別名呼叫
```python=
from calculate import add as a
from calculate1 import add as a1

print(a(7, 3)) # 10
print(a1(7, 3)) # 13
```

## 使用as指定模組別名
這裡建立好**module_7.py**
那各位可能會認為說,不是函式名稱太長
而是模組名稱calculate太長,我們可以這樣做
```python=
import 模組名稱 as 別名
```
如此一來,使用函式時使用[別名.函式名稱],就可以避免較長模組名稱

```python=
import calculate as cal

print(cal.add(7, 3))
print(cal.sub(7, 3))
```
# numpy


## 建立一維陣列

```python=
import numpy as np

np1 = np.array([1, 2, 3, 4])
np2 = np.array([5, 6, 7, 8])
print(np1)
print(np2)
print(type(np1), type(np2))
```

## numpy統計函數
|   函數  |運算|  函數  |運算|
|--------|--------|--------|--------|
| sum |總和  | prod |乘積 |
| mean  |平均值  | std  |標準差 |
| max   |最大值  | var  |變異數 |
| min |最小值  | cumsum |陣列元素累加  |
| median   |中位數 | cumprod   |陣列元素累乘  |

影片名稱:numpy統計函數
```python=
import numpy as np

seed = 0

np1 = np.random.RandomState(seed).randint(1, 51, 12).reshape(3, 4)
print(np1)

```

## numpy 數組

```python=
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
```
創建一個數組,最直接的方法就是透過
numpy的array方法把列表轉為數組
最簡單判斷的方式,是看有幾個方括號,就可以判斷有幾維數組

```python=
arr1.ndim # 1
```
而shape會返回一個元組,表示各個元素的個數

```python=
arr1.shape #(3,) 表示一個維度有三個元素
```
我們要去看他的類型,可以用dtype,它是int32(int64)


```python=
arr1.dtype # int開頭說明類型是整數
# Out[26]: dtype('int32')
```

在numpy裡面,也有方法稱為arange
表示針對array的range方法
```python=
np.arange(起點,終點,間隔)
np.arange(1,10,2)
# Out[25]: array([1, 3, 5, 7, 9])
```


# Django
**學Django對嗎?**
除了Django,python有名的框架有Flask,FastApi
優點:有大量資源可以使用
缺點:執行速度很慢
Django使用在很多網站上,基本上沒有問題


**前言:Django的書更新比較慢,坊間在賣的書很少V5.0以上,外面賣中文版的書都是v3.0或v4.0,甚至線上課程也很少在教Django,但基本上不會有太大改變Django如果要學好,還是要看書**

**建言:每個人python學習程度不同,
建議熟悉class語法,尤其是函式,後面會比較好銜接**

框架的概念,只需要填入中間的商業邏輯就可以形成網頁
好處是:用這個框架可以寫出風格類似的網頁

觀念:框架是個限制?
當公司人一多的時候,使用框架的優點是大於缺點




## 設定Django環境
**安裝好python之後
建議用vscode來做,設定Django環境
記得profile,建立環境**
![image](https://hackmd.io/_uploads/SJ2msOidyx.png)
建立好之後,會看到profile變成DJ
![image](https://hackmd.io/_uploads/SJL85souJl.png)
這樣的目的是為了得到相同的開發環境
安裝vscode 擴充套件

**1.python
2.會自動附加pylance
3.isort 目的:import 會按照字母來排序
![image](https://hackmd.io/_uploads/SyCJkcjukl.png)
4.black formatter 排版工具
5.Even Better TOML
6.Django
7.djlint**


VsCode中設定自動排版,可以參考我的json格式設定
就可以存檔後排版

```json=
{
    "workbench.colorTheme": "Default Light Modern",
    "editor.fontSize": 18,
    "window.zoomLevel": 1,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
}
    }
}
```

"[python]": 
在使用者開啟python這個語言 
"editor.defaultFormatter": "ms-python.black-formatter",
預設的排版工具要用blackformatter
"editor.formatOnSave": true,
當使用者按下存檔後自動排版
"editor.codeActionsOnSave": 
當使用者存檔後
"source.organizeImports": true
重新排序import字母的順序
安裝好套件之後,記得要export profile
![image](https://hackmd.io/_uploads/rJYKgcj_1l.png)


## 安裝虛擬環境
很多人可能會直接下pip install Django==5.1.5
pip是套件的管理工具,可以從網路上下載
**這是官方的做法(今天寫這篇文章,為2025/02/02)**
```python=
py -m pip install Django==5.1.5
```
它的版本為5.15,當時我看到的版本是4.2.7
不建議直接這樣做,具體原因如下:
通常在開發過程中,因為公司可能是做Django的網頁
它用的版本不可能會相同,換句話說我要去建立虛擬環境

**虛擬環境建立方法如下**
```python=
python -m venv .venv
```
-m:module
venv:裡面的venv,來建立 .venv的虛擬環境
結果如下:
![image](https://hackmd.io/_uploads/H1KNDpnOyl.png)

<span style="font-size:20px;">建立虛擬環境：`python -m venv .venv`</span>
<span style="font-size:20px;">啟用虛擬環境：`.\.venv\Scripts\activate.bat`</span>
<span style="font-size:20px;">退出虛擬環境：`deactivate`</span>

.:表示當前目錄
\表示windows的分隔符號
Scripts: 在 Windows 系統中，虛擬環境會在 .venv 資料夾下創建一個名為 Scripts 的子資料夾，裡面包含了啟動虛擬環境所需的可執行文件。
activate.bat: 這是啟動虛擬環境的批次檔案（batch file）。在 Windows 中，這個檔案會設置必要的環境變數來啟動虛擬環境，並讓你在命令行中使用安裝在虛擬環境中的套件。

結果如下:
虛擬環境只有一個pip,接著安裝Django
```python=
pip install Django
```
![image](https://hackmd.io/_uploads/Sylx3p3_yx.png)
**可以看到裝起來了**
![image](https://hackmd.io/_uploads/H1TZ2Th_Jx.png)

假設我的資料夾名稱改了,它的虛擬環境內容都會不見
是因為路徑一定要正確,所以不會備份.venv的資料夾
```python=
pip freeze # 列出套件與版本
```
```python=

pip freeze > requirements.txt # 資料夾會出現requirements
```
結果如下:
![image](https://hackmd.io/_uploads/rJlrCa3uJg.png)
**這樣做的好處是:我可以將.venv刪除
那要如何還原呢?**
首先是要建立和啟動虛擬環境,接著輸入以下指令
```python=
pip install -r requirements.txt #
# 這段話的意思,就是我去根據紀錄進行安裝
```

## Django 專案建立
建立專案：`django-admin startproject core .`
**django-admin:是django框架的指令,一定要安裝才會有
,檔案是由 startproject 所建立出來的
core:核心目錄的檔名,.(點)表示當前目錄**

啟動伺服器：`python manage.py runserver`
**manage.py 表示專案的進入點**
打開瀏覽器訪問 http://127.0.0.1:8000

建立專案後產生的檔案
![image](https://hackmd.io/_uploads/r1kxfRnOke.png)
`core:創建的 Django 項目的名稱。在這個例子中，項目會被命名為 core
建立後的第一件事就是檢查manage.py`

![image](https://hackmd.io/_uploads/SkA-gVAO1l.png)

產生runserver,輸入 127.0.0.1:8000
![image](https://hackmd.io/_uploads/HkQ2f0hdye.png)

關於python manage.py後面會再補充,不要去動
請參考以下:
![image](https://hackmd.io/_uploads/SJszSC2dJl.png)

## 安裝Poetry
以前很多人可能會用Anoconda,避免使用Anoconda,因為動則20G
所以盡可能用原生的東西,公司不可能讓你裝那麼多東西
盡可能用venv,才了解過程用什麼?用poetry.....最好


**先前做的事情是虛擬環境+套件管理**
參考網址:https://python-poetry.org/
那poetry就是把虛擬環境和套件管理整理在一起
讓我們比較方便去做這件事
到cmd 輸入 
```python=
pip install pipx
```

**參考網址:
https://python-poetry.org/docs/#installing-with-pipx**
**全域安裝方式**
pipx 是不同於pip的套件,不會影響到全域的環境
接著就是透過pipx去安裝poetry


## Poetry 安裝
https://python-poetry.org/

安裝 pipx：`pip install pipx`
透過 pipx 安裝 poetry：`pipx install poetry`
編輯環境變數讓電腦找得到透過 pipx 安裝的指令：`pipx ensurepath`
確認 poetry 版本（需開啟新的命令提示字元）：`poetry --version`
**如果之後要更新可以輸入pipx upgrade poetry
目前(2025/2)**
![image](https://hackmd.io/_uploads/SJDiUVCOJg.png)
透過 poetry 初始化專案（在專案的資料夾中）：`poetry init`
安裝 django 到 poetry 的虛擬環境中：`poetry add django`
進入 poetry 的虛擬環境：`poetry shell`
退出 poetry 的虛擬環境：`exit`
刪除 poetry 的虛擬環境：`poetry env remove --all`
依照 pyproject.toml 設定安裝套件：`poetry install`

### 實驗,重新建一個資料夾
pipx是可以全域安裝的套件,可以輸入pip list裡面是空的
但透過poetry --version,裡面是有的
這個因為pipx,但不影響全域環境
接著輸入
```python=
poetry init
```
**輸出結果如下:**
![image](https://hackmd.io/_uploads/rJlwdV0_Jl.png)
這個時候,我用vscode開啟資料夾,就會看到pyproject.toml
![image](https://hackmd.io/_uploads/SJfTuN0uyg.png)
顏色會不一樣,這是因為我們有裝even better toml
原本我們的虛擬環境,是透過python -m venv .venv
套件管理是透過pip管理,可是舊的專案,安裝Django,有依賴套件
![image](https://hackmd.io/_uploads/BkpwcNR_ke.png)
到新的資料夾下指令:
```python=
poetry add django
```
![image](https://hackmd.io/_uploads/rJ3RcNC_1x.png)
裝好之後呢?它會幫我建虛擬環境,就可以看到它的依賴是python 3.12版
![image](https://hackmd.io/_uploads/SyYEhN0O1e.png)
可以輸入pip list,沒有看到django,它把預設當作虛擬環境裝
### poetry功用
poetry是套件管理加上虛擬環境管理的一個工具,如果我想安裝django
它會幫我裝,當發現沒有虛擬環境的時候,它會幫我建立
```python!
poetry shell
```
![image](https://hackmd.io/_uploads/BkYlqHROJe.png)

看一下 poetry.lock
![image](https://hackmd.io/_uploads/HJnm8HAu1l.png)
這樣做的好處就是以虛擬環境為主,退出可以使用exit
簡單來說,lock的檔案是自動被建立出來的,不要手動更新
```python!
exit
```

```python!
poetry show --tree
```
會出現這一段的解決方式如下:
![image](https://hackmd.io/_uploads/SkVlaHAdyx.png)

```python=
[tool.poetry] # 要改成tool.poetry
name = "django-project"
version = "0.1.0"
description = ""
authors = ["Test01 <test01@gitlab.local>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
django = ">=5.1.5,<6.0.0"

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

```
![image](https://hackmd.io/_uploads/BkDmoekF1x.png)

(2025/02/03 更新) 後面會盡可能使用poetry

專案架構
假設目錄名稱為dj-project
|   檔案或目錄  |說明| 
|--------|--------|
| 上層dj-project目錄 |本專案的主目錄  | 
| manage.py  |python命令檔,提供專案管理功能,包含建立app,啟動server和shell  |
| 下層dj-project目錄   |包含專案設定,url配置,網頁伺服器介面設定檔  | 
|  ____init.py____  |一個空檔,使得該資料夾成為一個python package  | 
| asgi.py |asgi伺服器和Django的介面設定檔 |
| setting.py  |本專案的設定檔 |
| urls.py  |url配置檔 |
| wsgi.py  |網頁伺服器和Django的介面設定檔 |

`manage.py` :代表專案的進入點
`____init.py____ `這是python的一部份變成package
`core`裡面asgi異步與wsgi同步
`setting.py` 最常會編輯的檔案,官方會更多
`urls.py`:網址斜線的後面就是指路由

## poetry相關複習
資料夾不要中文名稱,如果我希望poetry管理我的套件
使用poetry會大幅縮短時間
```python=
poetry init
```
結果如下:會出現pyproject.toml
![image](https://hackmd.io/_uploads/rJwqwoJY1x.png)
要去檢查版本
```python=
django -admin --version
```
結果如下:
![image](https://hackmd.io/_uploads/B1uknikYkg.png)

Django版本 5.1.5 大版號5,中間最好是2 表示 long time support
盡可能用5.2最好,現在要建立專案,core 後面要加點
在當前的目錄建立core
```python=
django-admin startproject core .
```
結果如下:
![image](https://hackmd.io/_uploads/BkbXRiyF1x.png)

poetry要如何知道依賴套件,都會在poetry.lock

### poetry 1.8以上進入虛擬環境問題

1. 升級poetry
```python=
pipx upgrade poetry
```
2. 檢查版本
```python=
poetry --version
```
![image](https://hackmd.io/_uploads/SkGttx-YJl.png)

3. 那現在要去進入虛擬環境,會失敗
![image](https://hackmd.io/_uploads/BJiiYgbYkg.png)

4. 解決辦法:
```python=
poetry self add poetry-plugin-shell
```
將 poetry-plugin-shell 插件安裝到 Poetry 中

5. 再試一次
```python=
poetry shell
```

結論如下:
![image](https://hackmd.io/_uploads/ryb13lZKye.png)

6. 我們用poetry show
![image](https://hackmd.io/_uploads/ryYEECZKJx.png)

7. 更新Django
```python=
poetry update django
```

8. 啟動 Django 的開發伺服器，並使其能夠在本地端運行
python manage.py runserver
manage.py 會是專案的進入點

結果如下:
![image](https://hackmd.io/_uploads/HJU2BRWKye.png)

[127.0.0.1:8000](http://127.0.0.1:8000)
連到我現在目前電腦的8000 port
或者是輸入 '[localhost:8000]localhost:8000' 
也就是django專案

## 製作第一個django程式
MVC,就是網頁框架基礎的分層,在django稱為MTV
M:model 負責與資料庫做交互,與資料庫做溝通
T:template 負責處理畫面
V:view 負責處理邏輯

現在我要想辦法產生MTV資料夾
在開發的時候,一台會跑runserver,所以會開另外一台終端機cmd
進入虛擬環境
```python=
poetry shell
```

```python=
python manage.py startapp first<名稱>
```
python manage.py startapp是用來創建一個新的應用（app）目錄的命令。
每個 Django 項目可以包含多個應用，每個應用負責不同的功能模組
這樣有助於將代碼進行模組化，便於維護和擴展。和其他管理方式不太相同。


通常作法會將app獨立在外面,打包成package,A與B專案,最後再引用
core/settings.py
![image](https://hackmd.io/_uploads/S1xLdmftJg.png)
執行之後結果如下:
![image](https://hackmd.io/_uploads/r1tc_mzFJl.png)
來看一下first資料夾,裡面有許多檔案
views:處理邏輯
tests:處理自動化測試網頁(這是一個獨門學問)
讓程式穩定度比較高(後面會說明)
apps:是app當前的基本資料
models:存放與資料庫交互
admin:內建功能
那template,必須要自己建,後面會提到,這一小節只會有views會用到
有些書不一定把app install到settings.py
如果app建好,請自行把install都裝上去,後面用model,template
**(強烈推薦)**如果app沒有出現在列表當中,它不會去尋找
要先startapp first之後才能去加入app
結果如下:
![image](https://hackmd.io/_uploads/BkOF5QfYkx.png)
先到 `first/views.py` 寫第一個程式,定義一個view來處理一個邏輯,回傳一個"Hello World"我們要去訪問路由(url)
```python=
def hello_world():
    return "Hello World"
```
上面是錯誤的(因為沒有加參數)
我要想辦法讓別人訪問我的路由執行function
與路由相關的都在urls.py 這時候登錄網址: 127.0.0.1:8000/admin

![image](https://hackmd.io/_uploads/S1ZCsXzFJl.png)
會看到一個登錄的畫面
![image](https://hackmd.io/_uploads/BJaQ27ftJx.png)
等一下的目標是 127.0.0.1:8000/hello-world/
要執行"hello_world"
![image](https://hackmd.io/_uploads/BkzbTQGF1x.png)
會發生錯誤,將一個參數傳遞給views
少一個參數(必須給它request)
路徑:core\urls.py
```python=
from django.contrib import admin
from django.urls import path
from first.views import hello_world

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world/", hello_world),
]
```
上述說明的是兩個參數,第一個放路徑,第二個放function
拿0個參數但1個被傳入了,用path的目的
是告訴django,負責執行hello_world
![image](https://hackmd.io/_uploads/r19fa7MK1x.png)
```python=
def hello_world(request):
    return "Hello World"
```
如果function的定位是views,一定要接受一個參數,request
這個錯誤,AttributeError at /hello-world/
如果看到這個錯誤,views表示回傳的不是http的response
### 為何要傳遞給views?
使用者要求看到一個網站,放在path第二個參數,
一定要接收request,變成'str' object has no attribute 'get',views接收一個request,要回傳response

![image](https://hackmd.io/_uploads/B13JCQfYJl.png)
換句話說,要給它一個http的response,不能是單純的string,正確結果如下:
`first\views.py`
```python=
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello World!!")
```

![image](https://hackmd.io/_uploads/rJfiGLfYkg.png)

上面只是指定url去訪問
現在我們要做跟使用者互動的網站
http://127.0.0.1:8000/say-hello

http 和 https 都是用來在網絡上傳輸資料的協議,https在傳輸的過程中會將內容加密,http會根據內容成功與否給予狀態碼
http status code,有很多種
參考網址如下:
https://zh.wikipedia.org/zh-tw/HTTP%E7%8A%B6%E6%80%81%E7%A0%81
最常見的是200與404,那我們回到
我先讓say-hello到hello_world
`core\urls.py`
```python=
urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world", hello_world),
    path("say-hello", hello_world),
]
```
結果如下:
![image](https://hackmd.io/_uploads/H1mYfVXtkx.png)
但這不是我們要的結果,回到
`first\views.py`
```python=
def say_hello(request):
    return HttpResponse("say hello to XXX")
```

```python=
from first.views import hello_world, say_hello

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world", hello_world),
    path("say-hello", say_hello),
]

```
如果我按照以下這樣做.結果為say hello to none
```python=
def say_hello(request):
    name = request.GET.get("user")
    return HttpResponse(f"say hello to {name}")
```
在 URL 中使用問號（?）是用來分隔 路徑（path） 和 查詢字符串（query string） 的部分。當你在 URL 中看到一個問號後，問號後面的部分就是 查詢字符串，它包含了許多鍵值對（key-value pairs），每一對鍵值對用來傳遞參數。
http://127.0.0.1:8000/say-hello/?name=user02
![image](https://hackmd.io/_uploads/Sy5fNEXtke.png)
現在我要想辦法讓使用者傳入一個參數給views
會使用到http.get參數,另外一種是post
目前都是用get,將東西傳給views
http的request如何傳入?
[127.0.0.1:8000](http://127.0.0.1:8000)
http://127.0.0.1:8000/say-hello/?name=user01
問號以後都是參數
可以正常訪問,但並沒有任何變化
那要如何拿到name這個參數?
使用print
```python=
def say_hello(request):
    print(request.GET)
    return HttpResponse("say hello to XXX")
```
我先print看看,但沒有任何變化,看一下終端機
![image](https://hackmd.io/_uploads/HJf7br7KJg.png)
<QueryDict: {'/name/user01': ['']}>
**這意思是request.get是一個dict結構**
key, value
```python=
def say_hello(request):
    print(request.GET["name"])
    return HttpResponse("say hello to XXX")
```

![image](https://hackmd.io/_uploads/rJSSEHmFJg.png)
現在就是print內容,給它一個變數存放
將XXX替換成name

```python=
def say_hello(request):
    user = request.GET["name"]
    return HttpResponse(f"say hello to {user}")
```
![image](https://hackmd.io/_uploads/H1q04BQF1g.png)
但假設不傳入,就會報錯,Django 會抛出 MultiValueDictKeyError，因為 request.GET 中沒有 name 這個鍵。request.get是一個dict型態,如果key不存在會引發錯誤
![image](https://hackmd.io/_uploads/r14HjrmYke.png)
request.GET是個dictionary,使用者傳入的所有參數,後面的.get是python中的語法
```python=
def say_hello(request):
    user = request.GET.get("name")
    return HttpResponse(f"say hello to {user}")
```
下面的意思是如果我傳入了name,會顯示,但如果不是呢?
會出現像這樣的結果

![image](https://hackmd.io/_uploads/BkoZCCLKkg.png)

```python=
def say_hello(request):
    name = request.GET.get("name", "unknown")
    print(name)
    return HttpResponse(f"say hello to {name}")
```

![image](https://hackmd.io/_uploads/BJGLn0IKJl.png)


![image](https://hackmd.io/_uploads/rynh9c7tJx.png)
`views.py`
```python=
def say_hello(request):
    name = request.GET.get("name", "unknown")
    repeat = request.GET.get("repeat", 1)
    return HttpResponse(f"say hello to: {name}" * int(repeat))
```
可以看到重複三次,因為repeat=3,我這邊拆分給各位看
```python=
def say_hello(request):
    name = request.GET.get("name", "unknown")
    print(request.GET.get("repeat"))
    print(name)
    return HttpResponse(f"say hello to {name}")
```
![image](https://hackmd.io/_uploads/Synt1JvKke.png)
那現在我要重複5次,就要給它變數存放


### 不一樣的參數傳遞
剛才都是以get的方式傳入參數,例如說:
`name = request.GET.get("name", "unknown")`
意思就是我沒有傳入name,就要給它預設值
所以現在就是要將參數加入到路徑裡面,讓參數變成路徑的一部分

first\views.py
```python=

def repeat(request):
    return HttpResponse("repeat")
```
core\urls.py

```python=
from first.views import repeat
path("repeat/<str:content>/", repeat),
```
repeat後面要跟上一段文字,這個錯誤的原因
django傳入的參數會傳入repeat views裡面
![image](https://hackmd.io/_uploads/BJaUzaNtyg.png)
```python=
def repeat(request, content):
    return HttpResponse(content)
```   
各位懂我意思嗎?
http://127.0.0.1:8000/repeat/OOOO/
![image](https://hackmd.io/_uploads/HkfKXaVY1g.png)
那repeat不能只有給content,要給它次數

path("repeat/<str:content>/<times>", repeat)
    ![image](https://hackmd.io/_uploads/SyT9Vp4Ykl.png)
http://127.0.0.1:8000/repeat/OOOO/1/
這樣就進到views裡面,但引發錯誤
http://127.0.0.1:8000/repeat/OOOO/ppp/   
![image](https://hackmd.io/_uploads/H1rWHTNtJx.png)
上面的錯誤代表沒有匹配到任何路徑
    
 ![image](https://hackmd.io/_uploads/HyYb-uwKJg.png)
參數必須是int  
    
```python=    
def repeat(request, content, times):
    return HttpResponse(content * times)
```  
![image](https://hackmd.io/_uploads/rJliSpEK1l.png)

    
這一階段完整的程式碼:
`views.py`
```python=
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello World!!")


def say_hello(request):
    name = request.GET.get("name", "unknown")  # 默認為 "unknown" 當未提供 name
    repeat = request.GET.get("repeat", 1)  # 默認為 1 次
    return HttpResponse(f"say hello to {name}" * int(repeat))  # 重複問候語


def repeat(request, content, times):
    return HttpResponse(content * int(times))

```  
    
`urls.py`
```python=
    
from django.contrib import admin
from django.urls import path

from first.views import hello_world, repeat, say_hello

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world/", hello_world),
    path("say-hello/", say_hello),  # 已經加s上結尾的 '/'
    path("repeat/<str:content>/<times>/", repeat),  # 已經加上結尾的 '/'
]

```
    
### template架構
html與Django,是兩個不同的程式語言
它不一定要同時存在django,我先舉個html例子
```html=
<h1>Hello World</h1>
<ol>
    <li>A</li>
    <li>B</li>
    <li>C</li>
    <li>D</li>
</ol>
```
可以看到有起始標籤與結束標籤,先開始的後結束
關於html,是門獨立的課程,短期間不太會跟各位介紹
那回到Django,將前後加上h1標籤,tag只是給瀏覽器看
    
first/views.py  
    
![image](https://hackmd.io/_uploads/HyuMZrDY1l.png)
   
![image](https://hackmd.io/_uploads/B1DSZHPYyx.png)
    
現在要用template架構,在first底下
建立template資料夾
`first\templates\repeat.html` 
    
```html=
    <h1>hello!!!</h1>
```    
先註解掉,不要讓它回傳http response 
![image](https://hackmd.io/_uploads/B1YzrBvKye.png)
```python=    
from django.shortcuts import render
    
def repeat(request, content, times):
    return render(request, "repeat.html")
```

![image](https://hackmd.io/_uploads/S1ZJvSwF1l.png)

    
### 練習    
Django 的程式是採用urlpattern 網址和函式對照方式
主要有兩個步驟
- 1.設定<urls.py>檔,urlpattern 串列中url網址和函式的對照
- 2.在<views.py>,撰寫函式

首先式url
```python=
path(網址, 函式),
```
#### 觀念
- request 是 Django 視圖函式的第一個參數，代表著用戶發送到服務器的HTTP請求。
- HttpResponse 是 Django 用來回應用戶請求的核心對象。每當 Django 接收到一個 HTTP 請求後
視圖函式必須返回一個 HTTP 回應來將處理結果發送回用戶端。

```python=
urlpatterns = [
path("admin/", admin.site.urls),
path("repeat/<str:content>/<int:times>/", repeat),
]    
```
結果如下:
![image](https://hackmd.io/_uploads/HkrHU5htkg.png)

## 使用render渲染動態模板 (2025/02/14)
http://127.0.0.1:8000/repeat/XXXXX/5/
我們的目標是希望五個大X,重複五次XXXXX
來看一下,要如何修改?urls.py,建立repeat路徑
repeat/斜線後面是字串,內容,次數
內容是字串string,乘上次數所以要給它整數型態integer
```python=
path("repeat/<str:content>/<int:times>/", repeat),
```
接著回到views裡面我們看一下
定義repeat函式,各位我要接收三個參數
第一個請求,第二個內容,第三個次數
```python=
def repeat(request, content, times):
    return HttpResponse(content * times)
```
那要回傳 HttpResponse,我們看一下路徑
完成之後,我們檢查一下
```http=
http://127.0.0.1:8000/repeat/XXXXX/5/
```
就會呈現我們要的結果
![image](https://hackmd.io/_uploads/HyChIqnFke.png)
那現在在這個view裡面,我想要讓它回傳跟html一樣
一個h1標籤要怎麼做?很簡單,我只需要在外圍
建立h1標籤就好,在外面用f字串包圍

`views.py`
    
```python=
    return HttpResponse(f'<h1>{content * times}</h1>')
```
大於小於的tag包圍為主要是給瀏覽器看的
我們回到瀏覽器看一下,有沒有發現,字體變大了
http://127.0.0.1:8000/repeat/XXXXX/5/ 
    
### render渲染
- 建立templates/repeat.html    
![image](https://hackmd.io/_uploads/B1APjohFyg.png)
`repeat.html`
```python=
<h1>hi!!!!</h1>
```
    
`views.py`
```python=
def repeat(request, content, times):
    # return HttpResponse(f"<h1>{content * times}</h1>")
    return render(request, "repeat.html", {"content": content * times})
```
可是repeat內容顯示什麼東西是根據content以及times對吧
那回到render看一下要怎麼做呢?
第一個request,第二個html檔名,第三個給它一個dict
return render(request, "repeat.html", {"message":content *times})
給repeat.html一個資料,例如:message: content *times
完成之後呢?我們回到html,就可以使用message這個變數
`repeat.html`
```python=
<h1>{{message}}</h1>
```
類似像這樣,回到瀏覽器,會得到一樣的效果,我們在view這邊留下商業邏輯,但內容是html所決定的   

http://127.0.0.1:8000/repeat/OOOOOOO/2/ 
    
    
### templates底下建資料夾
建資料夾有什麼好處?
因為在Django的資料結構裡面,template會在每個app裡面
我無法保證其它app裡面剛好有repeat.html,說穿了
就是為了方便管理,減少衝突,
`\first(app名稱)\templates\first\repeat.html`
```html=
    <h1>{{message}}</h1>
```

`views.py`
```python=
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def hello3(request, username):
    now = datetime.now()
    return render(request, "hello3.html", {"username": username, "now": now})
    
def repeat(request, content, times):
    # return HttpResponse(f"<h1>{content * times}</h1>")
    return render(request, "first/repeat.html", {"message": content * times})


```

`hello3.html`
```html=
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django</title>
</head>
<body>
    <h1>Hi ,{{username}} </h1>
    <h2>現在時間: {{now}} </h2>
    
</body>
</html>
```

    
`urls.py`
    
```python= 
    path("repeat/<str:content>/<int:times>/", repeat),
```
    
### template和views,url綜合練習


`urls.py`
```python=
    path("list-item/<str:item>/<int:times>/", list_item),
```
    
`views.py`
    
```python=
def list_item(request, item, times):
    return render(
        request,
        "first/list_item.html",
        {"item": item, "times": times},
    )
```

`dj-project\first\templates\first\list_item.html`  

```html= 
<h1>{{item}} * {{times}}</h1>  
```   
http://127.0.0.1:8000/list-item/hello/5
如果這樣做會呈現以下結果,不會變成幾次
![image](https://hackmd.io/_uploads/Sy3s4Oe5ye.png)
    
```html= 
<h1>{{item}} * {{times}}</h1>

<ol>
    {% for i in range%}
    <li>{{item}}</li>
    {% endfor %} 
</ol>
    
```   
結果如下:
![image](https://hackmd.io/_uploads/rJfh2de5yx.png)

# Django-ubantu環境   
## 在 Ubuntu 虛擬機中使用 Poetry 管理 Django 專案
先前沒有跟各位提到如何安裝
這一小節我用ubantu示範安裝

## 套件安裝部分

- 0.確認發行版
```bash=
lsb_release -a
```
    
- 1. 用curl安裝poetry
```bash=  
sudo curl -sSL https://install.python-poetry.org | python3 -  
```

- 2. 找到正確位置
```bash=   
ls ~/.local/bin/poetry
```

- 3. 設定環境變數
```bash=
sudo vim ~/.bashrc
```
    
- 4. 添加到結尾,:wq存檔離開
```bash=
export PATH="$HOME/.local/bin:$PATH"
```

- 5. 重新載入配置文件
```bash=
source ~/.bashrc 
```
- 6. 檢查版本
```bash=
poetry --version
``` 
結果如下:
![image](https://hackmd.io/_uploads/S17Kh4Qc1x.png)

- 7. 更新版本
```bash=    
poetry self update
```
- 8.先建立一個資料夾    
```bash=    
poetry new dj-project
```  
- 9.切換資料夾   
```bash=    
poetry new dj-project
```  
- 10.初始化 poetry環境
```bash=
poetry init
```
- 11. 添加django或修改pyproject.tmol  
```bash=
poetry add django
```
到dependencies = [
"django"] 取新增

- 12.新增完成之後,我要安裝
```bash=
poetry install
```

- 13. 安裝完成之後,進入虛擬環境
```bash=
poetry shell
```
- 14. 這時候查看版本
```bash=
django-admin --version
```
- 移除的指令
```bash=
poetry remove django
```

15. 建立專案
```bash=
django-admin startproject core .
```
```bash=
python manage.py runserver
```
16. 解決應用未遷移的問題
```bash=
python manage.py migrate
```

17. 到settings.py 去新增host
    
python manage.py runserver 0.0.0.0:8000

```bash=   
ALLOWED_HOSTS = ['10.11.12.100', '127.0.0.1', 'localhost']
```

結果如下: 
![image](https://hackmd.io/_uploads/Bkw8IrX5Je.png)


## Django的MTV架構
|   任務  |MVC架構|  MTV架構  |
|--------|--------|--------|
| 資料庫存取 |M=Model 模型 | M=Model 模型 |
| 輸入表單或顯示資料 |V=View 視圖  | T=Template 模板 |
| 控制與整合 |C=Controller控制 | V=View 視圖 |

Django架構是採用model,template,view
分開來的架構,稱為MTV架構
Template：處理 HTML 顯示，顯示從 View 傳遞過來的資料。
View：控制邏輯，負責從 Model 獲取資料並將其傳遞給 Template。
Model：處理資料庫存取和商業邏輯。

![image](https://hackmd.io/_uploads/HySrlcE9yl.png)

舉例來說，假設你正在開發一個網路商店，那麼你的商業邏輯可能包括：

訂單處理邏輯：當顧客下單時，應該檢查庫存、計算總金額、應用折扣、計算運費，並將訂單儲存到資料庫。
用戶驗證邏輯：當用戶登入時，系統需要檢查提供的帳號密碼是否正確，並根據用戶的權限決定能夠訪問的資料和功能。
支付處理邏輯：在顧客支付時，可能需要進行支付金額計算、支付方式選擇、交易的確認和通知。
- 建立專案
    
```bash=
python manage.py startapp first(名稱自訂)
```
    
/home/user/dj-project/first/views.py   
```bash=
from django.http import HttpResponse
from django.urls import path


def hello(request):
    return HttpResponse("hello")
```
    
/home/user/dj-project/core/urls.py
```bash=
from django.contrib import admin
from django.urls import path

from first.views import hello

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
]

```
    
![image](https://hackmd.io/_uploads/r1gmZCNqJg.png)

### 
urls.py

```python=    
from first.views import hello5 ,dice
    path("hello5/<str:content>/<int:times>", hello5),
```

views.py
    
```python=
from django.shortcuts import render
def hello5(request, content, times):
    message = content * times
    return render(request, "first/hello5.html", {"message": message})
    
def dice(request):
    point = random.randint(1, 6)
    return render(request, "first/dice.html", {"no": point})

```
first/hello5.html   
```python=
<h1>{{message}}</h1>
```
first/dice.html 
```python=
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>骰子</title>
</head>

<body>
  <h1>點數: {{no}} </h1>
</body>

</html>
```
結果如下:
![image](https://hackmd.io/_uploads/Hy0u5k891e.png)

http://10.11.12.100:8000/hello5/   
![image](https://hackmd.io/_uploads/Bk6TleL5ke.png)
##  settings.json設定
```json=
{
    "workbench.colorTheme": "Default Light Modern",
    "editor.fontSize": 18,
    "window.zoomLevel": 1,

    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    },

    "python.defaultInterpreterPath": "/home/user/.cache/pypoetry/virtualenvs/dj-project-WCi96M66-py3.12/bin/python",

    "[django-html]": {
        "editor.quickSuggestions": {
            "other": true,
            "comments": true,
            "strings": true,
            "html": true
        },
        "editor.snippetSuggestions": "inline",
        "djlint.enableLinting": true,
        "djlint.profile": "django"
    },

    "html.format.enable": true,
    "html.format.wrapLineLength": 120,
    "html.format.indentSize": 4,
    "html.autoClosingTags": true,
    "html.autoSelfClosingTags": true,
    "editor.formatOnSave": true,
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.defaultFormatter": "vscode.html-language-features",

    "emmet.includeLanguages": {
        "django-html": "html"
    }
}
```
    
## for與if判斷式應用
    

- views.py
```html=

def list_item(request, item, times):
    return render(
        request,
        "first/list_item.html",
        {"item": item, "times": times, "range": range(times)},
    )
```

- urls.py
```python=
path("list-item/<str:item>/<int:times>/", list_item),
```
first/list_item.html
```html=
<h1>{{item}} ** {{times}}</h1>

<o1>
    {% for i in range %}
    <li>{{item}}</li>
    {% endfor %}
</o1>
    
{% if show %}
<p>hello world</p>
{% else %}
<p>fail</p>
{% endif %}
```
http://10.11.12.100:8000/list-item/XXX/5/?show=0
以上"沒有"出現hello world    
http://10.11.12.100:8000/list-item/XXX/5/?show=true
以上"有"出現hello world 

在Django中,兩個大括號,表示輸出某一個值  
那各位可能會想說,我們在python中不是也有用else
{% else %} 大括號加上百分比的情況下,{% 通常是指指令   
    
製作結果
![image](https://hackmd.io/_uploads/B1psUtO5kx.png)

![image](https://hackmd.io/_uploads/BknQhY_qJx.png)

討論:
    
```python=
print(request.GET)
```
http://127.0.0.1:8000/list-item/YYY/5/?show=0
`<QueryDict: {'show': ['0']}>
[24/Feb/2025 11:03:23] "GET /list-item/YYY/5/?show=0 HTTP/1.1" 200 137`
request.GET是 Django 中的一個字典（QueryDict），它包含了 HTTP GET 請求中 URL 查詢字符串的所有參數。
結論就是會得到一組key, value
    
request.GET.get(key, default=None) 會返回給定 key 對應的查詢參數值。如果該查詢參數不存在，則返回 default 參數提供的值（如果有指定的話），否則返回 None。

## 設定排版

### 安裝djlint
    
```python=
poetry add --group dev djlint
```
### 安裝black isort
    
```python=
poetry add --group dev black isort
```
- 移除指令
`poetry remove --group dev black isort`  
dj-project\pyproject.toml  
```python=
[tool.poetry]
name = "dj-project"
version = "0.1.0"
description = ""
authors = ["naxchang <naxchang@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
django = "^5.1.5"


[tool.poetry.group.dev.dependencies]
djlint = "^1.36.4"
black = "^25.1.0"
isort = "^6.0.0"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.djlint]
profile = "django"
preserve_blank_lines = true
```
參考網址:
https://www.djlint.com/docs/configuration/
    
## VScode 設定存檔排版
```json=    
{
    "workbench.colorTheme": "Default Light Modern",
    "editor.fontSize": 17,
    "window.zoomLevel": 1,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    "[django-html]": {
        "editor.formatOnSave": true
    }
} 
```
- 排版參考2   
```
    {
    "workbench.colorTheme": "Default Light Modern",
    "editor.fontSize": 18,
    "window.zoomLevel": 1,

    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    },

    "python.defaultInterpreterPath": "/home/user/.cache/pypoetry/virtualenvs/dj-project-WCi96M66-py3.12/bin/python",

    "[django-html]": {
        "editor.quickSuggestions": {
            "other": true,
            "comments": true,
            "strings": true,
            "html": true
        },
        "editor.snippetSuggestions": "inline",
        "djlint.enableLinting": true,
        "djlint.profile": "django",
        "editor.defaultFormatter": "monosans.djlint"
    },

    "html.format.enable": true,
    "html.format.wrapLineLength": 120,
    "html.format.indentSize": 4,
    "html.autoClosingTags": true,
    "html.autoSelfClosingTags": true,
    "editor.formatOnSave": true,
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.defaultFormatter": "vscode.html-language-features",

    "emmet.includeLanguages": {
        "django-html": "html"
    }
}


```
    
## 設定form表單-GET
接下來我們要更深入了解django-template的互動方式
回頭來看一下,我們的show等於true這件事情,都是由問號來控制的對吧!我們不可能讓使用者來改這個東西!
    
所以我們要用個方式可以讓前端網頁與使用者互動
會使用到一個工具叫做form,那form這個工具要怎麼用?
我們先到template底下建立say_hello.html
http://127.0.0.1:8000/list-item/YYY/5/?show=true  
`urls.py`
```python=
import say_hello
 path("say-hello/", say_hello),
```
  
`first/say_hello.html`
```python=
{% for i in range %}<p>say hello to {{ name }}</p>{% endfor %}

<form action="" method="get">
    <p>
        <input type="text" placeholder="name" name="name">
    </p>
    <p>
        <input type="number" placeholder="repeat" name="repeat">
    </p>
    <p>
        <button type="submit">Send</button>
    </p>

</form>


```
在表單提交時，表單的數據會以 name=value 的形式發送
其中 name 是這個 input 元素的名稱
而 value 是用戶在該字段中輸入的內容

views.py  
```python=   
def say_hello(request):
    name = request.GET.get("name")
    if not name:
        name = "unknown"
    try:
        repeat = int(request.GET.get("repeat", 1))
    except Exception:
        repeat = 1
    return render(
        request, "first/say_hello.html", {"name": name, "range": range(repeat)}
    )

```   
http://127.0.0.1:8000/say-hello/?name=test1&repeat=5
結果如下:
    
![image](https://hackmd.io/_uploads/rklSZmh9Jg.png)

表單送出後,會得到結果
    
    
## 設定form表單-POST
    
GET 用於讀取資料並顯示，適合不涉及機密資訊的情況；而 POST 用於提交資料，適合用於處理表單提交、登錄等需要隱藏數據的情境。
所以這一小節,我們來練習post

`views.py`
    
```python=
def say_hi(request):
    return render(
        request,
        "first/say_hi.html",
        {
            "name": request.POST.get("name", "unknown,"),
        },
    )
```
http://127.0.0.1:8000/say-hi/ (windows)
http://10.11.12.100:8000/say-hi/ (Linux)
    
接著我要想辦法拿到get參數
前面我們是用request.GET
現在我們來看一下,如果要拿post要怎麼拿?
那就是print(request.POST),回到瀏覽器重新整理
像這樣的方式,都是get請求,並沒有辦法送出post請求
所以我們要用form來協助我們送出post請求
我們去templates,去新增一個html
<form action="" method="post"></form>
我新增了一個form,action是同一個路徑
method,從先前的get改為post.我將一些欄位複製過來喔!

`first\say_hi.html`
```python=
<form action="" method="post">
    {% csrf_token %}
    <p>
        <input type="text" placeholder="name" name="name">
    </p>
    <button type="submit">Send</button>
</form>

```

urls.py
```python=
from first.views import say_hi   
    path("say-hi/", say_hi),
```
 
 結果如下:
    
![image](https://hackmd.io/_uploads/HJnW3Un91g.png)
我們按下重新整理的時候,各位會看到重新傳送這個視窗
確認重新提交表單,為什麼會這樣我解釋一下
當你按下重新整理的時候,瀏覽器會自動幫你重送最後一次請求
最一開始有說過,用post傳送的東西,大部份都是機敏資訊
    

    
在first外圍建立一個檔案   
`dj-project\templates\base.html`
    
![image](https://hackmd.io/_uploads/rkOjMYpckl.png)
    
這目的是希望跨app的template
那各位可能會有疑惑阿~我要放在外圍的template
還是要放在app裡面的template呢?
我們裡面的template是給first裡面用的
我就會放在first這個app裡面
那外圍的template會放跨app所使用的
例如我在裡面新增base.html

`dj-project\first\templates\first\say_hi.html`
```html=  
{% extends "base.html" %}
{% block body %}

    <h1>Hello {{ name }}</h1>
    <form action="" method="post">
        {% csrf_token %}
        <p>
            <input type="text" placeholder="name" name="name">
        </p>
        <button type="submit">Send</button>
    </form>

{% endblock %}
```
    
    

    
dj-project\templates\base.html
```html=  
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Django</title>
    </head>
    <body>
        {% block body %}{% endblock %}
    </body>
</html>
```
我再右鍵檢查一下網頁原始碼,是不是有完整的出現
網頁的內容,並且將我們指定好的東西填到body裡面
那我要怎麼確定它是不是吃到base.html,而不是其它東西
來做個實驗,回到base.html,我將title改為Django
表示確實有新增html這邊我重新說明一下,
template所在的資料夾不再原本的預設的template裡面
所以我們要額外指派它的路徑,各位懂我意思吧!
dj-project\core\settings.py
    
```python=   
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],   
```
    
![image](https://hackmd.io/_uploads/B1owiiT5kg.png)
    
### (複習)在django建立一個form表單
    
![image](https://hackmd.io/_uploads/HJ_ITLeikl.png)
http://10.11.12.100:8000/hi-news/
urls.py
```python=
import  hi_news
path("hi-news/", hi_news),
```
    
views.py    
```python=
def hi_news(request):
    return render(request, "first/hi_news.html")
```

```html=
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <form action="">
            <label for="news">選擇要觀賞的節目</label>
            <select name="" id="news">
                <optgroup label="國內新聞頻道">
                    <option value="">晚間頻道</option>
                    <option value="">即時新聞</option>
                </optgroup>
                <optgroup label="國外新聞頻道">
                    <option value="">CNN</option>
                    <option value="">NHK</option>
                </optgroup>
            </select>
        </form>
    </body>
</html>
```
    
## 模板繼承與區塊管理技巧
我們要一個完整的html,需要一個!加一個tab鍵
如果我每一個都要去新增,但我們如果要去改個title
不就要一個一個去改了?所以在寫網頁時
我們會在最外層的專案中建立一個template
裡面放一個base,我們會在base裡面建立一個空間
然後讓其它的template來去繼承base.html,
填入block的區塊
    
- dj-project\templates\base.html   
```python=
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Django</title>
    </head>
    <body>
        {% block body %}{% endblock %}
    </body>
</html>
``` 
所以這一小節我們來複習一下,到repeat.html
如果我在這個template要去繼承base.html
我需要輸入extends
{% extends "base.html" %}
那下面是不是要顯示在base.html的body當中
我已經建立一個block叫做body
我可以在這裡寫上block,選擇unname
這個時候我可以將h1放到body裡面
輸入以下程式碼,存檔後會幫我排版
    
這個時候我右鍵檢查網頁原始碼,可以看到外面都是base
裡面都是block   
- http://10.11.12.100:8000/repeat/PPPP/2/
    
dj-project\first\templates\first\repeat.html
    
    
```python=    
{% extends "base.html" %}
{% block body %}<h1>{{ message }}</h1>{% endblock %}
 ``` 
 
結果如下:
![image](https://hackmd.io/_uploads/HJNzh0zs1g.png)
原始碼:
![image](https://hackmd.io/_uploads/ryFHNzQskg.png)
    
以下兩個範例快速製作
- dj-project\first\templates\first\say_hello.html
    
```python=
{% extends "base.html" %}
{% block body %}
    {% for i in range %}<p>say hello to {{ name }}</p>{% endfor %}

    <form action="" method="get">
        <p>
            <input type="text" placeholder="name" name="name">
        </p>
        <p>
            <input type="number" placeholder="repeat" name="repeat">
        </p>
        <p>
            <button type="submit">Send</button>
        </p>

    </form>
{% endblock %}
```
    
- dj-project\first\templates\first\list_item.html
```python=
{% extends "base.html" %}
{% block body %}
  <h1>{{ item }} * {{ times }}</h1>
  <ol>
    {% for i in range %}<li>{{ item }}</li>{% endfor %}
  </ol>

  {% if show %}
    <p>hello world</p>

  {% else %}
    <p>fail</p>
  {% endif %}

{% endblock %}
      
```    

那除此之外,Django可以做一些複雜的操作
現在在我的app的templates/底下建立一個first_base.html
    
- dj-project/first/templates/first_base.html
```python=
{% extends "base.html" %}

{% block body %}
    <h1>my first app!!!</h1>
    {% block first_body %}{% endblock %}
{% endblock %}

```
    
`dj-project/first/templates/first/list_item.html`
    
```python=
{% extends "first_base.html" %}
{% block first_body %}
    <h1>{{ item }} * {{ times }}</h1>

    <ol>
        {% for i in range %}<li>{{ item }}</li>{% endfor %}
    </ol>

    {% if show %}
        <p>hello world</p>
    {% else %}
        <p>fail</p>
    {% endif %}
{% endblock %}
```
dj-project/first/templates/first/repeat.html    
```python=
{% extends "first_base.html" %}
{% block first_body %}<h1>{{ message }}</h1>{% endblock %}
```   
各位可以看到,它是可以無限去繼承下去的,但必須思考的點是
這樣會不會太複雜,這樣做的好處,假設我有重複性的文字需要被修改
採用這樣的方式,是不錯的選擇,程式碼放在底下連結,各位可以練習看看喔!
    
結果如下:
![image](https://hackmd.io/_uploads/r1R-jf7oke.png)

## djlint 排版功能補充
可能會看到紅紅的提示
    
顯示如下:
![image](https://hackmd.io/_uploads/HJ1aCgwj1l.png)

是因為我使用了djlint
它有自動排版功能
我們要將djlint關掉
但比較推薦各位盡可能去按照lint的排版
可以看一下官方的資料,把不需要的規則關掉就好
那我提供一個方法將djlint全部關掉
最直接的方法就是到vscode
搜尋djlint lint,往下拉看到Djlint:Enable Linting
點選also modified elsewhere
我們現在用的是django HTML ,我們取消勾選
到setting.json,會看到djlint.enableLinting:false
參考網址
https://www.djlint.com/docs/linter/
    
    
### 繼承base
- dj-project\first\templates\first\say_hi.html 
    
```python=    
{% extends "first_base.html" %}

{% block first_body %}
    <p>Hello {{ name }}</p>

    <form action="" method="post">
        {% csrf_token %}
        <p>
            <input type="text" placeholder="name" name="name">
        </p>
        <p>
            <button type="submit">Send</button>
        </p>
    </form>
{% endblock %}
```
    
## 繼承first_base.html
稍微幫我整理一下,say-hi
它只繼承base.html,我們到瀏覽器看一下結果
現在我要繼承first_base.html(改一下)
先來看一下內容
{% block first_body %}
In first app!!!++ 底下
底下加入區塊名稱我給它first_body
到瀏覽器看一下,確認可以正常被執行
檢查原始碼,是完整的HTML格式.可以看到空一格
對吧!

- dj-project\first\templates\first\say_hello.html
    
```html=
{% extends "first_base.html" %}
{% block first_body %}
    <p>Hello {{ name }}</p>
    <form action="" method="post">
        {% csrf_token %}
        <p>
            <input type="text" placeholder="name" name="name">
        </p>
        <p>
            <button type="submit">Send</button>
        </p>
    </form>
{% endblock %}
```
    
那first_base.html
它可以有多層次的繼承對吧!
其實在Django中哪block是可以被選填的
我到base.html,例如,將body這個名稱改為head
title底下{% block head %}{% endblock %}

因為我下面的html都沒有對它進行填充
block區塊是選填的,沒有一定要填入,有需要再填入就可以了
http://10.11.12.100:8000/say-hi/
完成之後我再檢查一下原始碼,這邊有空一格head
但是我下面的html並沒有做填充
所以我現在不會出現任何東西

其實我們的block區塊,也可以讓它有預設值
我舉個例子,例如我再title後面加上block
類似像這樣子,重新整理之後(say-hi/)沒有任何改變
 
- dj-project\templates\base.html    
```html=
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Website
            {% block title %}- default{% endblock %}
        </title>
    </head>
    <body>
        {% block body %}{% endblock %}
    </body>
</html>
```    
  
dj-project\first\templates\first\say_hi.html
    
```html=    
{% extends "first_base.html" %}
{% block title %}Say - Hi{% endblock %}
{% block first_body %}
    <p>Hello {{ name }}</p>
    <form action="" method="post">
        {% csrf_token %}
        <p>
            <input type="text" placeholder="name" name="name">
        </p>
        <p>
            <button type="submit">Send</button>
        </p>
    </form>
{% endblock %}
```

那say-hi 繼承了first_base.html
first_base 繼承了 base對吧!
我先前我做一個say_hello.html
它是繼承base.html
可以看到 Website -default
我們再練習一次,到say-hello.html
{% block title %}- say-hello{% endblock %}
就可以看到website say-hello
各位懂我意思嗎?這是有沒有填入的差異
它會以最內層的為最高優先級

    
dj-project\first\templates\first_base.html   
```html=
{% extends "base.html" %}
{% block title %}- First{% endblock %}
{% block body %}
    <h1>In first app!!!++</h1>
    {% block first_body %}{% endblock %}
{% endblock %}
 ``` 
http://127.0.0.1:8000/say-hello/
http://127.0.0.1:8000/say-hi/
    
製作結果如下:
![image](https://hackmd.io/_uploads/SyiEHavsJl.png)

那我們看一下title,可以看到它做了改變
    
    
C:\Users\user\Desktop\dj-project\first\templates\first\_alert.html
 
### Django-模板繼承與安全的換行處理技巧
    
前面我們用繼承都是用extends,這邊開始我們來用include
假設在sayhello,還有sayhi,我希望有alret的字出現
該怎麼做?我在first底下建一個_alert.html
內容我輸入  <p>Alert!!!</p>
那這個時候我可以在say_hello.html加上include的語法
    
dj-project/first/templates/first/_alert.html
    
```python=
<p>Alert!!!</p>    
```
各位可能會有疑惑?何時用extends,何時用include?
我們在project層級都會有base.html
如果在整個app都需要出現的功能,通常會寫在那個base裡面
剛才用的alert,它不隸屬於任何app,它也不會被重複利用
所以我們會傾向於include,將它從任何地方include進來
用剛才用底線_開頭這件事情,不是一定要使用
我只是要方便去辨識它是拿來include用的
當一個程式碼不能獨自構成一個完整的頁面
這句話什麼意思我解釋一下喔!
當我們一開始return render say_hello 的時候
它是有繼承first_base,它是一個頁面
所以我用一般的檔名去命名它
不能獨自構成一個完整的頁面,我才會用底線
可以依照自己的習慣去命名
- dj-project/first/templates/first/say_hi.html    
```html=    
{% extends "first_base.html" %}
{% block title %}say-hi{% endblock %}
{% block first_body %}
    {% include "first/_alert.html" %}
    <p>Hello {{ name|linebreaksbr }}</p>
    <form action="" method="post">
        {% csrf_token %}
        <p>
            <input type="text" placeholder="name" name="name">
        </p>

        <button type="submit">送出</button>

    </form>
{% endblock %}  
```
    
dj-project/first/templates/first/say_hello.html
```html=
{% extends "first_base.html" %}
{% block title %}say-hello{% endblock %}
{% block first_body %}
    {% include "first/_alert.html" %}
    {% for i in range %}<h1>say hello to {{ name }}</h1>{% endfor %}
    <form action="" method="get">
        <p>
            <input type="text" placeholder="name" name="name">
        </p>
        <p>
            <input type="number" placeholder="repeat" name="repeat">
        </p>
        <button type="submit">送出</button>
    </form>
{% endblock %}
```
我們通常不會用safe的方法,
如果要換行,會在我想要換行的地方輸入\n
"un\nknown"
阿我剛才說\n沒用對吧!我可以用django提供的語法
`{{ name|linebreaksbr }}`
它會自動把\n換成p標籤
回頭看一下瀏覽器,就可以看到它幫我換行了
檢查網頁原始碼,就可以看到br,有換行的效果
用linebreaksbr的好處,就只會將\n換成br
而不會產生其它安全性的問題


結果如下:
    
![image](https://hackmd.io/_uploads/S1WABw_o1l.png)
    
![image](https://hackmd.io/_uploads/S1eh8P_iyl.png)

## Ubantu 移除與安裝postgresql

- 檢查版本
```bash=    
psql --version
```
    
- 停止postgresql
```bash=
sudo systemctl stop postgresql
```
- 移除postgre
```bash=
sudo apt-get --purge remove postgresql postgresql-contrib
```
    
- 移除postgre(萬一失敗)
sudo apt-get purge postgresql postgresql-*

  
- 刪除數據庫目錄與用戶

```bash=   
sudo rm -rf /var/lib/postgresql/
```
    
- 刪除PostgreSQL 用户
```bash=   
sudo deluser postgres
```

再度檢查版本
```bash=
psql --version 
```
- 1.安裝依賴包
```bash=    
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```
- 2.切換到 PostgreSQL 用戶並登入  
```bash=   
sudo -u postgres psql
```
- 3.創建數據庫和用戶   
```bash=
CREATE DATABASE dj_project;
```  
- 4.設定密碼    
```bash=
CREATE USER nameless WITH PASSWORD 'password';
```
- 5.設置用戶的客戶端編碼為 UTF-8，確保數據能夠正確存儲和傳輸  
```bash=
ALTER ROLE nameless SET client_encoding TO 'utf8';
```
- 6.設置用戶的預設事務隔離級別為 read committed    
    
```bash=
ALTER ROLE nameless SET default_transaction_isolation TO 'read committed';

```
 
- 7.設置用戶的預設時區為 UTC
```bash=
ALTER ROLE nameless SET timezone TO 'UTC';
```
- 8.授予用戶對數據庫的所有權限。   
```bash=
GRANT ALL PRIVILEGES ON DATABASE dj_project TO nameless;
```

- 9.離開    
```bash=
\q
```

- 10.檢查版本
```bash=
psql --version 
```
    
- 11.進行測試
    
```bash=
psql -U nameless -d dj_project -h 10.11.12.100
```
-U nameless：以 nameless 用戶身份登錄。
-d dj_project：連接到你創建的 dj_project 數據庫。
-h localhost：指定 PostgreSQL 服務運行在本地主機上。
10.11.12.100   
    
- 12.無法連線解決
編輯 listen_addresses
```bash=    
sudo nano /etc/postgresql/16/main/postgresql.conf
```
listen_addresses = '*'
    
pg_hba.conf
```bash=   
sudo nano /etc/postgresql/16/main/pg_hba.conf
```
host    all             all   
10.11.12.100/32         md5

host    all             all             10.11.12.0/24           md5
    
檢查狀態
```bash=
sudo systemctl status postgresql
```
    
```bash=
sudo systemctl start postgresql
```
```bash=
GRANT ALL PRIVILEGES ON SCHEMA public TO nameless;
```
```bash=
ALTER USER nameless WITH PASSWORD 'password';
```
    
```bash=
psql -h 10.11.12.100 -U nameless -d dj_project
```  
    
- 13. 確保 PostgreSQL 使用者具有適當的權限

你需要為 PostgreSQL 使用者（在配置中為 nameless）授予在 public 模式中創建表的權限。你可以通過以下步驟來實現：

以 postgres 超级用户身份登陸PostgreSQL 數據庫：


psql -U postgres
然後，選擇你的數據庫（在此情况下是 dj_project）：

sql
```bash=
\c dj_project
```
给 nameless 用户授予創建表的權限
```bash=
GRANT ALL PRIVILEGES ON SCHEMA public TO nameless;
```
還沒有為使用者授予表的權限，你還需要執行以下命令：


```sql=
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO nameless;
``
確保對未來創建的表也給予權限


```sql=
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO nameless;
```
退出 PostgreSQL


```sql=
\q
```
    
重新運行遷移


```sql=
python manage.py migrate --database=postgres
```
    
結果如下:
![image](https://hackmd.io/_uploads/BkqyiNgn1x.png)


### 回到win10介紹Model(2025/03/12)
    
前面有說過Django是MTV架構
template有用過,view也用過
我們這一小節準備來講model
在開始之前會簡單使用一下資料庫
你就把它想像成很多excel的集合
可以做很複雜的操作跟運算
我這邊會使用SQLite,它是一個單一的檔案
我們這邊是練習用,如果要上線的網站
不要用SQLite當資料庫,因為它只有DB的功能
頂多拿來開發用,我們打開一個資料庫
Django內建都有一些功能,它有
db.sqlite3,接著到終端機輸入 

`python manage.py migrate`
它就幫我們把表全部套用在db.sqlite3,按一下F5重新整理
### models模組,資料庫操作

    
```python=
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)

```
    
```python=
python manage.py makemigrations
```
結果如下:
    
![image](https://hackmd.io/_uploads/HyoqSW12kg.png)

    
## Model,makemigrations,migrate(2025/03/13)
    
前面有提到我們建好一個initial0001的檔案
這個檔案是自動產生的,它由Django自動產生它
這裡會記錄,這次的版本與上一次的版本
可以看到 dependencies = []裡面是空的
因為是0001所以沒有前面的版本它不依賴於任何先前的遷移。
與前面不同的是,我建立一個名為Post的Model
fileds欄位有兩個,一個是id,一個是title
這時候各位可能會有疑惑,我的models.py明明就只有
title,為什麼這邊有id跟title呢?

所有資料表中一定有一個欄位叫做pk
每個 Django 模型都會有一個主鍵欄位來唯一標識每一行資料。
我們在models沒有建立
當它發現這張表裡面沒有pk的時候,會自動建立一個流水號的pk
我們通常的習慣是不會主動建立pk,除非有特殊需求
那我的migration file生成之後呢?
這個時候我可以輸入 python manage.py migrate
按下enter,到資料庫看一下,重新整理,就可以看到first_post
這張表長出來了,裡面有id還有title,而且是varchar255
Variable Character（可變字元），
它是一種用來儲存字串資料的資料型態。   

```pytohn=
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)

```

結果如下:
![image](https://hackmd.io/_uploads/BkLIObe21e.png)


    
除此之外,我也可以告訴Django,請幫我套用
python manage.py migrate first 
意思是告訴 Django 要將 first 
這個應用的資料庫遷移（migration）
套用到 版本 0001，即回到 first 應用的第一個遷移版本。
我們到資料庫結構,就可以看到is_public這個欄位不見了 
    
```python=
 python manage.py migrate first 0001   
```
    

![image](https://hackmd.io/_uploads/ryHAUZl2kx.png)

### 整理關於遷移檔
產生遷移（migrations）檔
```python=
python manage.py makemigrations
```   
套用遷移檔到 
```python=
python manage.py migrate
```
    
將 DB 退到特定的版本
```python=
python manage.py migrate first 0001
```
    
希望退到 first 0001 之前
```python=
python manage.py migrate first zero
```
作者:非本科系學程式找工作