# We use the for loop to loop through a list a tuple or even a dictionary

fruits = ["Banana", "Mango", "oranges", "Berries", ]
print(fruits)

print("=====================")
# Below we loop through our list as we print each item in the list
for fruit in fruits :
    print(fruit)

# Assignment create a tuple of languages with international languages. if english is found on 
# Assignment: Create a tuple of languages with 10 international languages. If English is found on the tuple, terminate the loop and print("English is found") otherwise print("English is not found")

languages = ("Spanish", "Mandarin", "French", "English", "Arabic", "Hindi", "Russian", "Portuguese", "Bengali", "German")

for lang in languages:
    if lang == "English":
        print("English is found")
        break
else:
     print("English is not found")
