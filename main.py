from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
make_coffee = CoffeeMaker()
coins = MoneyMachine()


is_on = True

while is_on:

    order_name = input(f"What would you like? ({items.get_items()}): ")
    if order_name == "off":
        is_on = False
    elif order_name == "report":
        make_coffee.report()
        coins.report()
    else:
        drink = items.find_drink(order_name)
        is_sufficient = make_coffee.is_resource_sufficient(drink)
        if is_sufficient:
            is_transaction = coins.make_payment(drink.cost)
            if is_transaction:
              make_coffee.make_coffee(drink)








# 4. Check transaction successful?
# 5. Make Coffee.

