import converter
a = int(input("Enter price of first itme: "))
b = int(input("Enter price of second itme: "))
c = int(input("Enter price of third itme: "))
d = int(input("Enter price of fourth itme: "))
e = int(input("Enter price of fifth itme: "))
ask = input("Do you want to convert into dollars or ruppees?('dollar' or 'ruppee': ")
ask = ask.lower()
if ask == "dollar":
    converter.dollar(a,b,c,d,e)
    print("Your total bill is: ",total)
elif ask == "ruppee":
    converter.ruppee(a,b,c,d,e)
    print("Your total bill is: ",total)
else:
    pass