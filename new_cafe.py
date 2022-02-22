from products_mysql import *
from mysql_couriers import *
from mysql_orders import*
import time
# welcoming Message

print("--------- Welcome to YOUR cafe! ---------")

#pause_1 = time.sleep(4)
#print('---------------------','Hi, Welcome to YOUR Cafe','---------------------')

while True:
    print("Please choose from the Options below:", '\n')
    print("0-------------------Exit.", '\n')
    print("1--------------Products Menu.", '\n')
    print("2----------------Couriers.", '\n')
    print("3----------------Order List.", '\n')

    exit_input = (input())
    # to caste it to int we can put   if int(exit_input)== 0:
    if exit_input== '0':
        print('Goodbye')
        break
    elif exit_input=='1':
        while True:
            print('0 ----------------Main Menu.', '\n')
            print('1 ----------- View the products Menu.','\n')
            print('2 ------------Add a product.', '\n')
            print('3 ---------- Update a product.', '\n')
            print('4-----------Delete a product', '\n')
            owner_input = input()
           #    # to caste it to int we can put   if int(owner_input)== 0:

            if owner_input== '0':
                print('What would you like to do?')
                break
            elif owner_input == '1': 
                view_products()
            elif owner_input=='2':
                add_product_into_table()
                view_products()

                            # updating a product

            elif owner_input == '3':
               product_update_table()
                
            # Delete a product
            elif owner_input == '4':

                del_product_from_table()

            else:
                print("Please make a valid choise")
               
                ##diplay courier options
    elif exit_input=='2':
        while True:
            print('0 --------------- View main menu.', '\n')
            print('1 ---------------View the Couriers.','\n')
            print('2 --------------Add an new courier.', '\n')
            print('3 ---------Update a courier name.', '\n')
            print('4 --------------- Delete a courier name', '\n')
            owner_input = input()
            if owner_input== '0':
                print('What would you like to do?')
                break
            elif owner_input == '1': 
                view_couriers()
                
               
            elif owner_input=='2':
               
                add_courier_into_table()
                view_couriers()

         # updating a product

            elif owner_input == '3':
               courier_update_table()
               view_couriers()
            
            # Delete a product
            elif owner_input == '4':
                del_courier_from_table()
    # orders dictionaries
    elif exit_input == '3':
        while True:
            print('0 ----------------Main Menu.','\n')
            print('1 ----------- View the Order List.','\n')
            print('2 ------------Add new Order.', '\n')
            print('3 ---------- Update order status.', '\n')
            print('4 ---------- Update Customer"s detail .', '\n')
            print('5-----------Delete an order', '\n')
            owner_input = input()
           #    # to caste it to int we can put   if int(owner_input)== 0:
            if owner_input== '0':
                print('Please choose an option?')
                break
            elif owner_input =='1':
                view_orders_from_table()
            elif owner_input =='2':
                add_order_into_table()
            elif owner_input =='3':
                view_orders_from_table()
                update_order_status()
                print('Order status changed')
            elif owner_input =='4':
                #update_order_table()
                pass

            elif owner_input == '5':
                del_order_from_table()

            else:
                print('Please make a valid choice')
    else:
        print("Please choose from the Options")

