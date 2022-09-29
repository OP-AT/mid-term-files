l = (1,2,3,4,5,6,7,8,9,10)
di = ["Varnit","Adrija","Ashmit","Shubham","Kashish"]
d = {}
m = []
for i in range(0,10):
    m1 = print("Enter marks of",di[i],"here:",end="")
    m2 = int(input(" "))
    d2 = {}
    d2["name"] = di[i]
    d2["marks"] = m2
    e = l[i]
    d[e]=d2
print(d)
print("MENU DRIVEN")
print("1) Name of student scoring highest marks.")
print("2) To arrange in ascending order.")
print("3) To create record of students scoring less then 400 marks.")
print("4) To add another record.")
print("5) To exit the program.")
while True:
    ch = int(input("Enter choice here: "))
    if ch==1:
        x = max(m)
        for i in d:
            if d[i]["marks"] == x:
                print(d[i]["name"],"got the maximum marks.")
    elif ch ==2:
        v = sorted(l)
        y = {}
        for i in v:
            v[i] = y[i]
        print(y)
    elif ch ==3:
        z = {}
        for i in d:
            if d[i]<400:
                d[i] = z[i]
        print(z)
    elif ch ==4:
        b1 = int(input("Enter board roll no. here: "))
        b2 = list(l)
        b2.append(b1)
        l = tuple(b2)
        v2 = input("Enter name of student.")
        di.append(v2)
        print("Enter marks of ",v2,"here: ",end="")
        b3 = int(input(" "))
        m.append(b3)
        b4 = {}
        b4["name"] = v2
        b4["marks"]=b3
        d[b1]=b4
        print(d)
    elif ch ==5:
        break
    else:
        print("Invalid choice")