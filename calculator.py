val1 = int(input("enter a random number : "))
val2 = int(input("enter a random number : "))

operation = input("enter the operation you want to perform : ")

if(operation == "+"):
    operation1 = val1 + val2
    
elif(operation == "-"):
    operation1 = val1 - val2

elif(operation == "*"):
    operation1 = val1 * val2   

elif(operation == "/"):
    operation1 = val1 / val2

print(operation1)