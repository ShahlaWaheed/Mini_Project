from cafe_functions import *
from courier_functions import*
import time
####shutil module to display text in the middle of the terminal
import shutil
# welcoming Message
## get_terminal__size and display the text in the middle of the screen
center_text = shutil.get_terminal_size().columns
print("--------- Welcome to YOUR cafe! ---------".center(center_text))

pause = time.sleep(4)
#print('---------------------','Hi, Welcome to YOUR Cafe','---------------------')

while True:
    print("Please choose from the Options below:".center(center_text), '\n', '\n')
    print("0----------------- Exit.".center(center_text), '\n')
    print("1--------------Main Menu.".center(center_text), '\n')
    print("2----------------Courier.".center(center_text), '\n')

    exit_input = (input())
    # to caste it to int we can put   if int(exit_input)== 0:
    if exit_input== '0':
        print('Goodbye')
        break
    elif exit_input=='1':
        while True:
            print('0 --------------------Exit.'.center(center_text), '\n')
            print('1 ----------- View the Menu.'.center(center_text),'\n')
            print('2 ------------Add a product.'.center(center_text), '\n')
            print('3---------- Update a product.'.center(center_text), '\n')
            print('4-----------Delete a product'.center(center_text), '\n')
            owner_input = input()
           #    # to caste it to int we can put   if int(owner_input)== 0:

            if owner_input== '0':
                print('What would you like to do?'.center(center_text))
               # new_list = []
                break
            elif owner_input == '1': 
                read_file=''
                read_text_file(read_file)

            elif owner_input=='2':
                print(' You can add new products to the List.','\n')
                print('Please enter new product, you wish to add to the menu.','\n')
                add_product = input()
                products =add_text_file(add_product)
                print( add_product +' added successfully:'.center(center_text),'\n' )
            
                read_text_file(products)

                

                            # updating a product

            elif owner_input == '3':
               update_text_file()
                
            # Delete a product
            elif owner_input == '4':

                delete_item()
            else:
                print("Please make a valid choise")
                # print('Please Enter 0 to Exit ')
                # print('Please Enter 1 to view the Menu ')
                # print('Please Enter 2 to view the Menu ')
                # print('Please Enter 3 to update the Menu OR 0 to Exit')
                # print('Please Enter 4 to delete a product')

                ##diplay courier options
    elif exit_input=='2':
        while True:
            print('0 --------------- View main menu.'.center(center_text), '\n')
            print('1 ---------------View the Couriers.'.center(center_text),'\n')
            print('2 --------------Add an new courier.'.center(center_text), '\n')
            print('3----------Update a courier details.'.center(center_text), '\n')
            print('4----------------- Delete a courier'.center(center_text), '\n')
            owner_input = input()
            if owner_input== '0':
                print('What would you like to do?'.center(center_text))
                break
            elif owner_input == '1': 
                
                read_courier()
               
            elif owner_input=='2':
                print('Please enter courier, you wish to add to the menu.'.center(center_text),'\n')
                add_new_courier= input()
                courier =add_courier(add_new_courier)
                print( add_new_courier +' added successfully:'.center(center_text),'\n' )
                read_courier(courier)

         # updating a product

            elif owner_input == '3':
               update_courier()
            
            # Delete a product
            elif owner_input == '4':

                delete_courier()
    else:
        print("Please Choose 0 to exit or 1 to View the menu")

