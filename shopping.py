# foods = []
# prices = []
# total = 0


# while True:
#     food = input("enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of the {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("----------Your cart-------------")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total += price

# print(f"Your total is: ${total}")

fruits =        ["banana", "apple", "oranges"]
vegetables =    ["calery", "carrotos", "potatoes"]
meats =         ["chicken", "fish", "turkey"]



groceries = [fruits, vegetables, meats]

for collection in groceries:
    for food in collection:
        print(food, end= " ")
    print()

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ('*',0, "#"))


for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()


    
