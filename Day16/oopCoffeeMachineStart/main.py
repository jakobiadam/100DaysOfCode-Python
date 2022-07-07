from os import system
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffeeMaker = CoffeeMaker()
    moneyMachine = MoneyMachine()
    reportResProfit = False

    while True:

        if reportResProfit:
            coffeeMaker.report()
            moneyMachine.report()
            reportResProfit = False

        drinkName = input(f"What would you like? ({menu.get_items()}):")

        if (drinkName == "off"): return

        if (drinkName == "clear"): system("clear")

        if (drinkName == "report"):
            coffeeMaker.report()
            continue

        drink = menu.find_drink(drinkName)

        if drink:
            if coffeeMaker.is_resource_sufficient(drink):
                print(f"The {drink.name}'s price is {drink.cost}.")
                if moneyMachine.make_payment(drink.cost):
                    coffeeMaker.make_coffee(drink)
                    reportResProfit = True

if __name__ == "__main__":
    main()
