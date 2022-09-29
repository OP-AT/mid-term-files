a = open("myfile.txt","r")
c = a.read()
b = c.split()
for i in b:
    if len(i) ==3:
        print(i)
    else:
        pass
a.close()