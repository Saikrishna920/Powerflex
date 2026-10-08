with open("abc.txt","r") as f:
    d={}
    a=input("enter a key:")
    for i in f.readlines():
        key,value=i.split(":")
        d[key]=value
        for j in d.keys():
            if j==a:
                print(d[j])

