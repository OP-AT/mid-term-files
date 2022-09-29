x = int(input("Enter first number here: "))
y = int(input("Enter second number here: "))
l1 = []
l2 = [1,2,3,4,5]
l3=[]
if x>y:
    upper=x
    lower=y
else:
    upper =y
    lower = x
def large(x,y):
    if x>y:
        print(x,"is greater than",y)
    elif x==y:
        print("Both the numbers are equal.")
    else:
        print(y,"is greater than",x)
def add(x,y):
    l1.append(x)
    l1.append(y)
    print("Your numbers are added in a list: ",l1)
def add_list(l1,l2):
    l3=l1+l2
    print(l3)
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
while True:
    print("MENU DRIVEN")
    print("1) Display the largest number.")
    print("2) Add these 2 numbers in the list")
    print("3) Provide a pre-created list to a function and add both the list.")
    print("4) Display all the prime numbers between both the numbers.")
    print("5) Exit the program")
    ch = int(input("Enter your choice: "))
    if ch ==1:
        large(x,y)
    elif ch ==2:
        add(x,y)
    elif ch ==3:
        add_list(l1,l2)
    elif ch ==4:
        ans = prime(lower,upper)
        print(ans)
    elif ch ==5:
        break
    else:
        print("Invalid choice")
    #Made by Varnit Kalra
    #Class XII-A
    #Admn number: 6709
    #If found please return to him. :)
    #Thanks!