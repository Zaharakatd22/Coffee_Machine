# constants
WATERMACHIHE: int = 200
MILKMACHIHE: int = 50
BEANMACHINE: int = 15


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


print_current_status(begin_water, begin_milk, begin_beans, begin_disposable_cups, begin_money)


water_count: int = int(input("Write how many ml of water the coffee machine has: \n"
                             "> "))
milk_count: int = int(input("Write how many ml of milk the coffee machine has: \n"
                            "> "))
beans_count: int = int(input("Write how many grams of coffee beans the coffee machine has:: \n"
                             "> "))
cups_count: int = int(input("Write how many cups of coffee you will need:\n"
                            "> "))

possible_water: int = water_count // WATERMACHIHE
possible_milk: int = milk_count // MILKMACHIHE
possible_beans: int = beans_count // BEANMACHINE

possible_cups = min(possible_water, possible_milk, possible_beans)

if cups_count == possible_cups:
    print("Yes, I can make that amount of coffee")
elif cups_count < possible_cups:
    print(f"Yes, I can make that amount of coffee (and even {possible_cups - cups_count} more than that)")
else:
    print(f"No, I can make only {possible_cups} cups of coffee")
