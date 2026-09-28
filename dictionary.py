capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Kenya": "Nairobi"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("china"))

# if capitals.get("USA"):
#     print("That capital exists")
# else:
#     print("That capital does not exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "New Yock"})
# capitals.pop("china")
# capitals.popitem()
# capitals.clear()

# key = capitals.keys()

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
