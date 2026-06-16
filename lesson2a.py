# Boolean is a data type that evalutes true or false

israining = False
print(israining)
print(type(israining))

paidloan = True
print(paidloan)
print(type(paidloan))

# python list data type
# A list is a collection of iteams that are ordered in a certain way
# A list is introduced by use of []
# The iteams of a list are store insides of indexes. index strat from zero.
# A list is mutable.i.e the content can be changed

cars = ["BMW", "Benz", "Hiance", "Prado", "Probox", "Mclaren", "Ranger", "Rover"]
print(cars)
print(type(cars))

# accesing items of a list
# we use the index to id access items
print("The car on index zero is: ",cars[0])
print("The car on index five is: ",cars[5])

# List Slicing - this is creating a list from an already existing list
print(cars[4:])

# Example 2
print(cars[0:4])

# Example 3 - print from index 3 to 6
print(cars[3:7])

# List mutability
# we use the append function to add an item at the end of the list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

# we use the pop function to remove item on the list
cars.pop()
print(cars)

# we can replace an item on a certian index ass show below
cars[0] = "Pajero"
print(cars)

# below we use del function to delete an item in a certian index
del cars[4]
print(cars)

# checkout on remove ,sort function on lists