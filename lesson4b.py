# Python function with parameters
# Parameters are values that mget pass as agument when you in invoke a function 

def greeting(name):
    print(f"Hello {name}. Hope you are doing fine?")

greeting("jane")
greeting("James")
greeting("Peter")
greeting("Miriam")

print("==================")

#below is an addition function that accepts 3 paremetres
def add(x, y ,z):
    sum = x + y +z
    print("The sum of the numbers is: ", sum)

#below  we invoke our function
add(45, 20, 15)
add(10, 15, 5)


print("=======================")
#By use of a function that accepts parametrs, calculate the speed of a vehicle which covered 400km in 5 hours time.
def speed(x,y):
    speeds = x/y
    print("The speed is: ", speeds, "km/h")
speed(400,5)