s = input()
ss = ""
for i in range(len(s)):
    if s[i] == ".":
        break
    else:
        ss += s[i]
print(f"{s} change to {ss}")


# print(s[i])
