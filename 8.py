import pickle
f = open("comp8.dat", "wb+")
a = input("enter desired string here: ")
pickle.dump(a, f)
f.close()

f = open("comp8.dat", "rb")
inq = input("which character to search for: ")
a = pickle.load(f)
chrc = 0
for chr in a:
    if chr == inq:
        chrc += 1
print(inq, "has appeared ", chrc, "time in  the text")
f.close()