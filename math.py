

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

def main():
    x = int(input("What's x? "))
    print("X squared is", square(x))

def square(n):
    return pow(n, 2)

main()


for i in range(3):
    print("meow")


while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")