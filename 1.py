x = int(input("Enter first number here: "))
y = int(input("Enter second number here: "))
while True:
    print(("MENU DRIVEN"))
    print("1. Print the largest number.")
    print("2. Print x raised to power y.")
    print("3. Check whether first number is divisible by second number or not")
    print("4. Calculate the remainder by dividing first by second.")
    print("5. Exit the program.")
    ch = int(input("Enter your choice here: "))
    if ch == 1:
        if x>y:
            print(x,"is greater.")
        else:
            print(y,"is greater.")
    elif ch == 2:
        print(x**y)
    elif ch==3:
        if x %y==0:
            print("It is divisible.")
        else:
            print("It is not divisible")
    elif ch ==4:
        print("The remainder is: ", x/y)
    elif ch ==5:
        break
    else:
        print("Invalid choice")