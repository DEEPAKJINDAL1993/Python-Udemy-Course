from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Choosing a random number between 1 and 100
answer = random.randint(1, 100)


# Function to set guess count based on difficulty chosen by the user
def guess_counter():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty.lower() == "easy":
        return 10

    elif difficulty.lower() == "hard":
        return 5
    else:
        return 5
        # print("That's not a valid difficulty.")


# Function to compare the guess against the answer
def check_answer(guess, number):
    if guess == number:
        print(f"You got it! The answer was {number}.")
        return 1
    elif guess < number:
        print("Too low.")
        return 0
    elif guess > number:
        print("Too high.")
        return 0


# Assign guess count using difficulty level input using function
guess_count = guess_counter()


# Guessing the number using a loop
while guess_count > 0:
    print(f"You have {guess_count} guess remaining to guess the number.")
    guessed_number = int(input("Make a guess:  "))
    if check_answer(guessed_number, answer) == 1:
        break
    else:
        guess_count -= 1


# In case user use all the attempts, we will be showing the actual number
if guess_count == 0:
    print("You loose")
    print("The number was " + str(answer))
