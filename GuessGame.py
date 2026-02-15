import random

secret_no = random.randint(1, 100)
guess = 0

print("Welcome To Number Guessing Game")
print(" Guess a number between 1 and 100")

while guess  != secret_no:
    guess = int(input("Enter your Guess:"))

    if guess > secret_no:
        print("Too High!")
    elif guess < secret_no:
        print("Too Low!")
    else:
        print(" Correct! You guessed it!")