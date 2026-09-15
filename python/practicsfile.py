# Create a new file "practices.txt" using puthon. Add the following data in it:

with open("practices.txt","w") as f:
    f.write("Hi everyone\nWe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

# WAF that replace all occurrences of "java" with "python" in above file.

with open("practices.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("practices.txt","w") as f:
    f.write(new_data)


# Search if the word "learning" exits in the file or not.
word = "learning"
with open("practices.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

# WAF to find in which line of the file does the word "learning" occur first. print -1 if word not found.


