age0 = 21

if(age0 >= 18):
    print("You are eligible for driving license!")


light = "green"

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("ready")
elif(light == "green"):
    print("go!")

"""if statement will alaways
 check for the condition whether
 previous was true or not
 but else if statement would not if 
 if statement becomes true. Else 
 condition is always used at the end 
 of all the conditions and executed 
 if no conditions are met."""
num = 6

if(num >= 10):
        print("greater than 10")
if(num >= 15):
        print("greater than 15")


if(num >= 7):
        print("greater than 7")
elif(num >= 19):
        print("greater than 19")
else:
      print("unexpected value")


#Grading system
marks = 80

if(marks >= 80):
      print("grade = A+")

elif(marks >= 70 and marks < 80):
      print("grade = A")

elif(marks >= 60 and marks < 70):
      print("grade = B")

elif(marks >= 50 and marks < 60):
      print("grade = C")

elif(marks >= 40 and marks < 50):
      print("grade = D")

else:
      print("You are fail you need to work your ass off")

marks_1 = int(input("enter student marks : "))

if(marks_1 >= 90):
      grade = "A+"
elif(marks_1 >= 80 and marks_1 < 90):
      grade = "A"
elif(marks_1 >= 70 and marks_1 < 80):
      grade = "B"
elif(marks_1 >= 60 and marks_1 < 70):
      grade = "C"
else:
      grade = "D"

print("You grade is :", grade)

if(grade == "A+" or grade == "A" or grade == "B"):
      msg = "Well done you did your best keep it up"
else:
      msg = "Failure doesn't means end it's a place where you learn how\nto rise, so keep going even if you can't even if you don't\nwant to just keep going and eventually you will get there.\n\nGood luck!"      

print(msg)

#nesting of statements:

age = int(21)
if(age >= 18):
    if(age > 70):
            print("cannot drive")
    else:
            print("can drive")
else:
      print("cannot drive")   

#WAP to check whether a number is even or odd:

num = int(input("enter any random number :"))
if(num % 2 == 0):
      number = "Even number" 
else:
      number = "Odd number"
print("Your input number is" , number)

#WAP to find the greatest of 3 numbers entered by the user

num_1 = int(input("enter any num : "))
num_2 = int(input("enter any num : "))
num_3 = int(input("enter any num : "))

if(num_1 > num_2 and num_1 > num_3):
      print(num_1 , "is the greatest number")
elif(num_2 > num_1 and num_2 > num_3):
      print(num_2 , "is the greatest number")
else:
      print(num_3 , "is the greatest number")

#WAP to check whether a number is a multiple of 7 or not

seven = int(input("enter your number : "))
if(seven % 7 == 0):
      print("the number is a multiple of 7")
else:
      print("it is not a multiple of 7")



