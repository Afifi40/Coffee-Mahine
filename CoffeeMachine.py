from sys import exit
import data_stub

COIN_TYPES = {"Q": 0.25, "D": 0.1, "N": 0.05, "P": 0.01, }
class CoffeeMachine:
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
        for drink_resource in self.resources:
            disp_msg = str.ljust(drink_resource, 10) + str(self.resources[drink_resource]) + "mL"
            print(disp_msg)
        print("Money:    $" + "{:.2f}".format(self.money))
        print()

    def resources_check(self, drink: str) -> bool:
        """ Check if Drink's required resources exist or not
    :param drink: type of drink of which resources are to be checked
    :returns True: if there are enough resources for that drink
        """
        drink_ingredient = self.MENU[drink]['ingredients']
        depleted_resources = ' '
        is_enough = True
        for drink_resource in self.resources:
            if self.resources[drink_resource] < drink_ingredient[drink_resource]:
                depleted_resources += drink_resource + ', '
                is_enough = False

        if not is_enough:
            print("Sorry, There is Not Enough" + depleted_resources + " Ask for Supervisor Refill\n")
        return is_enough

    def prompt_user(self) -> str:
        """
    Prompts user to enter his order.\
    :returns "Drink_type": type of drink the user ordered"""
        while True:
            print("What would you like to order?")
            for menu_drink in self.MENU:
                disp_msg = str.ljust(menu_drink, 15) + str(self.MENU[menu_drink]['cost'])
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
        entered_money = 0.00
        print("Please, enter coins (quarter/dime/nickle/pennie) in the form of ")
        print("(Q/D/N/P)")

        while True:
            coin = input().upper()
            if coin not in COIN_TYPES:
                return round(entered_money, 2)
            else:
                entered_money += COIN_TYPES[coin]
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
        for drink_resource in self.resources:
            self.resources[drink_resource] -= drink_ingredients[drink_resource]
        print(f"Here is your {drink}. Enjoy!")

