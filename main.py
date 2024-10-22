name = input("please enter name:")
for i in range(3):
    print(name)
name = input("please enter a name:")
for letter in name:
    print(letter)
#
number = int(input("enter a number between 1 and 12"))
for i in range(1,13):
    print(f"{number} * {i} = {number*i}")

name = input("enter a name:")
num =int(input("enter a number:"))
print(f"Hi,{name}, this is your name {num} times")
for i in range(num):
    print(name)

name = input("please enter a name")
num = int(input("enter a number between 1 to 5"))
for letter in range(num):
    for letter in name:
        print(letter)

