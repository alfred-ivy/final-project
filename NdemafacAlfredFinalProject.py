##Meal available
available_menus = ['Gari and Okra', 'jelof rice', 'Rice and beans', 'Salad', 'PBJ-sandwich', 'puff-puff and beans']
available_toppings = ['mushroom', 'onions', 'green pepper', 'extra Salad']
menu_prices = {'Gari and Okra': 5, 'jelof rice':9.8, 'Rice and beans': 7, 'Salad': 6, 'puff-puff and beans': 6.5}
topping_prices = {'mushroom':1, 'onions': 2, 'green pepper':3, 'extra Salad':4}
sub_total = []
final_order = {}
customer_adress = {}


#ordering a menu
print("welcome to Fred online restau  ordering and delivery service")
order_menu = True
while order_menu:    
    print("Please your item today's menu: ")
    print()
    for menus in available_menus:
        print(menus)
        print()
    while True:
        menu = input("which meal would you like to order? ")
        if menu in available_menus:
            print(f"You have ordered a {menu}.")
            sub_total.append(menu_prices[menu])
            break
        if menu not in available_menus:
            print(f"I am sorry, we currently do not have {menu}.")

    #asking for extra toppings
    order_topping = True
    print("This is the list of available extra toppings: ")
    for toppings in available_toppings:
        print(toppings)
        print()
    while order_topping:
        extra_topping = input("Would you like an extra topping? yes/no ")
        if extra_topping == "yes":
            topping = input("Which one would you like to add? ")
            if topping in available_toppings:
                final_order.setdefault(menu, [])
                final_order[menu].append(topping)
                print(f"I have added {topping}.")
                sub_total.append(topping_prices[topping])
            else:
                print(f"I am sorry, we don't have {topping} available.")

        elif extra_topping == "no":
            break
    extra_menu = input("Would you like to order another item from our menu? yes/no ")
    if extra_menu == "no":
        for key, value in final_order.items():
            print(f"\nYou have order a {key} menu with {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is this correct? yes/no ")
            if order_correct == "yes":
                check_order = False
                order_menu = False
            if order_correct == "no":
                print(final_order)
                add_remove = input("would you like to add or remove? yes/no ")
                if add_remove == "remove":
                    remove = input("Which menu would you like to remove yes/no?  ")
                    del final_order[remove]
                    print(final_order)
                if add_remove == "add":
                    check_order = False

#finalizing the order
print(f"\nYour total order price is: ${sum(sub_total)}")

print("Please provide us with your name, adress and phone number")
customer_adress['name'] = input("Enter your name ")
customer_adress['street_name'] = input("Enter your street address ")
customer_adress['zipcode'] = input("city and  zip code ")
customer_adress['phone number'] = input("Phone number ")
print()
print(f"Thank you for your order {customer_adress['name']}.")
print()
print("We will deliver your order to this adress ASAP")
print()
print(customer_adress['street_name'])
print(customer_adress['zipcode'])
print()
print(f"we will contact you on {customer_adress['phone number']} if anything comes up.")  
