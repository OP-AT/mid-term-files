import csv
f = open("data.csv", "r")
a = csv.reader(f)
print(a)
f.close()