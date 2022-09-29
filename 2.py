l1 = []
i = 0
y = 10
while y >i:
    x = int(input("Enter the element you want to add: "))
    l1.append(x)
    i+=1
print(l1)
while True:
    print("Menu Driven")
    print("1. Display the largest number")
    print("2. Count the number divisible by 5")
    print("3. Count even and odd numbers.")
    print("4. Increase the number by 2 if it is a positive number.")
    print("5. Exit the program.")
    ch = int(input("Enter your choice here: "))
    if ch ==1:
        l1.sort()
        print(list[-1]) 
    elif ch ==2:
        l2 = []
        for i in range(0,y):
            if l1[i] %5==0:
                l2.append(l1[i])
        print("Total number of elements which are divisible by 5 is ",len(l2))
    elif ch ==3:
        even = []
        odd = []
        for i in range(0,y):
            if l1[i]%2==0:
                even.append(l1[i])
            else:
                odd.append(l1[i])
        print("The number of odd numbers are: ",len(odd))
        print("The number of evern numbers are: ",len(even))
    elif ch ==4:
        for i in range(0,y):
            if l1[i] >0:
                l1[i]+=2
        print(l1)
    elif ch ==5:
        break
    else:
        print("Invalid choice.")