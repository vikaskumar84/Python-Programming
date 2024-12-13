string=set("a quick brown fox jumped over lazy dog")
print(string)
for i in string:
    if i in "aeiou":
        print(i,end=" ")
        continue