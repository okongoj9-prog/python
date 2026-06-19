# Python Modules
# A module in python isa file that contains the python definations and structures. Defination may include variables, functions, loops etc...
# We need modules to separate a huge chunk of a progrm into smaller and manageable pieces which are easier to understand and work with.
# In python wew have 2 main types of modules i.e: inbuilt modules and the user defined modules.


def add():
    number1 = 20
    number2 =50
    sum = number1 + number2
    print("The sum is:", sum)


print("======================")

#Below is afunction to find the difference of number
def subtracrt():
    numx = int(input("Enter the first number: "))
    numy = int(input("Enter the second number: "))
    difference = numx - numy
    print("The difference of the number is: ", difference)

# create python function that is able to calculate the area of a squere import the  function on lesson 5b and invoke it there.
print("===========================")
def area():
    length = int(input("Enter the length: "))
    length = int(input("Enter the width: "))
    Area = length * length
    print("The answer is: ", Area)

area()