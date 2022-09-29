i = 0
def fact(n):
    if n ==0:
        return 1
    else:
        return(n*fact(n-1))
while i<10:
    n = int(input("Enter number here: "))
    print(fact(n))
    i+=1