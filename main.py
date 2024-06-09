from sys import exit

import data_stub
data = data_stub


def resources_check(drink: dict) -> bool:
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
        print("Not Enough" + depleted_resources + " Ask for Supervisor Refill")
    return is_enough

def print_report():
    print(f'Input Resources {data.resources}')


#   TODO 2 Turn off the Coffee machine by entering off to the prompt, code ends execution

#   TODO 3 Entering REPORT to the prompt should print resources report

#   TODO 4 Resources suffeciency check
#    When the user enters a drink the program should check if resoruces are enough
#    print "Sorry there is not enough water" if they aren't

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
            pass
        elif user_order == 'espresso':
            print(resources_check(data_stub.MENU['espresso']['ingredients']))
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

