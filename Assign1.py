#WAP to count odd and even numbers out of 10 entered numbers.
for i in range(0,10):
    n = int(input("Enter max number here: "))
    if n%2 == 0:
        print(n,"is an even number")
    else:
        print(n,"is an odd number")