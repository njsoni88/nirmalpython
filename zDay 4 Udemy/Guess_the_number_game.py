from random import randint

guess = 0
secret_number = randint(1, 100)
estimation = 0
name = input("What is your name? ")

print(f"ok {name}, I have thought of a number between 1 and 100\n You have 8 attempts to guess the number.")

while guess < 8:
    estimation = int(input("what is the number?: "))
    guess += 1

    if estimation < secret_number:
        print("My number is higher")
    elif estimation > secret_number:
        print("My number is lower")
    else:
        print(f"congratulation {name}! you have gussed in {guess} attempts.")
        break

if estimation != secret_number:
    print(f"Sorry {name}, you have run out of attempts. The secret number was {secret_number}.")