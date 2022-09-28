# Write a menu based program to show all operations on a stack , based on the choice selected by the user.
print("to add element press 1")
print("to pop  press 2")
print("to display stack  press 3")
print("to exit press 4")
stk = []
while True:
    ch = int(input("enter your choice"))
    if ch == 1:
        ask = int(input("enter element to be added: "))
        stk.append(ask)
    elif ch == 2:
        stk.pop()
    elif ch == 3:
        print(stk)
    else:
        break
