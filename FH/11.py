import pickle
b = open("items.dat","rb")
def search(stri):
    try:
        while True:
            a = pickle.load(b)
            if a[0] == stri:
                print(a)
    except EOFError:
        pass
stri = int(input("Enter code to be searched: "))
search(stri)
b.close()