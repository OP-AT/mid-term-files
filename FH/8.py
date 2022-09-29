import pickle
a = open("comp.dat","wb+")
c = input("Enter the string you want to enter: ")
pickle.dump(c,a)
a.close()
f = open("comp.dat","rb")
eek = input("Which character do you want to search for: ")
b = pickle.load(f)
z = 0
for i in b:
    if i == eek:
        z = z+1
print(eek,"has appeared ",z,"times in the text.")
f.close()
