import csv
with open("pass.csv","w") as a:
    b = csv.writer(a)
    b.writerow(["User Id","Password"])
    while True:
        user = input("Enter id: ")
        password = input("Enter password: ")
        rec = [user,password]
        b.writerow(rec)
        ch = input("press y to continue and n to terminate the program\n")
        if ch in "Nn":
            break
        elif ch in "Yy":
            continue
a.close()
with open("pass.csv","r") as x:
    x2 = csv.reader(x)
    inp = input("Enter the user id to be searched: ")
    for i in x2:
        next(x2)
    if i[0] == inp:
        print("password is: ",i[1])
    else:
        pass