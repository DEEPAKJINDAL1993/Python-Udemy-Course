import random
import os
from art import vs_logo, hl_logo
from game_data import data

def clear_console():
    print("\n" * 20)

# Random starting point in the data
length = len(data)
start_index = (random.randint(0, length))%length

# Initialize score to zero
score = 0
correct = True

# Print A and B
while correct:
    print(hl_logo)

    if score > 0:
        print(f"You're right! Current Score: {str(score)}")

    print(f'Compare A: {data[start_index]['name']}, a {data[start_index]['description']}, from {data[start_index]['country']}')
    print(vs_logo)
    print(f'Against B: {data[(start_index + 1)%length]['name']}, a {data[(start_index + 1)%length]['description']}, from {data[(start_index + 1)%length]['country']}')

    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if user_choice == 'A':
        if data[start_index]['follower_count'] > data[(start_index + 1)%length]['follower_count']:
            correct = True
        else:
            correct = False
    elif user_choice == 'B':
        if data[start_index]['follower_count'] < data[(start_index + 1)%length]['follower_count']:
            correct = True
        else:
            correct = False

    if correct:
        score += 1
        start_index = (start_index + 1) % length
        clear_console()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")


