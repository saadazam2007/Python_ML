
x = int(input("Enter any value for x  ")) 

if(x > 10):
    print(x,"x should be less than or equal to 10")
else:
    match x:
        case 0:
            print(x, "is equal to zero")
        case 1:
            print(x, "is equal to one")  
        case 2:
            print(x, "is equal to two")
        case 3:
            print(x, "is equal to three")
        case 4:
            print(x, "is equal to four")
        case 5:
            print(x, "is equal to five")
        case _:
            print(x, "is probably any number between 6 to 10")
            if(x == 6):
                print(x, "is six")
            elif(x == 7):
                print(x, "is seven")
            elif(x == 8):
                print(x, "is eight") 
            elif(x == 9):
                print(x, "is nine")
            else:
                print(x, "is ten")  





