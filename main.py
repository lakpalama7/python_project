from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

coffee_machine=True

while coffee_machine:
   

    choice=input(f"What would you like ?({menu.get_items()}):").lower()
    
    if choice == 'off':
        coffee_machine=False
    elif choice =='report':
        coffee_maker.report()
        money_machine.report()
    else:
 
        choice_item=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(choice_item):
            if money_machine.make_payment(choice_item.cost):
                coffee_maker.make_coffee(choice_item)
   


