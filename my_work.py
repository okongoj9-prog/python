# Example of a List
shopping_list = ["apples", "bananas", "milk"]
shopping_list.append("bread") 
print(shopping_list) # Output: ['apples', 'bananas', 'milk', 'bread']

# Example of a Tuple
gps_coordinates = (40.7128, -74.0060)
# gps_coordinates[0] = 41.0  --> This will trigger a TypeError!

# Example of a Dictionary
user_profile = {"username": "coder123", "joined": 2026, "active": True}
print(user_profile["username"]) # Output: coder123

a = "10"
b = "10"

answer = a + b
print(answer)


response = input("Would you like food? (N/Y): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")


age = input("Write your age? ")


if age < 10:
    print("“You are in Primary Classes”")
elif age > 12 and age <= 15:
    print("“You are in Junior Secondary”")
elif age > 15 and age <= 19:
    print("“You are in Senior Secondary”")
elif age > 15 and age <= 19:
    print("“You are in Senior Secondary”")
elif age >= 19:
    print("“You are in College”")
else:
    print("“You are in Transition Classes”")