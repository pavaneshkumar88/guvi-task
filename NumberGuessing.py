import random
r=random.randrange(1,100)
guess=int(input("Enter your guess between 1 to 100"))
for i in range(4):
    if guess>r:
        print("your guess is too high")
        print("try again")
        guess=int(input("Enter your guess"))
    else:
        print("your guess is to low")
        print("try again")
        guess=int(input("Enter your guess"))
print("hit!")
