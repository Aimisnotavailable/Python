import os
import msvcrt
customer_name = "Customer"
menu = ["Adobo    ", "Igado    ", "Steak    ", "Porkchop ", "Menudo   ", "Caldereta", "Afritada "]
price =[100, 80, 130, 110, 100, 100, 100]
food_order = [0,0,0,0,0,0,0]
change = 0
balance = 0
confirmation_state = False
confrimation_state_input = False
input_type = [0,1,2]
maximum_order = 1000
maximum_money = 10000000

def food_menu():
    print("\t        WELCOME THIS IS OUR FOOD MENU")
    print("\t        Choose from the following code")
    for i in range(len(menu)):
        print("["+str(i+1)+"]",menu[i], end = "...................................")
        print(price[i])

def customer_order():
    response_type = ""
    print("Input code:", end = " ")
    response_type = input()
    return response_type

def user_food_quantity():
    food_quantity = ""
    print("How many orders would you like?:", end = " ")
    food_quantity = input()
    return food_quantity

def user_cash_input():
    user_cash = ""
    print("Cash: ", end = "")
    user_cash = input()
    return user_cash
    
def add_to_cart_prompt(response_type_initial = 0):
    response_type_initial -= 1
    print("You've just added", menu[response_type_initial],"\n"+"for", price[response_type_initial], "on to your cart")

def cart(quantity, response_type_initial):
    response_type_initial -=1
    food_order[response_type_initial] += quantity
    return food_order

def cost_of_food_receipt(food_order_checkout):
    os.system("cls")
    count = 0
    total_cost = 0
    cost = 0
    print("Item","                 Quantity")
    for i in food_order_checkout:
        if i != 0:
            print(menu[count],"---------------","x" + str(food_order_checkout[count]))
            cost = food_order_checkout[count] * price[count]
            total_cost += cost
        count +=1
    print("Total cost","               "+ str(total_cost))
    return total_cost

def user_payment(total_cost):
    user_cash  = [0]
    user_cash_state = 0
    error_type = 0
    change = 0
    user_cash_state = user_response_state(user_cash, input_type[2])
    if user_cash_state != 1:
        error_type = 0
        transaction_state(error_type)
    else:
        if int(user_cash[0]) >= total_cost:
            error_type = 2
            change = int(user_cash[0]) - total_cost
            transaction_state(change = int(user_cash[0]) - total_cost)
            return 1
    
        error_type = 1
        transaction_state(error_type)
    
def transaction_state(type = "2",*,change = 0):
    if type == 0:
        print("Invalid input")
        print("Transaction failed")
        print("Please press any key to exit")

    elif type == 1:
        print("You don't have enough money to continue the transaction", "you lack", (-1)*(change))
        print("Transaction failed")
        print("Please press any key to exit")
    
    else:
        print("User change is", change)
        print("Transaction success")
        print("Please press any key to exit")
    
    msvcrt.getch()

def input_verification(response_type = [], type = 0):
    response_check = ""
    if type == 0:
        for i in range(len(menu)):
            i+=1
            response_check = str(i)
            if(response_check == response_type[0]):
                return 1
        return 0
    elif type ==1:
        for i in range(1,maximum_order):
            response_check = str(i)
            if(response_check == response_type[0]):
                    return 1
        return 0
    elif type == 2:
        for i in range(1,maximum_money):
            response_check = str(i)
            if(response_check == response_type[0]):
                    return 1
        return 0
             
def confirmation():
    print("Do you wish to proceed to check out?")
    print("Press Y to proceed")
    confirmation_key_type = input()
    if(confirmation_key_type == 'Y' or confirmation_key_type =='y'):
        return True
    return False

def input_warning(response_type_final):
    if response_type_final != 1:
        print("Input is invalid please try again")
        print("Press any key to continue...")
        msvcrt.getch()
        os.system("cls")

def user_response(response_type_initial= [],type = 0):
    response_type_state = 0
    response_type_state = input_verification(response_type_initial,type)
    input_warning(response_type_state)
    return response_type_state

def user_response_state(response_type_initial = [0], type = 0):
    if type == 0:
        response_type_initial[0] = customer_order()
        response_type_state = user_response(response_type_initial, input_type[0])
        return response_type_state
    elif type == 1:
        response_type_initial[0] = user_food_quantity()
        response_type_state = user_response(response_type_initial, input_type[1])
        return response_type_state
    elif type == 2:
        response_type_initial[0] = user_cash_input()
        response_type_state = user_response(response_type_initial, input_type[2])
        return response_type_state

def main_menu():
    confirmation_key = False
    food_order = [0,0,0,0,0,0,0]
    total_cost = 0
    transaction_state = 0
    while not confirmation_key:
        os.system("cls")
        confirmation_key = False
        food_type = [0]
        food_type_state = 0
        food_quantity = [0]
        food_quantity_state = 0
        while food_type_state == 0 or food_quantity_state == 0:
            food_menu()
            food_type_state = user_response_state(food_type, input_type[0])
            if food_type_state == 0:
                continue
            food_quantity_state = user_response_state(food_quantity, input_type[1])
        food_order = cart(int(food_quantity[0]),int(food_type[0]))
        add_to_cart_prompt(int(food_type[0]))
        confirmation_key = confirmation()
    total_cost = cost_of_food_receipt(food_order)
    user_payment(int(total_cost))

main_menu()
