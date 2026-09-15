# file read a program. 

f = open("demo.txt","r")
data = f.read(5)
print(data)
print(type(data))
# f.close()

f1 = open("demo.txt","r")

line1 = f.readline()

print(line1)
f1.close()

