f = open("data.txt","r")
line = " "
while line:
    line = f.readline()
    for i in line.split():
        print(i,end="#")
    print()
f.close()