x = str(input("Enter your string here: "))
length = len(x)
space = 0
alnum = 0
for ch in x:
    if ch.isspace():
        space+=1
    elif ch.isalnum():
        alnum+=1
percent = (alnum/length)*100
print("Number of words are: ",(space+1))
print("Number of words are:",(length+1))
print("Number of characters are: ",(length+1))
print("Alphanumeric percentage is:",percent)