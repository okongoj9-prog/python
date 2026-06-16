# Dictinary Data type
# It store it data in form of key - valuespairs.
# Introduced by the use of {}
# Values can be stored inside of a dictionary can be of different type i.e int, tuple,
# string , list , dictionary
# N/B Unlike tuple/lists, on the dictionaries we normally usre the keys to access the values 
# The key and nthe values are separeted from each other by the use of full colon(:)
# End of each pair there should be a coma.


# example one:
phonebook = {
    "Benson" : 254743985,
    "Mary" : 254734732,
    "Joseph" : 254758243,
}

print("My dictionary is:", phonebook)
print(type(phonebook))

# Below we use the keys to access items of the dictionary

print(phonebook["Benson"])
print(phonebook["Mary"])

print("============================")

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["Miami", "PSG", "Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : (25756423, 3554443, 234234354)
    }

}

print("The name of  my player is:", player["name"])
print(player["teams"][2])
print(player["more"]["phone"][2])
