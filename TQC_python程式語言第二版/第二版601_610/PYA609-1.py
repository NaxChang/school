# -*- coding: utf-8 -*-
year, month, day = map(int, input().split())

# 檢查閏年，若是閏年將 2 月的天數改為 29
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    days_in_feb = 29
else:
    days_in_feb = 28

# 定義每個月的天數
days_in_month = [0, 31, days_in_feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 檢查輸入日期是否合法
if month < 1 or month > 12 or day < 1 or day > days_in_month[month]:
    print("error")
else:
    # 計算日期是當年的第幾天
    day_of_year = sum(days_in_month[:month]) + day
    print(day_of_year)
    
   