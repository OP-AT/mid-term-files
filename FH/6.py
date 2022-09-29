f = open("data.txt","r")
a = f.read()
for i in a.split():
    if "p" in i:
        a.replace("p","")
        print(a)
f.close()