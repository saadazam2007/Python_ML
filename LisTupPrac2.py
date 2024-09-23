#WAP to check if a list contains a palindrome of elements.
'''PALINDROME
ex are
racecar if we reverse it it will be same'''
list1 = [1,2,3,4,5]
list2 = [1,2,1]
copy1 = list1.copy()
copy1.reverse()
if(copy1 == list1):
    print("the list contains a palendrome of elements")
else:
    print("Don't contain")
    
copy2 = list2.copy()
copy2.reverse()
if(copy2 == list2):
    print("the list contains a palendrome of elements")
else:
    print("Don't contain")