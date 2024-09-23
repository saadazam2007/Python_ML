#LIST datatype in Python
#It is similar to an array but it can store values of different data types.

Marks = [ 30, 40, 50, 60, 70 ]
student_m = ["Gandhi" , 15  ,  "Quaid" ,  25 ]
print(Marks[0])
print(student_m[3])
print(len(student_m))


#Lists are mutable
'''strings value cannot be changed
a = "Hello"
print(a)
a[0] = h
this is not possible
but in lists
a = ["Hello", "Hi"]
print(a)
a[0] = h
the value will be updated'''

#List Slicing
print(Marks[1 : 3])#last index will not be included
#negative slicing
print(Marks[-2 : -1])
#List methods
#methods are specific for any datatype

list = [1,2,3,7,4,6,5]
'''APPEND
it adds an element at the end of a list'''
print(list.append(6))
print(list)#in lists only the updation will take place when using methods unlike striings
'''SORT
sort() and sort(reverse = true)
sorts the item of the list into ascending or
descending order'''
print(list.sort())#only the list will be updated no result would be shown
print(list)
print(list.sort(reverse=True))
print(list)
#sorting is also possible in strings
list_1 = ["apple","banana","ant","zebra","x","y","c"]
print(list_1.sort())
print(list_1)
'''REVERSE
all the items order of a list will be reversed'''
print(list.reverse())
print(list)
'''INSERT
it is similar to append but use to add
elements on a specified index'''
print(list.insert(0, 90))
print(list)
'''REMOVE
remove the defined items for the first index it occurs'''
print(list.remove(6))
print(list)
'''POP
removes the element on the specified
index provided'''
print(list.pop(0))
print(list)

#TUPLE datatype in Python
#a buit-in data type that let us create immutable sequences of values
tup_0 = (2,3,4,5,8,6,1,1)
print(type(tup_0))

print(tup_0[0])
'''UPDATION
we cannot update an index in a tuple
EX:
tup[0] = 20
Error will ocur'''
'''SINGLE CHR TUPLE SYNTAX
if we want to create a single element tuple a coma is necessary or the language will not perceive it as a tuple
EX:
tup_1 = (1)'''
tup_1 = (1,)
print(tup_1)
'''SLICING
Itis the same as list or string slicing'''
print(tup_0[0:3])

#TUPLE METHODS:
'''INDEX
To find the index of first occurence
of any element'''
print(tup_0.index(6))
'''COUNT
counts the total number an element
occur in a tuple'''
print(tup_0.count(1))
