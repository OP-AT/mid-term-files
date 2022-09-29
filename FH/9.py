import pickle
a = open("school.dat","wb+")
x = input("Enter the string you want to put in the file: ")
pickle.dump(x,a)
a.close()
b = open("school.dat","rb")
z = pickle.load(b)
z = z[::-1]
print(z)
b.close()