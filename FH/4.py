f = open("one.txt","r")
a = 0
e = 0
i_i = 0
o = 0
u = 0
x = " "
while x:
    x = f.readline()
    for i in x:
            if i == "a" or i == "A":
                a +=1
            elif i == "e" or i == "E":
                e +=1
            elif i == "i" or i == "I":
                i_i+=1
            elif i == "o" or i == "O":
                o+=1
            elif i == "u" or i == "U":
                u +=1
print(a,e,i_i,o,u,sep="\n")
f.close()