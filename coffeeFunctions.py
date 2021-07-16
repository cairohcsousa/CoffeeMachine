def print_report(resources_dict, cash):
    """
    Takes a dictionary with the amount of resources available and of cash that is in the machine and prints
    a report with these informations.
    :param resources_dict:
    :param cash:
    """
    water = resources_dict['water']
    milk = resources_dict['milk']
    coffee = resources_dict['coffee']

    print(f"Water : {water}ml")
    print(f"Milk : {milk}ml")
    print(f"Coffee : {coffee}g")
    print(f"Money: ${cash:.2f}")


def are_there_resources(resources_dict, type_of_coffee):
    """
    Takes a dictionary with the amount of resources available and the coffee to be made.
    Returns True if there's enough resources to make the coffee.
    Returns False otherwise.
    :param resources_dict:
    :param type_of_coffee:
    :return: boolean
    """
    from data import MENU

    for ingredient in MENU[type_of_coffee]['ingredients']:  # 'ingredient' is a string; loops through the keys
        if MENU[type_of_coffee]['ingredients'][ingredient] > resources_dict[ingredient]:
            print(f" Sorry. There is not enough {ingredient}")
            return False

    return True


def charge_refund(type_of_coffee):
    """
    Takes the selected coffee and asks the user for the money.
    Returns the amount that should go to the machine's cash
    :param type_of_coffee:
    :return: coffee_cost, if (money > coffee_cost); None, otherwise
    """
    from data import MENU
    coffee_cost = MENU[type_of_coffee]['cost']

    print("Please insert coins.")
    quarters = float(input("how many quarters?: ")) * 0.25
    dimes = float(input("how many dimes?: ")) * 0.1
    nickels = float(input("how many nickels?: ")) * 0.05
    pennies = float(input("how many pennies?: ")) * 0.01

    money = quarters + dimes + nickels + pennies

    if money < coffee_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return None  # That is, no money enters the machine
    else:
        print(f"Here is your ${(money-coffee_cost):.2f} in change.")
        return coffee_cost


def make_coffee(resources_dict, type_of_coffee):
    """
    Takes a dictionary with the amount of resources available and the coffee to be made.
    Returns the dictionary with the resources necessary for the coffee deducted.
    :param resources_dict:
    :param type_of_coffee:
    :return: resources_dict
    """
    from data import MENU

    for ingredient in MENU[type_of_coffee]['ingredients']:  # 'ingredient' is a string; loops through the keys
        resources_dict[ingredient] -= MENU[type_of_coffee]['ingredients'][ingredient]

    return resources_dict
