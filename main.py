# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")


print("Write how many cups of coffee you will need:")
cups_count = int(input("> "))

water_count = cups_count * 200
milk_count = cups_count * 50
beans_count = cups_count * 15

print("For {} cups of coffee you will need: ".format(cups_count))
print("{} ml of water".format(water_count))
print("{} ml of milk".format(milk_count))
print("{} g of coffee beans".format(beans_count))
