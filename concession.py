# Concessions stand programs

# dictionary {key: value}

menu = {"pizza": 3.00,
        "nachos": 3.55,
        "popcorn": 6.55,
        "fries": 3.67,
        "chips": 2.50,
        "pretzel": 4.90,
        "soda": 3.50,
        "Lemonade": 4.55,}

cart =[]
total= 0


print("--------------MENU-------------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------MENU------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------------YOUR ORDER ---------------")

for food in cart:
    total = total + menu.get(food)
    print(food, end=' ')

print()
print(f"Total is: ${total:.2f}")