cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
import time


def draw_card():
    return random.choice(cards)


def initial_draw():
    drawn_cards = []
    for card in range(0, 2):
        drawn_cards.append(draw_card())
    return drawn_cards


player_cards = initial_draw()
dealer_cards = initial_draw()


def sum_cards(card_list):
    if sum(card_list) <= 21:
        return sum(card_list)
    elif sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)
    else:
        return sum(card_list)


game_over = False
while not game_over:

    print(f"Your cards are {player_cards}. Sum = {sum_cards(player_cards)}")
    print(f"Dealer cards are {dealer_cards[0]} and x")

    if sum_cards(player_cards) == 21:
        print("You win!")
        game_over = True
        break
    elif sum_cards(player_cards) > 21:
        print("You lose!")
        game_over = True
        break
    else:
        while not game_over:
            user_choice = input("Do you want to hit another card? Y/N\t")

            if user_choice.lower() == "y":
                player_cards.append(draw_card())
                print(f"Your cards are {player_cards}. Sum = {sum_cards(player_cards)}")
                if sum_cards(player_cards) == 21:
                    print("You win!")
                    game_over = True
                    break
                elif sum_cards(player_cards) > 21:
                    print("You lose!")
                    game_over = True
                    break

            elif user_choice.lower() == "n":
                print(f"Dealer cards are {dealer_cards}. Sum = {sum_cards(dealer_cards)}")
                while sum_cards(dealer_cards) < 17:
                    dealer_cards.append(draw_card())
                    print("Dealer takes another card")
                    print(f"Dealer cards are {dealer_cards}. Sum = {sum_cards(dealer_cards)}")
                    if 21 >= sum_cards(dealer_cards) > sum_cards(player_cards):
                        print("You lose!")
                        game_over = True
                        break
                    elif sum_cards(dealer_cards) > 21:
                        print("You win!")
                        game_over = True
                        break
                    time.sleep(3)
                if sum_cards(dealer_cards) == sum_cards(player_cards):
                    print("It's a draw!")
                    game_over = True
                    break

                elif sum_cards(dealer_cards) < sum_cards(player_cards):
                    print("You win!")
                    game_over = True
                    break





