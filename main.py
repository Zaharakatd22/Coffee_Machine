# constants
# type 1
WATER_ESPRESSO: int = 250
MILK_ESPRESSO: int = 0
BEANS_ESPRESSO: int = 16
MONEY_ESPRESSO: int = 4

# type 2
WATER_LATTE: int = 350
MILK_LATTE: int = 75
BEANS_LATTE: int = 20
MONEY_LATTE: int = 7

# type 3
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


def buy_coffee(coffee_type: int):
    global curr_water, curr_milk, curr_beans, curr_disposable_cups, curr_money

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
        coffee_type_request: str = input("What do you want to buy? 1 - espresso, 2 - latte, "
                                         "3 - cappuccino, back - to main menu: \n "
                                         "> ")
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
    else:  # == "exit"
        break

# water_count: int = int(input("Write how many ml of water the coffee machine has: \n"
#                              "> "))
# milk_count: int = int(input("Write how many ml of milk the coffee machine has: \n"
#                             "> "))
# beans_count: int = int(input("Write how many grams of coffee beans the coffee machine has:: \n"
#                              "> "))
# cups_count: int = int(input("Write how many cups of coffee you will need:\n"
#                             "> "))
#
# possible_water: int = water_count // WATERMACHIHE
# possible_milk: int = milk_count // MILKMACHIHE
# possible_beans: int = beans_count // BEANMACHINE
#
# possible_cups = min(possible_water, possible_milk, possible_beans)
#
# if cups_count == possible_cups:
#     print("Yes, I can make that amount of coffee")
# elif cups_count < possible_cups:
#     print(f"Yes, I can make that amount of coffee (and even {possible_cups - cups_count} more than that)")
# else:
#     print(f"No, I can make only {possible_cups} cups of coffee")
