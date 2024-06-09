
import data_stub
data = data_stub


def print_report():
    print(f'Input Resources {data.resources}')
#   TODO 1 Prompt user, check what it'd like to order, show everytime order is completed, repeat.
#    The prompt "What would you like? (espresso/latte/cappuccino): "

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


if __name__ == '__main__':
    print_report()
    print("END")

