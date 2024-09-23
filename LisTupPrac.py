#WAP to ask the user to enter names of their 3 favorite movies & store them in list
'''list = [str(input("Enter your No.1 Favorite movie : ")),str(input("Enter your No.2 Favorite movie : ")), str(input("Enter your No.3 Favorite movie : "))]
print(list) '''

#Another way
movies = []
mov1 = input("Enter your No.1 Favorite movie")
mov2 = input("Enter your No.2 Favorite movie")
mov3 = input("Enter your No.3 Favorite movie")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
