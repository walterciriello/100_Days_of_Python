# Hangman

import random
from hangman_words_and_art import word_list, stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

# testing code
print(f'Pssst, the solution is {chosen_word}.')

# creating whitespace inside the list
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # checking if the chosen letter appears in the word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # warning that the chosen letter is not in the word and subtracting a life
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # joining all the elements of the list and transforming it into a string
    print(f"{' '.join(display)}")

    # Check if the user got all the letters right
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
