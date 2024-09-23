#WAP to count the num of std with "A" grade in the following tuple
tup0 = ("A", "B", "C", "A","B", "A", "D")
print(tup0.count("A"))


#Store the above values in a list & sort them from A To D
list = []
list.append(tup0[0])
list.append(tup0[1])
list.append(tup0[2])
list.append(tup0[3])
list.append(tup0[4])
list.append(tup0[5])
list.append(tup0[6])

print(list)
list.sort()
print(list)
