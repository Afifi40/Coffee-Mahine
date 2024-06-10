from CoffeeMachine import CoffeeMachine
if __name__ == '__main__':
    my_coffee_machine = CoffeeMachine(4.35)
    # print(list(data_stub.MENU.keys()))
    while True:
        chosen_drink = my_coffee_machine.prompt_user()
        if my_coffee_machine.resources_check(chosen_drink):
            coins = CoffeeMachine.enter_coins()
            if my_coffee_machine.process_transaction(coins, chosen_drink):
                my_coffee_machine.make_coffee(chosen_drink)
    # print("Program end")
