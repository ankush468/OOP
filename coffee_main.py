from coffee_menu import MENU
from coffee_menu import resources
from coffee_oop import Coffee 


is_on = True 

while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'off':
      is_on = False

    elif choice == 'report':
       print(f'water {resources['water']}ml')
       print(f'milk {resources['milk']}ml')
       print(f'coffee {resources['coffee']}ml')


    elif choice in ['espresso', 'latte', 'cappuccino']:
          # check if we have resources to make coffee

          drink = MENU[choice]
          resources_check_data = Coffee(resources ,drink) # initilize coffee class
          resources_status = resources_check_data.check_resources() # check resources
          print(resources_status)

          # process coin if we have resources
          if resources_status == True:
              quarters = int(input("Please enter number of quarters ")) * 0.25
              dimes = int(input ("Please enter number of dimes ")) * 0.10
              nickles = int(input ("Please enter number of nickles ")) * 0.05
              pennies = int(input ("Please enter number of pennies ") )* 0.01

              cost_of_coffee = MENU[choice]['cost']
              coin_added_by_customer = quarters + dimes + nickles + pennies

              check_sufficient_money = resources_check_data.calculate_coin_value(cost_of_coffee,coin_added_by_customer) # check if you have enough money to buy
              print(check_sufficient_money)

              if check_sufficient_money == True:
                  resources_left =  resources_check_data.resources_left() # deduct the resources from main resource
                  print(f"here is your {choice} enjoy your coffee")