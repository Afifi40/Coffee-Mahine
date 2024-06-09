from sys import exit

import data_stub
data = data_stub
money = 2.00


def print_report(profit: float):
    """Entering REPORT to the prompt should print Water, Milk, and Coffee resources inside the machine
    :param profit: Numerical representation of money collected by the machine"""
    print(f'Resources report:')
    print(f'Water   = {data.resources["water"]}')
    print(f'Milk    = {data.resources["milk"]}')
    print(f'Coffee  = {data.resources["coffee"]}')
    print("Money: $" + "{:.2f}".format(profit))
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


#   TODO 5 Prompt user to insert coins
#    Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#    calculate total value inserted on each coin insert

#   TODO 6 Check transaction success
#    if not enough money inserted print "Sorry that's not enough money. Money refunded"
#    if enough money is inserted, add cup profit to money in data_stub, return any extra money as change
#    The change should be rounded to 2 decimal places.

#   TODO 7 Make Coffee
def prompt_user():
    """ Prompt user, check what it'd like to order, show everytime order is completed, repeat.
        The prompt "What would you like? (espresso/latte/cappuccino): " """
    while True:
        print("What would you like? (espresso/latte/cappuccino): ")
        user_order = input().lower()
        if user_order == 'off':
            exit()
            pass
        elif user_order == 'report':
            print_report(money)
            pass
        elif user_order == 'espresso':
            resources_check(data_stub.MENU['espresso']['ingredients'])
        elif user_order == 'latte':
            resources_check(data_stub.MENU['latte']['ingredients'])
        elif user_order == 'cappuccino':
            resources_check(data_stub.MENU['cappuccino']['ingredients'])
        else:
            print("Wrong Entry, Try_Again\n\n")
        # complete order


if __name__ == '__main__':
    prompt_user()
    print("Program end")

