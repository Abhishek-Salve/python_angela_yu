# Virtual coffee machine

# coin options
PENNY_VALUE = 0.01    # 1 cent
NICKEL_VALUE = 0.05   # 5 cents
DIME_VALUE = 0.10     # 10 cents
QUARTER_VALUE = 0.25  #  25 cents

# menu pricing
ESPRESSO_PRICE = 1.50
LATTE_PRICE = 2.50
CAPPUCCINO_PRICE = 3.00

# default ingredients
DEFAULT_WATER = 300     # value in ml
DEFAULT_MILK = 200      # value in ml
DEFAULT_COFFEE_POWDER = 100     # value in grams (g)

# current ingredients
CURRENT_WATER = DEFAULT_WATER
CURRENT_MILK = DEFAULT_MILK
CURRENT_COFFEE_POWDER = DEFAULT_COFFEE_POWDER

MONEY_EARNED = 0.0

order_menu = [
    {
        "order" : "espresso",
        "water" : 50,
        "coffee" : 18,
        "milk" : 0,
        "price" : 1.50
    },
    {
        "order": "latte",
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price" : 2.50
    },
    {
        "order": "cappuccino",
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price" : 3.00
    }
]


def start_maintenance():
    print("Maintenance team is now working on the coffee machine")


def show_report():
    print("The current material availability are:")
    print(f"Water : {CURRENT_WATER} ml")
    print(f"Milk : {CURRENT_MILK} ml")
    print(f"Coffee : {CURRENT_COFFEE_POWDER} g")


def find_order_num_on_menu_list(user_order):
    for order_num in range(len(order_menu)):
        if order_menu[order_num]["order"] == user_order:
            return order_num


def check_materials(order_num):
    if CURRENT_MILK >= order_menu[order_num]["milk"]:
        if CURRENT_WATER >= order_menu[order_num]["water"]:
            if CURRENT_COFFEE_POWDER >= order_menu[order_num]["coffee"]:
                print("Sufficient materials available")  # for debug only
                return True
            else:
                print("Not sufficient coffee powder")
                return False
        else:
            print("Not sufficient water")
            return False
    else:
        print("Not sufficient milk")
        return False


def take_payment(order_num):
    global MONEY_EARNED

    print("Please insert coins")
    user_quarter = int(input("How many quarters: "))
    user_nickel = int(input("How many nickels: "))
    user_dime = int(input("How many dimes: "))
    user_penny = int(input("How many pennies: "))

    total_currency = (user_penny * PENNY_VALUE) + (user_nickel * NICKEL_VALUE) + (user_dime * DIME_VALUE) + (user_quarter * QUARTER_VALUE)
    currency_change = total_currency - order_menu[order_num]["price"]
    if currency_change >= 0:
        print(f"Change returned to user : {round(currency_change, 2)}")
        MONEY_EARNED += (total_currency - currency_change)
        return True
    else:
        print(f"There is not enough change, you gave ${round(total_currency, 2)}, required for current order is ${order_menu[order_num]["price"]}")
        return False


def process_order(order_num):
    global CURRENT_WATER, CURRENT_MILK, CURRENT_COFFEE_POWDER

    CURRENT_WATER -= order_menu[order_num]["water"]
    CURRENT_MILK -= order_menu[order_num]["milk"]
    CURRENT_COFFEE_POWDER -= order_menu[order_num]["coffee"]
    print(f"Order {order_menu[order_num]["order"]} is served ☕")



def ask_service():
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    print(f"User order is : {user_order}")
    if user_order == "off":
        start_maintenance()
        return False
    elif user_order == "report":
        show_report()
    # elif user_order == "espresso" or "latte" or"cappuccino":
    else:
        order_num = find_order_num_on_menu_list(user_order)
        # print(f"Order number for {user_order} = {order_num}")   # for debug only

        # Check if resources sufficient
        materials_available = check_materials(order_num)

        # Process coins
        if materials_available:
            payment_complete = take_payment(order_num)
            if not payment_complete:
                return True
            else:  # serve order
                process_order(order_num)
                print(f"Money earned = ${MONEY_EARNED}")
                return True
        else:
            print("There are not sufficient materials to process this order")
            show_report()
            return True


if __name__ == '__main__':
    ask_again = True
    while ask_again:
        ask_again = ask_service()


