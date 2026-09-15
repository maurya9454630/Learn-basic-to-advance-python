# WAF to find in which line of the file does the word "learning" occur first. print -1 if word not found.
def check_for_word():
    word = "learning"
    with open("practices.txt","r"):
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practices.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()

# From a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("practices.txt","r") as f:
    data = f.read()
    # print(data)

    nums = data.split(",")
    for val in nums: 
        if(int(val) % 2 == 0):
            count +=1
        
    print(count)
    # print(nums)

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(num)
    #         num = ""
    #     else:
    #         num += data[i]

