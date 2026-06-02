from Day15_Coffee_Machine_Support_functions import *
import copy

# Menu for coffee flavours with ingredients required
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Resources Dictionary
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Resource Units
resource_units = {
    "water": 'ml',
    "milk": 'ml',
    'coffee': 'g'
}


# Money blank Dictionary
money_sample_dic = {
    'quarter': {
        'value': 0.25,
        'qty': 0
    },
    'dime': {
        'value': 0.1,
        'qty': 0
    },
    'nickle': {
        'value': 0.05,
        'qty': 0
    },
    'penny': {
        'value': 0.01,
        'qty': 0
    }
}

# Coffee Machine money dictionary with 20 coins each
machine_money = copy.deepcopy(money_sample_dic)
for coin in machine_money:
    machine_money[coin]['qty'] = 20

# Testing
print("Machine money at the start")
print(machine_money)

customer_in_queue = True

while customer_in_queue:

    # Prompt user to ask for type of coffee
    choice = input(f"What would you like? ({'/'.join(MENU.keys())}): ").lower()

    if choice in MENU.keys():
        resource_check = check_resources(choice, resources, MENU)
        if resource_check:
            print(f"You need to pay ${MENU[choice]['cost']} for {choice}.")

            # Testing
            print("Machine money before user gave coins")
            print(machine_money)

            user_coins = process_coins(money_sample_dic)

            # Testing
            print("You gave these coins")
            print(user_coins)

            user_amount = calculate_money(user_coins)
            # Testing
            print(f"You paid ${user_amount}.")

            print("Machine money before transaction")
            print(machine_money)
            machine_money = add_money(machine_money, user_coins)
            print("Machine money after transaction")
            print(machine_money)

            trans_status, refund = transaction_status(choice, user_amount, MENU)
            # Testing
            print(f"Transaction status is {trans_status}")
            print(f"Refund is ${refund}.")

            if refund > 0:
                machine_money, refund_money_dic = process_refund(machine_money, refund, money_sample_dic)
                print(f"Here is ${refund} in change.")
                print(refund_money_dic)
            if trans_status:
                make_coffee(choice, resources, MENU)
    elif choice == 'report':
        generate_report(resources, resource_units, machine_money)
    elif choice == 'off':
        customer_in_queue = False
    else:
        print("Please enter a valid choice")
