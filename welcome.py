# welcoming Message


print('Hi, Welcome to YOUR Cafe')
# read_file = open('products1.txt', "r")
# get_content= read_file.read()
# print(get_content)


our_menu = ['Espresso','Coffee Latte','Cappuccino','Tea']
# write_file = open("products.txt", "w")
# for product in our_menu:
#     write_file.write(product+ '\n')
# write_file.close()
while True:
    print("Please choose from the Options below")
    print("Press 0 to Exit")
    print("Press 1 to go to Main Menu")
    exit_input = (input())
    # to caste it to int we can put   if int(exit_input)== 0:
    if exit_input== '0':
        print('Goodbye')
        break
    elif exit_input=='1':
        while True:
            #print(our_menu)
            print('Please Enter 0 to Exit ')
            print('Please Enter 1 to view the Menu ')
            print('Please Enter 2 to add an Item to the Menu ')
            print('Please Enter 3 to update an Item.')
            print('Please Enter 4 to delete an Item')
            owner_input = input()
            #    # to caste it to int we can put   if int(owner_input)== 0:

            if owner_input== '0':
                print('will see you again')
                new_list = []
                
                break
            elif owner_input == '1': 
                print(our_menu)
                # creat a new product
            elif owner_input=='2':
                print('Hi, You can add new products to the List.')
                print('Please enter new product, you wish to add to the menu.')
                add_product = input()
                our_menu.append(add_product)
                print('You have added '+ add_product +' to the menu and new menu is:' )
                print(our_menu)

                            # updating a product

            elif owner_input == '3':
                for item in our_menu:
                    print(our_menu.index(item),'--------------', item)
                print('Please Enter a number to select a product to update')
                new_input_int = int(input())
                print('------------------')
                print('Please Enter new product name to update')
                input_str = input()
                our_menu[new_input_int] = input_str
                print(our_menu)

            # Delete a product
            elif owner_input == '4':
                for item1 in our_menu:
                    print(our_menu.index(item1),'--------------', item1)
                    print('----------------')
                print('\n' ,'Please enter a number for the product you want to delete')
                input_del = int(input())
                our_menu.pop(input_del)
                print(our_menu)
            else:
                print("Please make a valid choise")
                # print('Please Enter 0 to Exit ')
                # print('Please Enter 1 to view the Menu ')
                # print('Please Enter 2 to view the Menu ')
                # print('Please Enter 3 to update the Menu OR 0 to Exit')
                # print('Please Enter 4 to delete a product')
    else:
        print("Please Choose 0 to exit or 1 to View the menu")

