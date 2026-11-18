
import random

number = random.randint(1, 100)
attempts = 0

print("================================")
print("    NUMBER GUESSING GAME")
print("================================")

print("Guess a number between 1 and 100")

while True:

    guess = int(input("Enter your guess: "))

    attempts = attempts + 1

    if guess < number:
        print("Too Low! Try Again")

    elif guess > number:
        print("Too High! Try Again")

    else:
        print("Congratulations! You Won!")
        print("Correct Number:", number)
        print("Total Attempts:", attempts)
        break
