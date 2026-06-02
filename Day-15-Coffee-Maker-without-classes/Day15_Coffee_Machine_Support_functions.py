import copy

# Function to calculate money
def calculate_money(money_dic):
    total_amount = 0
    for coin in money_dic:
        total_amount += money_dic[coin]['value'] * money_dic[coin]['qty']
    return round(total_amount,2)


# Function to process coins
def process_coins(money_sample_dic):
    user_money = copy.deepcopy(money_sample_dic)
    print('Please insert coins.')
    user_money['quarter']['qty'] = int(input('How many quarters?: '))
    user_money['dime']['qty'] = int(input('How many dimes?: '))
    user_money['nickle']['qty'] = int(input('How many nickles?: '))
    user_money['penny']['qty'] = int(input('How many pennies?: '))
    return user_money


# Function to add user money to the machine wallet
def add_money(machine_money, user_money):
    for coin in user_money:
        machine_money[coin]['qty'] += user_money[coin]['qty']
    return machine_money


# Function to process refund
def process_refund(machine_money, refund, money_sample_dic):
    refund_money_dic = copy.deepcopy(money_sample_dic)
    while refund > 0:
        for coin in refund_money_dic:
            if machine_money[coin]['qty'] > 0:
                refund_money_dic[coin]['qty'] = int(min(refund // refund_money_dic[coin]['value'], machine_money[coin]['qty']))
                refund -= refund_money_dic[coin]['qty'] * refund_money_dic[coin]['value']
                refund = round(refund,2)
                machine_money[coin]['qty'] -= refund_money_dic[coin]['qty']
            if refund <= 0.0000001:
                break
    return machine_money, refund_money_dic


# Function to generate report on available resources for the coffee machine
def generate_report(current_resources, resource_units, current_money):
    for resource in current_resources:
        print(f'{resource.capitalize()}: {current_resources[resource]}{resource_units[resource]}')
    print(f'Money: ${calculate_money(current_money)}')


# Function to check available resources against the user's choice of coffee
def check_resources(choice, current_resources, current_menu):
    for ingredient in current_menu[choice]['ingredients']:
        if current_resources[ingredient] < current_menu[choice]['ingredients'][ingredient]:
            print(f'Sorry, there is not enough {ingredient}.')
            return False
    return True


# Function to check if transaction is successful
def transaction_status(choice, user_amount, current_menu):
    refund = 0
    if user_amount > current_menu[choice]['cost']:
        refund = round(user_amount - current_menu[choice]['cost'], 2)
        return True, refund
    elif user_amount == current_menu[choice]['cost']:
        return True, refund
    else:
        print("Sorry that's not enough money. Money refunded")
        return False, user_amount


# Function to make coffee and deduct resources
def make_coffee(choice, current_resources, current_menu):
    for ingredient in current_menu[choice]['ingredients']:
        current_resources[ingredient] -= current_menu[choice]['ingredients'][ingredient]
    print(f"Here is your {choice}, Enjoy!")
