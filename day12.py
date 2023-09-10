#Number Guessing Game
import random

def main():

    def check_level():
        if level == "hard":
            return 5
        else:
            return 10

    def check_guess():
        if guess > secret_num:
            print("Too high.")
            return True
        elif guess < secret_num:
            print("Too low.")
            return True
        else:
            print("You win!")
            return False

    secret_num = random.randint(0, 100)
    print(f"I'm thinking of a number 1 to 100\nPsst the correct answer is {secret_num}")

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    lives = check_level()

    wrong = True
    while wrong:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        wrong = check_guess()

        if wrong == True:
            lives -= 1

        if lives == 0:
            wrong = False
            print("You've run out of guesses, you lose.")

    play_again = input("Would you like to play again? (y/n) ")

    if play_again == 'y':
        main()

main()
print("Thank you for playing the number guessing game.")