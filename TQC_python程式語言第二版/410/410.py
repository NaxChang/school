n = int(input())
with open("read.txt", mode="r", encoding="utf8") as f:
    data = f.readlines()
with open("write.txt", "w", encoding="utf8") as f:
    for i in range(n):
        ans = ""
        L = data[i].split()
        for j in range(len(L)):
            L[j] = L[j].capitalize()
        ans += " ".join(L) + "\n"
        print(ans)
        f.write(ans)
