# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")

WATERMACHIHE: int = 200
MILKMACHIHE: int = 50
BEANMACHINE: int = 15


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
