info = {
    "key": "value",
    "Name":"Saad",
    "age": 16,
    "Salary": 10000,
    "Loved ones":0,
    "married": False,
    "Siblings born year": [2010, 2013, 2015, 2020],
    "Fav Sub": ("Computer", "Biomechanics"),
}
"""DICTIONARY
 is a datatype to store 
Key: value pairs. It is mutable & except 
List we can use every datatype as a key but
for Value evry datatype is eligible"""


# """METHODS"""
print(info.keys()) #Return a collection of keys in dic
print("\n\n")
print(info.values()) #Return a collection of values in dic
print("\n\n")
print(info.items()) #Return All keys and values in pairs as a tuple
print("\n\n")
print(info.get("Siblings born year"))#Return the value of the key
print("\n\n")
New_info = info.update({1:1})#Returns the Dictionary with a newly added key:value pair
print(New_info)
print("\n\n")



"""DIFF B/W Info.get() & Info[]
If the key Doesn't exist Info.get() will not 
give any errors instead the output will be 
(None) while Info[] will give an error"""


"""SET
it is a datatype that stores values of different datatypes 
similar to lists, duplication is overwrited and 
list and dictionary datatypes are not valid in a set. 
It's elements are immutable and it is an unordered 
collection of data."""

collection = {1,22,"hello", "hello", False, 4.44444444,1,345,"world", (0,9,8,9,0)}
print("\nSETS:")
print(collection)
#empty SET
collection_1 = {}#this a dic syntax
collection_2 = set()


#SET METHODS
print("\nTYPE OF DATA:")
print(type(collection_2))
collection_2.add(123)#adds elements in a set
collection_2.add(True)
collection_2.add("Hello")
collection_2.add("World")
collection_2.add(4.889)
collection_2.add(1)
collection_2.add(22)
print("\nADDITION:")
print(collection_2)
collection_2.remove(4.889)#remove elements in a set
print("\nREMOVAL:")
print(collection_2)
collection_2.pop()#remove a random element can be anyone
print("\nREMOVE ANY RANDOM ELEMENT")
print(collection_2)
collection_2.intersection(collection)#combines the same elements and return a new set
print("\nUNION OF TWO SETS:")
print(collection_2)
collection_2.union(collection)#add the elements of the other set and make a new set
print("\nINTERSECTION OF TWO SETS:")
print(collection)
collection_2.clear()#empty the set
print("\nEMPTY THE SET:")
print(collection_2)


