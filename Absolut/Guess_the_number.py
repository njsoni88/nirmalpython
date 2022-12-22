from random import randint

run_code_d = 5
run_code_e = 10


def check_answer(guess, computer_number, turns):
    if guess > computer_number:
        print("Too high")
        return turns - 1
    elif guess < computer_number:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it right. The correct number is {computer_number}.")


def set_difficulty():
    level = input("Choose the difficulty level. Type 'Easy' or 'Hard': ")
    if level == "easy":
        return run_code_e
    else:
        return run_code_d


# Allow the player to submit a guess for a number between 1 and 100.
def game():
    print("Welcome to the 'Number Guessing Game'!")
    print("Guess a number between 1 to 100 ")

    computer_number = randint(1, 100)
    # print(f"Computer chose {computer_number}")

    turns = set_difficulty()

    guess = 0
    while guess != computer_number:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Enter a number: "))
        turns = check_answer(guess, computer_number, turns)
        if turns == 0:
            print("You are out of attempts. You lose")
            print(f"The correct number was {computer_number}")
            return
        elif guess != computer_number:
            print("Guess again")


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
game()