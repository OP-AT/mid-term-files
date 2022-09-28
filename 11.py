import pickle


def serachrec():
    try:
        while True:
            a = pickle.load(f)
            if a[0] == code:
                print(a)
    except EOFError:
        pass


f = open("items11.dat", "rb")
code = int(input("enter code to be searched: "))
serachrec()
f.close()