''' Enter board roll numbers of 10 students in a tuple and names in a list. 
 Create a dictionary to store these values. 
Now add marks for each student in that. Display following information in option selected from menu:
a) Display name of the student scored maximum marks
b) Display records of students in ascending order of board roll number
c) Create another dictionary to copy records of only those students who scored less than 400 marks
d) Add one more record in a dictionary
'''
r=(18,16,14,15,12,17,13,12,1,10)
n= ["Varnit", "Akshat", "Tanmay", "Abhishek", "Rathul", "Ashmit", "Mukul", "Ayush", "Shubham", "Daksh"]
d={}
m=[]
for i in range(0,10):
    m1= print("Enter marks of ", n[i], "here: ", end= " ")
    m2= int(input(" "))
    m.append(m2)
    d2={}
    d2["name"]= n[i]
    d2["marks"]= m2
    d[i]= d2
print(d)
print("MENU")
print("1)Name of the student scoring maximum marks.")
print("2)Records of students in ascending order of board roll number.")
print("3)Create another dictionary to copy records of only those students who scored less than 400 marks.")
print("4)Adding one more record.")
print("5) Exit the program")
while 2>1:
    ch= int(input("enter your choice here: "))
    if ch == 1:
        c1= max(m)
        for i in d:
            if d[i]["marks"]==c1:
                print(d[i]["name"], "topped this exam ")
    elif ch==2:
        sorted(d)
        print(d)
    elif ch == 3:
        d3={}
        for i in d:            
            if d[i]["marks"]< 400:
                d3[i]= d[i]
        print(d3)
    elif ch == 4:
        b1=int(input("Enter the board roll number: "))
        b2= input("Enter the name of the student: ")
        print("Enter marks of  ", b2, "here: ", end= "")
        b3= int(input(""))
        b4= {}
        b4["names"]= b2
        b4["marks"]= b3
        d[b1]= b4
        print(d)
    else:
        break