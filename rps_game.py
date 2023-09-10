#Rock Paper Scissors Game
import random

user_win = False

rock = "R"
paper = "P"
scissors = "S"

user_choice = int (input("Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computer_choice = random.randint(0, 2)

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if user_choice == computer_choice:
    print("\nTie Game")
elif user_choice == 1 and computer_choice == 0 or user_choice == 0 and computer_choice == 2 \
        or user_choice == 2 and computer_choice == 1:
    user_win = True
else:
    user_win = False

if user_choice != computer_choice:
    if user_win == True:
        print("You win.")
    else:
        print("You lose.")
