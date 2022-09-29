def vowels():
    x = open("data.txt","r")
    total = 0
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for i in x.read():
        if i in vowels:
            total = total+1
    x.close()
    print("Total vowels are: ",total)
def consenants():
    y = open("data.txt","r")
    total = 0
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for i in y.read():
        if i not in vowels:
            total = total+1
        elif i >="A" or i >= "a" and i<="Z" or i <="z":
            total +=1
    y.close()
    if total>1:
        print("There are " + str(total) + " Consonants available in the File")
    elif total==1:
        print("There is only 1 Consonant available in the File")
    else:
        print("There is no any Consonant available in the File!")
def upper_lower():
    a = open("data.txt","r")
    up = 0
    low = 0
    for i in a.read():
        if i.isupper() == True:
            up = up+1
        elif i.islower()==True:
            low = low+1
        else:
            None
    print("Uppercase letters in the file :", up)
    print("Lowercase letters in the file :", low)
    a.close()
vowels()
consenants()
upper_lower()
