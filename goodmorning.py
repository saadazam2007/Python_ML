import time
name = str(input("enter your name : "))
name_cap = name.capitalize()

time1 = time.strftime('%H:%M:%S')
time2 = int(time.strftime('%H'))
if(time2 < 12):
    print("Good morning", name_cap , "it's", time2)
elif(time2 < 17):
    print("Good afternoon", name_cap , "it's" , time2)
else:
    print("Good night", name_cap , "it's" , time2)

