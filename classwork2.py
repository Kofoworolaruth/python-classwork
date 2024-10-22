# num = int(input("enter a num below 50"))
# if num == 25:
#     print("your code is correct")
# elif num < 25:
#     print("out of range")
# else:
#     print("invalid input")

num = int(input("enter a below 50"))
print(f"countdown from 50 to {num}")
for i in range(50,num -1,-1):
    print(i, end=', ')
print(f"we have reached")

name = (input("enter a name"))
num =int(input("enter num"))
if num < 10:
    print(f"Hi,{name} this is your name {num} times")
    for num in range(num):
        print(name)
else:
    print("too high")

direction = input("do you want to count up or down: ").lower()

if direction == 'up':
    top = int(input("enter the top number: "))
    print(f"\n Counting up to {top}:")
    for i in range(top):
        print(i, end=", ")

elif direction == 'down':
    num = int(input("enter a number from 20 and below: "))
    # x = 20
    # while x >= 20:
    #     print(x)
    #     x -= 1
    print(f"Counting down from 20 to {num}")
    for i in range(20, num -1, -1):
        print(i, end=', ')
else:
    print("i don't understand")

        


# i = 0
# while i in range(top):
#     print(i)
#     i += 1

# elif direction == 'down':
#     num = input("enter a number below 20:")
#     print(f"\n Counting down from {num}")


