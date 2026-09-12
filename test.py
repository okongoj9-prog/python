print("Hello")


# This is a comment

names =["Alice", "Bob", "Charles"]
scores = [95, 88, 91]

for name,scores in zip(names,scores):
    print(name, scores)


languages = ("Spanish", "Mandarin", "French", "English", "Arabic", "Hindi", "Russian", "Portuguese", "Bengali", "German")

for lang in languages :
    if lang == "English":
        print("English found")
else :
    print("English not found")


for lang in languages :
    if lang == "Spanish":
        print("Spanish found")
else :
    print("Spanish not found")

for lang in languages :
    if lang == "French":
        print("French found")
else :
    print("French  not found")

print("========================================")

for year in range(2000,2060):
    if year % 4 == 0:
       print(f"{year} is a leap year") 

print("========================================")
for year in range(2000,2063):
    if year % 4 == 0:
        print(f"{year} is a leap year")

print("==================================")


def add():
    number1 = 20
    number2 = 15
    sum = number1 + number2
    print("The sum is:", sum)

add()

print("======================================")
def subtract():
    num1 = 20
    num2 = 22
    subtract = num1 - num2
    print("The sub is:", subtract)

subtract()

def todolist():
    print("/n This is a todolist that help me achive my goals")
    print("1. view task")
    print("2. Add daily task")
    print("3. Update the task")
    print("4. Delete task")

def view_tasks(tasks):
    if not tasks:
        print("/n To do task empty!")
        return
    print("/n Your task")
    for index, task in enumerate(tasks, start=1):
        status ="done" if task["completed"] else "not done"
        print(f"{index}. [{status}] {task[title]}")












