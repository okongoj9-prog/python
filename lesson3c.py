# Python Loops
# Some times we may need to do apiece of code number of times and in such a case a loop may be of importance.A loop is a contro structure thayt allows to execute a block of code repeadetly until certian condition is meet.
# In python, 2 main loops i.e the for loop and the while loop

# python for loop. below sytax
"""
for variable in range(n):
    block of code to be executed
"""

for greeting in range(5):
    print("Hello there", greeting)

print("==========================")
for number in range(10, 20):
    print(number)


print("============================")
# below we use some steps
for x in range(50, 71, 2):
    print(x)

print("=======================")
# Create a program that is able to print  all the odd numbers between 0 and 51

for number in range(0, 52):
    if number % 2 != 0:
        print(number)