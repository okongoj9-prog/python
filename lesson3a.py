# comparision / Relation operators
# These are operators that used ro compare ?relate different condition and usually evaluate  to
# a boolean value (False/True)
# They are six in total i.e (> < >= <= !=)

print(5>2)
print(5<2)
print(5>=2)
print(5<=2)
print(5==2)
print(5!=5)

# Logcal operators
# Logical and - evalutes to true only if both or all of the condition are true
print((5<2) and (5<3))

# logical or
# logical or = this evalutres true if one of the statment /condition is true
print((5<2) or (5>3))

# logical not
# used to negate a condition (if the anser is true in turns out be false viceverse)
print(not(5>2))



print("======================")
# if... else conditional statment
# This is a conditional statement that is used to avaluate and if it is not, the if
# block execute otherwise the else gets ezacuted.

number = -10

if number > 0:
    print("The number is positive")
else:
    print("The number is negative")

print("==================")
# create a python program that is able to evaluater whether a number is an even ot an add number.


number2 = -12

if number2 % 2 == 0 :
    print(f"The {number2} number is even")
else:
    print(f"The {number2 } number is odd")

print("======================")

# If  ...elif ...else conditional statment.
# we use the above to evaluate multiple conditions

mynumber = 0
if mynumber > 0:
    print("The number is positive")
elif mynumber == 0:
    print("The number is zero")
else:
    print("The number is negative")

print("=========================")

# create a python program that is able to check based whether a person is eligable to vote or
# not . if he is eligable to vote print ("you can vote") else print ("You are not allowed
# to vote.") A person is eligible to vote if his/her age is above 18years

age = 4
if age >= 18:
    print("you can vote")
else:
    print("You are not allowed to vote.")