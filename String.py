#why three methodes given to define a string

# 'this is apnacollege's Youtube channel'
# "this book was written by "Saad azam""


# escape characters 

str1 = "this is a string.\n we are now creating strings"
print(str1)
str2 = "this is a string.\t we are now creating strings"
print(str2)

#Basic Operations in str


# concatenation:
# length function to find str length:
str3 = "apna"
str4 = "college"
final_str = str3 + str4
final_str1 = str3 + " " + str4
print(final_str, "  ", final_str1)
len1 = len(final_str)
len2 = len(final_str1)
print(len1)
print(len2)


#in length special chr and whitespaces are also counted
#str indexing starts from 0 and tells the location for access

#Indexing:

ch = final_str1[2]
print(ch)

#Slicing:

Name = "SAADAZAM"
slice1 = Name[0:4]
print(slice1)

Name1 = "SAADAZAM"
slice12 = Name1[0:len(Name1)]#we can use len function if we want to go to the last index
print(slice12)

Name2 = "SAADAZAM"
slice123 = Name2[0:]#this way you say that you have to go to the last index sam egoes for the opposite.
print(slice123)

#negative counting for index is also valid in slicing

fruit = "apples"
print(fruit[-5:-3])
print(fruit[-4:-1])
#ending index is not included



#STRING FUNCTIONS:

rand_line = "i am learning python from apna college"

print(rand_line.endswith("ege"))

print(rand_line.capitalize())#a copy of string will be created
rand_line = rand_line.capitalize()#this will modify the original string
print(rand_line)

print(rand_line.replace("python","C & C++"))

print(rand_line.find("apna"))#returns the index of the chr 1st occurence
#find function will return -1 index if the given chr is not found

print(rand_line.count("i"))

#PRACTICE:
#WAP to input user first name & print it's length
# User_first_name = input("Enter Your First Name: ")
# print("You first name length including whitespaces is ",len(User_first_name))


#WAP to find the occurence of "$" in a string
Occur_var = "If i learned python, C, C++ and Java i will be able to earn $200K per year"
print(Occur_var.find("$"))

