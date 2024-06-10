from CoffeeMachine import CoffeeMachine
if __name__ == '__main__':
    my_coffee_machine = CoffeeMachine(4.35)
    # print(list(data_stub.MENU.keys()))
    while True:
        chosen_drink = my_coffee_machine.prompt_user()
        is_enough_resources = my_coffee_machine.resources_check(chosen_drink)
        if is_enough_resources:
            coins = CoffeeMachine.enter_coins()
            is_enough_money = my_coffee_machine.process_transaction(coins, chosen_drink)
            # drink_cost: float
            my_coffee_machine.make_coffee(chosen_drink)
    # print("Program end")
