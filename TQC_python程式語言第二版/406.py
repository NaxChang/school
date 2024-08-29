def trans(s):
    keys = "qwertyuiopasdfghjklzxcvbnm"

    ss = ""
    for x in s:
        if x == "P" or x == "p" or x == "L" or x == "l" or x == "M" or x == "m":
            ss = ss + x
        else:
            if x.isupper():
                x = x.lower()
                s1 = keys[keys.index(x) + 1]
                ss += s1.upper()
            else:
                s1 = keys[keys.index(x) + 1]
                ss += s1
    return ss


s = input()
print(trans(s))
