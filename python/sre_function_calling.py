# add two num argument 
# def addition(*args):
#     sum = 0 
#     for i in args:
#         sum = sum + i
#     print(sum)

# addition(12,12,12,12,12)

# argument kwargs

def information(**kwargs):
    # print(kwargs)
    print("Your information is\n\n ")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

information(name = "aman", age = 23, designation = "AI/ML")

# turnary operator

a = 12
print("even") if a%2 == 0 else print("odd")


