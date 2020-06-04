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

# begin values
curr_water: int = 400
curr_milk: int = 540
curr_beans: int = 120
curr_disposable_cups: int = 9
curr_money: int = 550


def print_current_status(water_count: int,
                         milk_count: int,
                         beans_count: int,
                         disposable_cups_count: int,
                         money_count: int):
    print()  # separating newline
    print("The coffee machine has:")
    print(f"{water_count} of water")
    print(f"{milk_count} of milk")
    print(f"{beans_count} of coffee beans")
    print(f"{disposable_cups_count} of disposable cups")
    print(f"{money_count} of money")
    print()


def check_ingredients_amount(coffee: int) -> bool:
    if curr_disposable_cups > 0:
        if coffee == "1":
            possible_water: int = curr_water // WATER_ESPRESSO
            possible_milk: int = curr_milk // MILK_ESPRESSO
            possible_beans: int = curr_beans // BEANS_ESPRESSO

            possible_cups = min(possible_water, possible_milk, possible_beans)

            if possible_cups > 0:
                return True
            return False
        elif coffee == "2":
            possible_water: int = curr_water // WATER_LATTE
            possible_milk: int = curr_milk // MILK_LATTE
            possible_beans: int = curr_beans // BEANS_LATTE

            possible_cups = min(possible_water, possible_milk, possible_beans)

            if possible_cups > 0:
                return True
            return False
        else:  # == "3"
            possible_water: int = curr_water // WATER_CAPPUCCINO
            possible_milk: int = curr_milk // MILK_CAPPUCCINO
            possible_beans: int = curr_beans // BEANS_CAPPUCCINO

            possible_cups = min(possible_water, possible_milk, possible_beans)

            if possible_cups > 0:
                return True
            return False


def buy_coffee(coffee_type: int):
    global curr_water, curr_milk, curr_beans, curr_disposable_cups, curr_money

    if check_ingredients_amount(coffee_type):
        print("I have enough resources, making you a coffee!")

        if coffee_type == "1":
            curr_water -= WATER_ESPRESSO
            curr_milk -= MILK_ESPRESSO
            curr_beans -= BEANS_ESPRESSO
            curr_disposable_cups -= 1
            curr_money += MONEY_ESPRESSO
        elif coffee_type == "2":
            curr_water -= WATER_LATTE
            curr_milk -= MILK_LATTE
            curr_beans -= BEANS_LATTE
            curr_disposable_cups -= 1
            curr_money += MONEY_LATTE
        else:  # == "3"
            curr_water -= WATER_CAPPUCCINO
            curr_milk -= MILK_CAPPUCCINO
            curr_beans -= BEANS_CAPPUCCINO
            curr_disposable_cups -= 1
            curr_money += MONEY_CAPPUCCINO
    else:
        print("Sorry, not enough water!")


def fill_machine(add_water, add_milk, add_beans, add_disposable_cups):
    global curr_water, curr_milk, curr_beans, curr_disposable_cups, curr_money

    curr_water += add_water
    curr_milk += add_milk
    curr_beans += add_beans
    curr_disposable_cups += add_disposable_cups


def take_money():
    global curr_money

    print(f"I gave you ${curr_money}")
    curr_money = 0


while True:
    request: str = input("Write action (buy, fill, take, remaining, exit): \n"
                         "> ")

    if request == "buy":
        coffee_type_request: int = int(input("What do you want to buy? 1 - espresso, 2 - latte, "
                                             "3 - cappuccino, back - to main menu: \n "
                                             "> "))
        if coffee_type_request != "back":
            buy_coffee(coffee_type_request)
    elif request == "fill":
        count_add_water: int = int(input("Write how many ml of water do you want to add: \n"
                                         "> "))
        count_add_milk: int = int(input("Write how many ml of milk do you want to add: \n"
                                        "> "))
        count_add_beans: int = int(input("Write how many grams of coffee beans do you want to add: \n"
                                         "> "))
        count_add_cups: int = int(input("Write how many disposable cups of coffee do you want to add: \n"
                                        "> "))
        fill_machine(count_add_water, count_add_milk, count_add_beans, count_add_cups)
    elif request == "take":
        take_money()
    elif request == "remaining":
        print_current_status(curr_water,
                             curr_milk,
                             curr_beans,
                             curr_disposable_cups,
                             curr_money)
    elif request == "exit":
        break
    else:
        print("Please, print correct request!")
        print()
