def max_word():
    x = open("data.txt","r")
    words = x.read().split()
    max_len = len(max(words,key=len))
    return [word for word in words if len(word)==max_len]    
def min_word():
    y = open("data.txt","r")
    words = y.read().split()
    min_len = len(min(words,key=len))
    return [word for word in words if len(word)==min_len]   
print("Longest word is: ",max_word())
print("Shortest word is: ",min_word())