
# s = input("Enter a string: ")

# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# second mehod

s = input("Enter a string: ")
reverse_string = ""

for char in s:
    reverse_string = char + reverse_string

if s == reverse_string:
    print("Palindrome")
else:
    print("Not Palindrome")
