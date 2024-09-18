#Creating variables

name = "Saad"
Age = 16
Gpa = 3.5
male = True
extra = None

#checking datatypes with "type" function in print
# the most basic datatypes

print(type(name))
print(type(Age))
print(type(Gpa))
print(type(male))
print(type(extra))

# assigning variable with a string value

name1 = 'Saad'
name2 = "Saad"
name3 = '''Saad'''

print("assigning variables with str datatype")
print(type(name1))
print(type(name2))
print(type(name3))

#Printing sum of two var

val1 = 12098
val2 = 1379

print(val1 + val2)

#comments

#single line comment
"""Multi-line comment
val1 = 12098
val2 = 1379
print(val1 + val2)"""


#OPERATORS
#arithematic operators

a = 1
b = 2

sum = a+b
diff = a-b
mult = a*b
div = a/b
exponent = b**a
modulus = b%a

print(sum, "," , diff, "," , mult, "," , div, "," , exponent, "," , modulus)


#relational/comparison operators

equal = a==b
not_equal = a!=b
greater = a>b
lesser = a<b
greater_equal_to = a>=b
lesser_equal_to = a<=b

print(equal, "," , not_equal, "," , greater, "," , lesser, "," , greater_equal_to, "," , lesser_equal_to)


#assignment operators


num = 10 
num += 10
num -= 3
num *= 10
num /= 3
num **= 2
num %= 2

print(num)

#logical operators

print(not a<b)
print("and operator", (50 == 50) and (49>=50))
print("or operator", (40==40) or (50>=60))

# OPERATORS ------------X------------X-----------X--------------X

#Type conversion
d = 4  #int
e = 4.9  #float


sum23 = d + e  #automatically converts int into float value 4.0 + 4.9 => 8.9
print(sum23)

# f = "4"  #str
# g = 4.9  #float
# sum234 = f + g  #cannot automatically converts str into float value against sysntax
# print(sum234)

#Type casting
h = float("3")  #type casting cannot work for scenario like a="saad"+b=4
i = 4
print(h+i)
j = 3.190
j = str(j)
print(type(j))



#input

acd = input("enter your name: ")
print(acd)
input("enter your age: ")
name2 =input("enter your name: ")
print("Hey how's evrything going on ", name2 )

#integers and floating values are converted into string in input function for strict datatype selection we have to use type casting

val3 = float(input("enter some value: "))
print(val3)