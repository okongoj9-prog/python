 #Create a python program that is able to calculate the simple interest given the principle as 50000, rate as 5% and time as 8 years. SI = (p * R * t)/100



# Assignment
# 1. Write a python program that is able to calculate the BMI of a person whose weight is 78kgs and height is 1.75 meters. BMI = (weight) / (height squared)
# 2. Find the Area and perimeter of a rectangle whose length is 48cm and width is 25cm
# Research on python list, tuple and Dictionary Data types.

# Define the given values
principal = 50000
rate = 5
time = 8

# Calculate simple interest using the formula: SI = (P * R * T) / 100
simple_interest = (principal * rate * time) / 100

# Display the result
print(f"The Simple Interest is: {simple_interest}")

# Define the given values
weight = 78       # in kilograms
height = 1.75     # in meters

# Calculate BMI using the formula: BMI = weight / (height squared)
bmi = weight / (height ** 2)

# Display the result rounded to two decimal places
print(f"The BMI is: {bmi:.2f}")

# Define the given dimensions
length = 48  # in cm
width = 25   # in cm

# Calculate Area (Length * Width)
area = length * width

# Calculate Perimeter (2 * (Length + Width))
perimeter = 2 * (length + width)

# Display the results
print(f"The Area of the rectangle is: {area} cm²")
print(f"The Perimeter of the rectangle is: {perimeter} cm")


