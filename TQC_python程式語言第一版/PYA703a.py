words = ()

while (word := input()) != "end":
    words += (word,)
print(words)
print(words[:3])
print(words[-3:])
