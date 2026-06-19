# Python function
# A function is a block of code that perform a given tasks. They are reusable meaning after creating a function you can invoke it multiple times.
# We have 2 main functions:
# In-built functions => Pre-installed i.e print(), append(), sort(), pop etc.

# User Defined function => Created by the programmer . To create a user defined function we use the def keyword follwed by the name of the function, parentheses and a full colon at the end. On the line that follows, you need to indent which marks the strart of the body of the function.

def greating():
    print("Hello there. Hope you are doing fine")
# below we invoke/ call out the function by use of it name
greating()

print("=====================")
# below is additiin function
def addition():
    number1 = 30
    number2 = 20
    answer = number1 + number2
    print("The answer is: ", answer)

addition()

print("==============================")

# create a bfunction that is able to multipy three numbers, invoke the function to get the output
def multiple():
    number1 = 26
    number2 = 56
    number3 = 46
    answers = number1 * number2 * number3
    print("The answer is: ", answers)

multiple()

print("===================================")
# below is a function that accepts user inputs
def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1/ number2
    print("The answer is: ", quotient)

divide()
divide()
divide()