age = int(input("What is your age? "))
if age < 10:
    print("You are in Primary Classes")
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

print("===================")

for year in range(2000, 2031):
    if year % 4 == 0:
        print(f"{year} is a leap year")


print("========================")

languages = ("Spanish", "Mandarin", "French",  "Arabic", "Hindi", "Russian", "Portuguese", "Bengali", "German")

for lang in languages:
    if lang == "English":
        print("English is found")
        break
else:
     print("English is not found")


print("================")

for number in range(0, 52):
    if number % 2 != 0:
        print(number)