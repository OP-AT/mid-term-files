def countword():
    f = open("data.txt","r")
    count = 0
    data = f.read()
    word = data.split()
    for i in word:
        if i == "The" or i == "the":
            count+=1
    print("Total number of 'the' or 'The' are: ",count)
    f.close
countword()