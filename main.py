# Imports
import data
import coffeeFunctions

machine_cash = 0.0  # initial cash

while True:
    selection = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == 'off':  # command to turn the machine off
        break
    if selection == 'report':
        coffeeFunctions.print_report(data.resources, machine_cash)
        continue
    elif selection in data.MENU:
        enough_resources = coffeeFunctions.are_there_resources(data.resources, selection)
    else:
        print(" Invalid option. Please try again.")
        continue

    if enough_resources is True:
        money_added = coffeeFunctions.charge_refund(selection)
        if money_added is None:  # i.e money is insufficient
            continue
        else:
            machine_cash += money_added
            data.resources = coffeeFunctions.make_coffee(data.resources, selection)
            print(f"Here is your {selection}. Enjoy!")
