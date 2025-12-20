What -> means in a function signature
The syntax appears after the function's parameter list and before the colon that marks the start of the function body. 
The code following the arrow indicates the expected type of the value the function will return. 


##mangaing python version
using this command: pyenv
$ pyenv global 3.7.3
$ pyenv versions
  system
* 3.7.3 (set by /Users/dhillard/.pyenv/version)

$ pyenv local 3.7.3
$ pyenv versions
  system
* 3.7.3 (set by /Users/dhillard/myproj/.python-version)

$ pyenv shell 3.7.3
$ pyenv versions
  system
* 3.7.3 (set by PYENV_VERSION environment variable)

$ python --version
Python 3.7.3
  system
* 3.7.3 (set by /Users/dhillard/myproj/.python-version
         
###using with, this has the benifit of cleaner code to utilise objects with a lifecycle like a socket or text. 
with open('txt.file') as f:
    data = f.read()


#use hash to comment throught your code for documentation
# PYTHON DOESNT HAVE A syntax for multiline comments, using hash multiple times allows multiline comments

x = "bril"
normal = 1

name = "bril"

number = 1 
fl = bool(2.432)
bool = True
bool = False

print(type(fl))

#creating a tuple
tupleList = ("first name","surname", "third name")
print(tupleList)
len(tupleList)

many_to_one = ["many","to", "one"]
#creating a list that matches 1 to 1 with the values in alist.
objects = ["MANY", "TO", "ONE"]
many, to, one = objects 
print(many) 

#function using global keyword
#at first i was doing the print statement outside of the function but it wouldnt work
#because y is a local variable,  the x worked cos it was gloabal
def globalFunc():
    global x 
    x = "bril"
    y = "adu"
    print("hi my name is ", x , y)
globalFunc()
#incorrect method. 
n = 5
type(n)
print(n)
#corrrect method. type is inside print statement
j = 9j
print("my value type is",type(j))
#floats can alsod be numbers with an "e" to indicate power of 10
z = -87.245e10
#complex numbers are writen with a "j" as an imaginary part
gene = 6j


#####THE CODE BELOW SHOWS HOW CHANGING THE TYPE ACTUALY GIVES IT NEW VALUES TO BECOME THE CHANGED TYP
#####
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

import random

print(random.randrange(1, 10))

A = """THIS IS A MULTILINE STR,
CAN OYU BELEIVE IT"""

print(A[0])

#getting length of a string 
functionLength = "what is the lenth of this function"
print(len(functionLength))

##checking if something is "in" a string using in
string = "my name is bril"
indeed = print("bril" in string)


#using if statement to creat conditioinal based on in 
string = "my name is bril"
indeed = print("bril" in string)
if indeed == True:
  print(string)


  
   


###for loops
###for incriments through a sequence/iterable object e.g list, tuple
##e.g list for loop below
for num in [1,2,3,4,5,6]:
 print(num)
 #string
for string in "name":
   print(string)



magicBox = range(3,8)

if userInput in magicBox:
   print("yes its there")
elif userInput == [1,2]:
   print("you are too cold") 
elif userInput in range(8,11):
   print("you are too cold")  
else:
   print(userInput, "not even close")


magicBoxx = [4,8,6]

userGuess = int(input("guess a number between 1 and 10 in my magix box: "))

if userGuess == magicBoxx:
   print("YOU GUESSED CORRECT")
else:
   print("you guessed incorrect guess again" ) 

print('       1')
print('     2','3')
print('   4','5','6')
print('7','8','9','10')
