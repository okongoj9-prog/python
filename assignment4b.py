#Functions Assignment 1. Create a Function to Find Simple Interest – PRT/100 2. Create a Function to Find Area of a Triangle – 1/2bh. – (With Parameters)
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    print("The simple interest is: ", interest, "Ksh")

simple_interest(50, 25, 13)

def area():
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    Area =  (base * height) /2
    print("The answer is: ", Area)

area()

print("===============")
def main():
    bases = int(input("Enter the base: "))
    heights = int(input("Enter the height: "))
    print("Area is", Triangle (bases, heights))

def Triangle (bases, heights):
    return ( bases * heights) /2

main()
