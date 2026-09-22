import re
with open("def.txt", "r") as f:
    a=input("Enter a string:")
    for i in f.readlines():
        if a in i:
            k=re.findall(r"[0-9]+[.][0-9]+",i)
print(k)
