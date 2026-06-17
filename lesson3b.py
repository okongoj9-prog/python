# Based on the  if ...elif ...else conditional statement , we can create the grading system as 
# show  belw

marks = 47

if marks > 0 and marks < 30 :
    print("Grade E")
elif marks >= 30 and marks <50 :
    print("Grade D")
elif marks >= 50 and marks <60 :
    print("Grade C")
elif marks >= 60 and marks <70 :
    print("Grade B")
elif marks >= 70 and marks <80 :
    print("Grade A")
else:
    print("Invalid entry. Please try agian...")

print("=====================")
# John wants to donate blood but there is a condition to check. A person who is able to donate blood is that who has ottained 50kgs or above and his age is not less than 18. Create a python program that is able to check whether John who has 57kgs and 26 years old is able to draw blood.

name = "John"
weight = 46
age = 26

if weight < 50:
    print("is not eligible. ")
elif age < 18:
    print("is not eligible.")
else:
    print("Eligible to donate blood.")
