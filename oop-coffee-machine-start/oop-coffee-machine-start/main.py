from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
cash_register = MoneyMachine()

is_on = True
while is_on:
    print(f"Items on menu list : {menu.get_items()}")
    user_choice = input("Enter your choice: ")
    # print(f"user_choice = {user_choice}")

    if user_choice == "off":
        print("Maintenance team is now working on the machine")
        is_on = False
    elif user_choice == "report":
        coffee_machine.report()
        cash_register.report()
    elif user_choice == "espresso" or "latte" or "cappuccino":
        drink = menu.find_drink(user_choice)
        material_available = coffee_machine.is_resource_sufficient(drink)
        # print(material_available)   # for debug only
        if material_available:
            payment_done = cash_register.make_payment(drink.cost)
            # print(payment_done)
            if payment_done:
                cash_register.report()
                coffee_machine.make_coffee(drink)
    else:
        print("Invalid command, try again")

