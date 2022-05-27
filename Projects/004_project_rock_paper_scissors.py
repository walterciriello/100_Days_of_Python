#Game rock, paper, scissors
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)
list = ["ROCK", "PAPER", "SCISSORS"]

print(f"You chose {list[user_choice]}!")
print(f"Computer chose {list[computer_choice]}!")

if user_choice == 0:
    if computer_choice == 0:
        print("You tied!")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("You tied!")
    else:
        print("You lose!")
else:
    if computer_choice == 0:
        print("You lose!")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("You tied!")
