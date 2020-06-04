# constants
WATER_ESPRESSO: int = 250
MILK_ESPRESSO: int = 0
BEAN_ESPRESSO: int = 16
MONEY_ESPRESSO: int = 4

WATER_LATTE: int = 350
MILK_LATTE: int = 75
BEAN_LATTE: int = 20
MONEY_LATTE: int = 7

WATER_CAPPUCCINO: int = 200
MILK_CAPPUCCINO: int = 100
BEAN_CAPPUCCINO: int = 12
MONEY_CAPPUCCINO: int = 6

# begin values
begin_water: int = 400
begin_milk: int = 540
begin_beans: int = 120
begin_disposable_cups: int = 9
begin_money: int = 550


def print_current_status(curr_water: int,
                         curr_milk: int,
                         curr_beans: int,
                         curr_disposable_cups: int,
                         curr_money: int):
    print("The coffee machine has:")
    print(f"{curr_water} of water")
    print(f"{curr_milk} of milk")
    print(f"{curr_beans} of coffee beans")
    print(f"{curr_disposable_cups} of disposable cups")
    print(f"{curr_money} of money")
    print()


def buy_coffee():
    coffee_type: str = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n"
                             "> ")

    print_current_status(begin_water, begin_milk, begin_beans, begin_disposable_cups, begin_money)


def fill_machine():
    print_current_status(begin_water, begin_milk, begin_beans, begin_disposable_cups, begin_money)


def take_money():
    print_current_status(begin_water, begin_milk, begin_beans, begin_disposable_cups, begin_money)


print_current_status(begin_water, begin_milk, begin_beans, begin_disposable_cups, begin_money)

request: str = input("Write action (buy, fill, take): \n"
                     "> ")

if request == "buy":
    buy_coffee()
elif request == "fill":
    fill_machine()
else:  # == "take"
    take_money()

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
