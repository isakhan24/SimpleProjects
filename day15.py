#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print(len(letters))
print(len(numbers))
print(len(symbols))
print("Welcome to the PyPassword Generator!")
user_letters = int(input("How many letters would you like in your password?\n"))
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for num in range(0, user_letters):
    password.append(letters[random.randint(0, 51)])

for num in range(0, user_numbers):
    password.append(numbers[random.randint(0,9)])

for num in range(0, user_symbols):
    password.append(symbols[random.randint(0, 8)])

random.shuffle(password)
final_p = ''

for x in password:
    final_p += x
print("Here is your password: " + final_p)