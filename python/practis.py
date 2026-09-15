#WAP to ask the user to enter names of their 3 favorite movies & store then in a list.

movies = []

# short cut form
# movies.append(input("enter 1st movie: "))
# movies.append(input("enter 2st movie: "))
# movies.append(input("enter 3st movie: "))
# print(movies)

mov1 = input("Enter 1st movie : ")
mov2 = input("Enter 2st movie : ")
mov3 = input("Enter 3st movie : ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
print(type(movies))
