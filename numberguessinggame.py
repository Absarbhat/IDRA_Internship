import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

attempts = 7

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")
print("You have", attempts, "attempts.\n")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess < number:
        print("Too Low!")

    else:
        print("Too High!")

    attempts = attempts - 1
    print("Attempts left:", attempts)

if attempts == 0 and guess != number:
    print("Game Over!")
    print("The correct number was:", number)

print("Thank you for playing!")