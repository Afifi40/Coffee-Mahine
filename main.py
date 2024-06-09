from sys import exit
from os import system
import data_stub
data = data_stub
money = 2.00


def print_report():
    """Entering REPORT to the prompt should print Water, Milk, and Coffee resources inside the machine"""
    print(f'Resources report:')
    print(f'Water   = {data.resources["water"]}')
    print(f'Milk    = {data.resources["milk"]}')
    print(f'Coffee  = {data.resources["coffee"]}')
    print("Money: $" + "{:.2f}".format(money))
    print()


def resources_check(drink: dict) -> bool:
    """ Check if Drink's required resources exist or not
:param drink: required resources for serving a specific drink
:type drink: dictionary
:returns True: if there are enough resources for that drink
    """
    depleted_resources = ' '
    is_enough = True
    if data.resources["milk"] < drink["milk"]:
        depleted_resources += 'milk,'
        is_enough = False
    if data.resources["water"] < drink['water']:
        depleted_resources += 'water, '
        is_enough = False
    if data.resources["coffee"] < drink['coffee']:
        depleted_resources += 'coffee, '
        is_enough = False
    if not depleted_resources.isspace():
        print("Sorry, There is Not Enough" + depleted_resources + " Ask for Supervisor Refill\n")
    return is_enough

#   TODO 7 Make Coffee
def prompt_user() -> str:
    """
Prompts user to enter his order.\
:returns "Drink_type": type of drink the user ordered"""
    while True:
        print("What would you like to order?")
        print("espresso     $1.50")
        print("latte        $2.50")
        print("cappuccino   $3.00")

        user_input = input().lower()
        if user_input == 'off':
            exit()
        elif user_input == 'report':
            print_report()
        elif user_input == 'espresso' or 'latte' or 'cappuccino':
            return user_input
        else:
            print("Wrong Entry, Try_Again\n\n")


def enter_coins() -> float:
    print("Please, enter coins (quarter/dime/nickle/pennie) in the form of ")
    print("(Q/D/N/P/E), Enter E when you're done ")

    entered_money = 0.00
    while True:
        coin = input().upper()
        if coin == 'Q':
            entered_money += 0.25
        elif coin == 'D':
            entered_money += 0.10
        elif coin == 'N':
            entered_money += 0.05
        elif coin == 'P':
            entered_money += 0.01
        elif coin == 'E':
            return round(entered_money, 2)
        print("Your Money = ", round(entered_money, 2))


def process_transaction(user_money: float, drink_cost: float) -> bool:
    global money
    change = user_money - drink_cost
    if change < 0:
        print(f"Sorry that's not enough money. {user_money} refunded.")
        return False
    else:
        print(f"Your order is being processed..., returning change, {change}...")
        money += drink_cost
        return True


def make_coffee(drink: str, ):
    drink_ingredients = data_stub.MENU[chosen_drink]['ingredients']
    data_stub.resources -= drink_ingredients
    print_report()
    print(f"Here is your {drink}. Enjoy!")


if __name__ == '__main__':
    while True:
        chosen_drink = prompt_user()
        is_enough_resources = False
        while not is_enough_resources:
            is_enough_resources = resources_check(data_stub.MENU[chosen_drink]['ingredients'])

        coins = enter_coins()

        is_enough_money = process_transaction(coins, data_stub.MENU[chosen_drink]['cost'])
        # drink_cost: float
        make_coffee(chosen_drink)
    print("Program end")

