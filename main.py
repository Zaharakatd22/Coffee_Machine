def main():
    class CoffeeMachine:
        # constants
        # type 1 (espresso)
        WATER_ESPRESSO: int = 250
        MILK_ESPRESSO: int = 0
        BEANS_ESPRESSO: int = 16
        MONEY_ESPRESSO: int = 4

        # type 2 (latte)
        WATER_LATTE: int = 350
        MILK_LATTE: int = 75
        BEANS_LATTE: int = 20
        MONEY_LATTE: int = 7

        # type 3 (cappuccino)
        WATER_CAPPUCCINO: int = 200
        MILK_CAPPUCCINO: int = 100
        BEANS_CAPPUCCINO: int = 12
        MONEY_CAPPUCCINO: int = 6

        def __init__(self, curr_water, curr_milk, curr_beans, curr_disposable_cups, curr_money):
            self.stage: str = "request"
            self.coffee_type: str = ""
            self.add_water: int = 0
            self.add_milk: int = 0
            self.add_beans: int = 0
            self.add_disposable_cups: int = 0
            self.curr_water: int = curr_water
            self.curr_milk: int = curr_milk
            self.curr_beans: int = curr_beans
            self.curr_disposable_cups: int = curr_disposable_cups
            self.curr_money: int = curr_money
            self.model = "Super-nano 209"

        def __repr__(self):
            return f"Coffee Machine runtime: stage - {self.stage}, coffee_type - {self.coffee_type};" \
                   f"Additional values: add_water - {self.add_water}, add_milk - {self.add_milk}," \
                   f" add_beans - {self.add_beans}," \
                   f" add_disposable_cups - {self.add_disposable_cups};" \
                   f"Current values: curr_water - {self.curr_water}, curr_milk - {self.curr_milk}," \
                   f" curr_beans - {self.curr_beans}, curr_disposable_cups - {self.curr_disposable_cups}," \
                   f" curr_money - {self.curr_money}."

        def __str__(self):
            return f"Coffee Machine '{self.model}' on stage {self.stage} with current count of ingredients: \n + " \
                   f"curr_water - {self.curr_water}, curr_milk - {self.curr_milk}," \
                   f" curr_beans - {self.curr_beans}, curr_disposable_cups - {self.curr_disposable_cups}," \
                   f" curr_money - {self.curr_money}."

        def processing_request(self, user_request, user_params):
            self.stage = user_request

            if self.stage == "buy":
                self.coffee_type = user_params[0]
                self.buy_coffee()
            elif self.stage == "fill":
                self.add_water = user_params[0]
                self.add_milk = user_params[1]
                self.add_beans = user_params[2]
                self.add_disposable_cups = user_params[3]
                self.fill_machine()
            elif self.stage == "take":
                self.take_money()
            elif self.stage == "remaining":
                self.print_current_status()

            self.stage = request

        def buy_coffee(self):

            if self.check_ingredients_amount():
                print("I have enough resources, making you a coffee!")
                print()

                if self.coffee_type == "1":
                    self.curr_water -= CoffeeMachine.WATER_ESPRESSO
                    self.curr_milk -= CoffeeMachine.MILK_ESPRESSO
                    self.curr_beans -= CoffeeMachine.BEANS_ESPRESSO
                    self.curr_disposable_cups -= 1
                    self.curr_money += CoffeeMachine.MONEY_ESPRESSO
                elif self.coffee_type == "2":
                    self.curr_water -= CoffeeMachine.WATER_LATTE
                    self.curr_milk -= CoffeeMachine.MILK_LATTE
                    self.curr_beans -= CoffeeMachine.BEANS_LATTE
                    self.curr_disposable_cups -= 1
                    self.curr_money += CoffeeMachine.MONEY_LATTE
                else:  # == 3
                    self.curr_water -= CoffeeMachine.WATER_CAPPUCCINO
                    self.curr_milk -= CoffeeMachine.MILK_CAPPUCCINO
                    self.curr_beans -= CoffeeMachine.BEANS_CAPPUCCINO
                    self.curr_disposable_cups -= 1
                    self.curr_money += CoffeeMachine.MONEY_CAPPUCCINO
            else:
                print("Sorry, not enough water!")
                print()

        def check_ingredients_amount(self) -> bool:
            if self.curr_disposable_cups > 0:
                if self.coffee_type == "1":
                    possible_water: int = self.curr_water // CoffeeMachine.WATER_ESPRESSO
                    possible_beans: int = self.curr_beans // CoffeeMachine.BEANS_ESPRESSO

                    possible_cups: int = min(possible_water, possible_beans)

                    if possible_cups > 0:
                        return True
                    return False
                elif self.coffee_type == "2":
                    possible_water: int = self.curr_water // CoffeeMachine.WATER_LATTE
                    possible_milk: int = self.curr_milk // CoffeeMachine.MILK_LATTE
                    possible_beans: int = self.curr_beans // CoffeeMachine.BEANS_LATTE

                    possible_cups: int = min(possible_water, possible_milk, possible_beans)

                    if possible_cups > 0:
                        return True
                    return False
                else:  # == "3"
                    possible_water: int = self.curr_water // CoffeeMachine.WATER_CAPPUCCINO
                    possible_milk: int = self.curr_milk // CoffeeMachine.MILK_CAPPUCCINO
                    possible_beans: int = self.curr_beans // CoffeeMachine.BEANS_CAPPUCCINO

                    possible_cups: int = min(possible_water, possible_milk, possible_beans)

                    if possible_cups > 0:
                        return True
                    return False

        def fill_machine(self):
            self.curr_water += self.add_water
            self.curr_milk += self.add_milk
            self.curr_beans += self.add_beans
            self.curr_disposable_cups += self.add_disposable_cups

        def take_money(self):
            print(f"I gave you ${self.curr_money}")
            self.curr_money = 0

        def print_current_status(self):
            print()  # separating newline
            print("The coffee machine has:")
            print(f"{self.curr_water} of water")
            print(f"{self.curr_milk} of milk")
            print(f"{self.curr_beans} of coffee beans")
            print(f"{self.curr_disposable_cups} of disposable cups")
            print(f"${self.curr_money} of money")
            print()

    params = []
    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

    print("*" * 15)

    # coffee machine interface runtime
    while True:
        request: str = input("Write action (buy, fill, take, remaining, exit): \n"
                             "> ")
        if request == "buy":
            print()
            coffee_type_request: str = input("What do you want to buy? 1 - espresso, 2 - latte, "
                                             "3 - cappuccino, back - to main menu: \n "
                                             "> ")
            params = [coffee_type_request]
            if coffee_type_request != "back":
                coffee_machine.processing_request(request, params)
        elif request == "fill":
            count_add_water: int = int(input("Write how many ml of water do you want to add: \n"
                                             "> "))
            count_add_milk: int = int(input("Write how many ml of milk do you want to add: \n"
                                            "> "))
            count_add_beans: int = int(input("Write how many grams of coffee beans do you want to add: \n"
                                             "> "))
            count_add_cups: int = int(input("Write how many disposable cups of coffee do you want to add: \n"
                                            "> "))
            params = [count_add_water, count_add_milk, count_add_beans, count_add_cups]

            coffee_machine.processing_request(request, params)
        elif request == "take":
            coffee_machine.processing_request(request, params)
        elif request == "remaining":
            coffee_machine.processing_request(request, params)
        elif request == "exit":
            break
        else:  # incorrect input
            print("Please, print correct request!")
            print()


if __name__ == "__main__":
    main()
