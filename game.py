
import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 5

print("==============================")
print("     NUMBER GUESSING GAME")
print("==============================")
print("Guess a number between 1 and 100")
print("You have only 5 chances!")

while attempts < max_attempts:

    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too Low! Try Again")

    elif guess > number:
        print("Too High! Try Again")

    else:
        print("Congratulations! You Won!")
        print("Correct Number:", number)
        print("Attempts:", attempts)
        break

    print("Chances left:", max_attempts - attempts)

else:
    print("Game Over!")
    print("The correct number was:", number)
