# Python While loop
# The while executes a piece of code until a condition is met. structure:

"""
intializing a variable with a valuie
while keywords follows
condition to be checked
statements to be printed out
lastly increment/decrement
"""

number = 0

while number <= 10:
    print(number)
    number = number +1


print("==============")
# below we print from a higher value to a lower value

y = 50

while y >=0:
    print(y)
    y =y - 1

# By use of a for loop , find all the leap years in between the year 2000 to 2030

'''
# Assignment: Create a tuple of languages with 10 international languages. If English is found on the tuple, terminate the loop and print("English is found") otherwise print("English is not found")

Modcom Learning 4:42 AM

# By use of a for loop, find all the leap years in between the year 2000 and 2030
when age is less than 10 the program should print “You are in Primary Classes” when age more 12 and less than 15 the program should print “You are in Junior Secondary” when age > 15 and less than 19 the program should print “You are in Senior Secondary” when age > 19 the program should print “You are
# create a program that is able to print all the odd numbers between 0 and 51
# Assignment: Create a tuple of languages with 10 international languages. If English is found on the tuple, terminate the loop and print("English is found") otherwise print("English is not found")
# By use of a for loop, find all the leap years in between the year 2000 and 2030
'''

for year in range(2000, 2031):
    if year % 4 == 0:
        print(f"{year} is a leap year")