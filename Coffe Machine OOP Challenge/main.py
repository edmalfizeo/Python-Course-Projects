from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
menu_item = MenuItem

should_End = True

while should_End:
    print("\nWelcome to Coffee Maker!")
    print("1 - See All The Items\n2 - Ask For a Coffe\n3 - Report Machine\n4 - Exit")
    user_choice = int(input("\nEnter your choice: "))
    if user_choice == 1:
        print(menu.get_items())
    if user_choice == 2:
        coffee = input("Enter the name of the coffee: ")
        drink = menu.find_drink(coffee)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    if user_choice == 3:
        print("")
        coffee_maker.report()
        money_machine.report()
    if user_choice == 4:
        should_End = False

