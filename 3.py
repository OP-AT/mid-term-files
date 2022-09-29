a = {}
i = 1
l = []
def eek(a):
    d = {}
    b = int(input("Enter item code: "))
    d["name"] = input("Enter item name: ")
    d["price"] = int(input("Enter price here: "))
    a[b] = d
    l.append(d["price"])
while True:
    ch = str(input("Do you want to enter?(Write yes or no.): "))
    if ch=="yes" or "Yes":
        eek(a)
    elif ch == "no" or "NO":
        print("Your item is: ",a)
        break
    print("MENU DRIVEN")
    print("1) Display the item code name from costliest item.")
    print("2) Enter item to search information.")
    print("3) Add more item.")
    print("4) Remove an item.")
    print("5) Exit the program. ")
    cho = int(input("Enter your choice here: "))
    if cho == 1:
        l.sort()
        for i in a:
            if a[i]["price"] == l[-1]:
                print(a[i]["name"],"is costliest")
    elif cho == 2:
        m = str(input("Enter the name here to search: "))
        for i in a:
            if a[i]["name"] == m:
                print(m,":",{"item code: ",i,"price:",a[i]["price"]})
    elif cho == 3:
        d = {}
        b = int(input("Enter item code: "))
        d["name"] = input("Enter name here: ")
        d["price"] = input("Enter price here: ")
        a[b] = d
        l.append(d["price"])
        print("Edited list is: ",a)
    elif cho ==4:
        V = str(input("Enter the name of item you want to remove: "))
        for i in a:
            if a[i]["name"] == V:
                del a[i]
                break
            print(a)
    elif cho == 5:
        break
    else:
        print("Invalid choice")
