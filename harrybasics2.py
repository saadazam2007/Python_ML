#strings

#using double quote or single quote doesn't allow multiple line strings but triple double and single quote do
s = """Assalamualaikum
bro how are you 
i might not be able to come to the gym
today. sorry!"""
d = '''Assalamualaikum

bro how are you i might 

not be able to come to the 

gym today. sorry!'''
print(s , d)

# we can use escape sequences or alternate quote if we want to use one in our string

a = "hello \" hi\" "
b = 'hello " hi " '
print(a)

#using for loop for indexing
for chr in d:
    print(chr)
