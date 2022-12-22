# Step 1
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_game = False
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)



display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

lives = 6

while not end_game:
    guess = input("Enter a letter: ").lower()
    for word in range(len(chosen_word)):
        letter = chosen_word[word]
        if letter == guess:
            display[word] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print(("You Lose"))


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You Win")

    print(stages[lives])