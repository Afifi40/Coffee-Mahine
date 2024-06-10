from sys import exit
import data_stub


class CoffeMachine:
    MENU: dict
    resources: dict
    money: float

    def __init__(self,
                 initial_money: float = 2.00,
                 shop_menu: dict = data_stub.MENU,
                 machine_resources: dict = data_stub.resources):
        self.money = initial_money
        self.MENU = shop_menu
        self.resources = machine_resources

    def print_report(self):
        """Entering REPORT to the prompt should print Water, Milk, and Coffee resources inside the machine"""
        print(f'Resources report:')
        print(f'Water   = {self.resources["water"]}')
        print(f'Milk    = {self.resources["milk"]}')
        print(f'Coffee  = {self.resources["coffee"]}')
        print("Money: $" + "{:.2f}".format(self.money))
        print()

    def resources_check(self, drink: str) -> bool:
        """ Check if Drink's required resources exist or not
    :param drink: type of drink of which resources are to be checked
    :returns True: if there are enough resources for that drink
        """
        drink_ingredient = self.MENU[drink]['ingredients']
        depleted_resources = ' '
        is_enough = True
        if self.resources["milk"] < drink_ingredient["milk"]:
            depleted_resources += 'milk,'
            is_enough = False
        if self.resources["water"] < drink_ingredient['water']:
            depleted_resources += 'water, '
            is_enough = False
        if self.resources["coffee"] < drink_ingredient['coffee']:
            depleted_resources += 'coffee, '
            is_enough = False
        if not depleted_resources.isspace():
            print("Sorry, There is Not Enough" + depleted_resources + " Ask for Supervisor Refill\n")
        return is_enough

    def prompt_user(self) -> str:
        """
    Prompts user to enter his order.\
    :returns "Drink_type": type of drink the user ordered"""
        while True:
            print("What would you like to order?")
            for drink in self.MENU:
                disp_msg = str.ljust(drink, 15) + str(self.MENU[drink]['cost'])
                print(disp_msg)

            user_input = input()
            if user_input.isalpha():
                user_input = user_input.lower()

            if user_input == 'off':
                exit()
            elif user_input == 'report':
                self.print_report()
            elif data_stub.MENU.keys().__contains__(user_input):
                return user_input
            else:
                print("Wrong Entry, Try_Again\n\n")

    @staticmethod
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

    def process_transaction(self, user_money: float, drink: str) -> bool:
        drink_cost = self.MENU[drink]['cost']
        change = round(user_money - drink_cost, 2)
        if change < 0:
            print(f"Sorry that's not enough money. {user_money} refunded.")
            return False
        else:
            print(f"Your order is being processed..., returning change, {change}...")
            self.money += drink_cost
            return True

    def make_coffee(self, drink: str, ):
        drink_ingredients = self.MENU[drink]['ingredients']

        data_stub.resources["milk"] -= drink_ingredients["milk"]
        data_stub.resources["coffee"] -= drink_ingredients["coffee"]
        data_stub.resources["water"] -= drink_ingredients["water"]
        print(f"Here is your {drink}. Enjoy!")


if __name__ == '__main__':
    my_coffee_machine = CoffeMachine(4.35)
    # print(list(data_stub.MENU.keys()))
    while True:
        chosen_drink = my_coffee_machine.prompt_user()
        is_enough_resources = False
        while not is_enough_resources:
            is_enough_resources = my_coffee_machine.resources_check(chosen_drink)
        coins = CoffeMachine.enter_coins()
        is_enough_money = my_coffee_machine.process_transaction(coins, chosen_drink)
        # drink_cost: float
        my_coffee_machine.make_coffee(chosen_drink)
    # print("Program end")
