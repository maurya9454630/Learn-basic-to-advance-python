# Write a file.

f = open("demo.txt","w")

f.write("Than I will move to reactjs. \n After that nodejs")


f = open("demo.txt","w+")
# f.write("abc")
print(f.read())
f.write("abc")

f.close()
