import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        print("two cards total is 21")
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        print("ace value from changed from 11 to 1")

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You Win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"

user_cards = []
computer_cards = []
game_over = False
for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    # user_cards.append(deal_card)
    computer_cards.append(deal_card())
    # print(f"this is user {user_cards}")
    # print(f"computer {computer_cards}")
def play_game():
    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" your cards: {user_cards} and current score: {user_score}")
        print(f" computer first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

print(f"   Your final cards: {user_cards}, final score: {user_score}")
print(f"   Computer final cards: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))

while input("Do you want to replay the game? 'y' or 'n") == 'y':
    play_game()