#string slicing

a= "saad#################"
print(a[3:5])


#string length

p = "asdada sdasdasd asdasda sdad as dasd as das a sd a da sd sa das dasd as da sd asd sss"
print(len(p))


#negative slicing of strings

print(p[0:-4])
#formula print(p[0:len(p=84) - 4])which becomes print(p[0:80]) means from index 0 to 79 all elements will be printed
 


#now in case of double negative values
print(p[-83:-1])#formula (p[len(p=84)-83:len(p=84)-1]) (p[1:83])



#quick quiz
nm ="harry"
print(nm[-4:-2])# nm[len(nm=5)-4:len(nm=5)-2] , nm[1:3]
#answer is "ar"









#string methods
b = "###asdasd####"
c = '''My name is Saad. he is a 2nd year std. 
he is good at computer related subjects.
he is interested in AI. he want to build a 
Saa'S agency he also wants a marketing and AI automation
agency'''
d = 66666777777888888
#strings are immutable

print(a.upper())#give the string in uppercase


print(a.capitalize())#make the 1st word capital and all the other's lowercase


print(a.lower())#give the string in lowercase


print(a.rstrip("#"))#this removes any tailing chr not leading chr
print(b.rstrip("#"))


print(c.replace("he" , "I"))#replaces the defined str all occurences


print(p.split(" "))


print(a.center(150))#aligns the string


print(a.count("#"))#give us the number of occurence of the defined str


print(a.endswith("a"))#check whether the variable ends with the defined value
#we can even check the value in betwen by giving starting and ending index positions
print(a.endswith("d", 0 , 4))


print(a.startswith("s"))#check whether the variable starts with the defined value


print(a.find("#"))#tell us the index of the first occurence of the value given


print(a.index("a"))#raises value error when the substring is not found


a = "sadasfdsfs23423545"
print(a.isalnum())#tell whether string contains a-z, A-Z, 0-9 returns true or false


a = "saaadasdefsfd"
print(a.isalpha())#tell whether string contains a-z, A-Z returns true or false


print(a.islower())#tell whether the string is in lower case


print(a.isupper())#tell whether the string is in upper case


print(a.isprintable())#tell whether the string is printable
a = "saad#######\n"
print(a.isprintable())



print(a.isspace())#tell whether string contains whitespaces, returns true or false 


a = "Saad is studying "
print(a.istitle())#tell whether string has all the words first letter capital, returns true or false


print(a.swapcase())# it converts the str case into lower if it is in upper or upper if it is in lower


print(a.title())#change the str case to title case





