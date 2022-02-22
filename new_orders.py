import csv

#from couriers import read_file
from new_products import read_file
#     main_list = [
#     {
#     "customer_name": "John",
#     "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
#     "customer_phone": "0789887334",
#     "courier": 2,
#     "status": "preparing",
#     "items": [3,2,1]
#         },
#       {
#     "customer_name": "HAnia",
#     "customer_address": "new cross stree",
#     "customer_phone": "0789887334",
#     "courier": 1,
#     "status": "Preparing",
#      "items":[1,2,3]
    
#     },
#       {
#     "customer_name": "Aron",
#     "customer_address": "little horton lane",
#     "customer_phone": "0879494944",
#     "courier": 5,
#     "status": "Preparing",
#      "items":[1,2,3]
#     },
#       {
#     "customer_name": "Rania",
#     "customer_address": "boynton street",
#     "customer_phone": "00973=334",
#     "courier": 6,
#     "status": "Preparing",
#     "items":[1,2,3]
#     }
# ]

def read_order():
    #created an empty list as order_list
    order_list =[]
    try:
     with open ('new_order_dict.csv', 'r')as file:
         #reader is an object of csv dictwriter
         reader = csv.DictReader(file)
         order_list = list(reader)
         #print(order_list[1]['status'])
         print('List of orders is: ','\n')
         #print(order_list)
         for index_item in order_list:
             print(order_list.index(index_item),'---------->', index_item)
    except:
        print('File Not Found',' ')

    return order_list
    

#read_order()


    ##writing firsttime in a dict to a csv file
def dict_writer(file_name):
    new_dict = read_order()
    try:
        with open(file_name, 'w', newline='') as file:
          ## fields_names are csv file header(columns' name)
            field_names=['customer_name','customer_address',
                          'customer_phone', 'courier','status','items' 
                        ]
            writer = csv.DictWriter(file,fieldnames=field_names)
            #it will add first line to csv file
            writer.writeheader()
           #writerow function will add that one row to csv file
            writer.writerows(new_dict)
    except FileNotFoundError as fnf:
        print('File not found' ,' ', fnf)
dict_writer('new_order_dict')
        

def add_customer_detail():
    print("Please add Customer's detail below:")

    print("Please enter customer's name: ")
    customer_name = input()

    print("Please enter customer's address: ")
    customer_address = input()

    print("Please enter customer's Mobile number: ")
    customer_mob = input()
    #print product list here with it's index value from courier_functions
    product_list = read_file('products.csv')

    ####GET user inputs for comma-separated list of product index values

    product_order =[]
    user_input = input("Please enter number for customer's order values: ")
    print ("customer's order is :", user_input)
    new_list = user_input.split(",")
    for items in new_list:
            product_order.append(int(items))
    print(product_order)
#print courier list here with it's index value from courier_functions

    courier_list = read_file('couriers.csv')
    print('\n', "Please enter courier's Index: ")
    courier_ind = int(input())
    courier_name = courier_list[courier_ind]
    print(courier_name)

    order_status = 'Preparing'
    new_dict = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_mob,
        "courier": courier_ind,
        "status": order_status,
         "items": product_order
    }
    
    try:
        with open('new_order_dict.csv', 'a', newline='') as file:
            field_names=['customer_name','customer_address',
                          'customer_phone', 'courier','status','items'  
                          ]
            writer = csv.DictWriter(file,fieldnames=field_names)
            writer.writerow(new_dict)
            print(new_dict)
    except:
        print|('File not found')
#add_customer_detail()
def order_status():
    my_list =read_order()
    # for index_item in my_list:
    #     print(my_list.index(index_item), ' ', index_item)
    print('Please enter index value for order you want to update')
    user_input = int(input())
    print('Please update order status')
    col_status = input()
    my_list[user_input]['status'] =col_status
    print(user_input ,'--------', col_status)
    try:
       #rewritin file with updating status value
        with open('new_order_dict.csv','w', newline='') as file:
            field_names=['customer_name','customer_address',
                          'customer_phone', 'courier','status' ,'items'
                        ]
            writer = csv.DictWriter(file,fieldnames=field_names)
            writer.writeheader()
            writer.writerows(my_list)
            print(my_list)
    except FileNotFoundError as file_not_found:
        print('Sorry file nor found, please check file name/path', file_not_found)
    #return my_list

#order_status()

def update_order():
    new_list = read_order()
    index_input = int(input('Please choose a number(order you want to update?): '))
    input_name = input('What you want to do? change name? or press "enter" for no change: ')
    input_address=input('What you want to do? change address? or press "enter" for no change: ')
    input_phone = input('What you want to do? change mob number? or press "enter" for no change: ')
    input_courier = input('What you want to do? change courier? or press "enter" for no change: ')
    input_order = input('What you want to do? change order? or press "enter" for no change: ')

    if input_name !='':
        new_list[index_input]['customer_name'] =input_name
    if input_address !='':
        new_list[index_input]['customer_address'] =input_address
    if input_phone !='':
        new_list[index_input]['customer_phone'] = input_phone
    if input_courier !='':
        new_list[index_input]['courier'] = input_courier
    if input_order !='':
        new_list[index_input]['items'] = input_order
    try:
        with open('new_order_dict.csv','w',newline='') as file:
            my_field_names=['customer_name','customer_address',
                        'customer_phone', 'courier','status','items' ]
            dict_writer = csv.DictWriter(file,fieldnames=my_field_names)
            dict_writer.writeheader()
            dict_writer.writerows(new_list)
            print('New Updated list is: ', '\n')
            for index_item in new_list:
                print(new_list.index(index_item), '---', index_item)
    except FileNotFoundError as fnfe:
        print('File Not Found' ,' ',str(fnfe))
    
    
#update_order()
def order_delete():
    del_list = read_order()
    input_index = int(input('Please enter a number you wan t to delete: '))
    del_list.pop(input_index)
    try:
        with open('new_order_dict.csv','w',newline='') as file:
            my_field_names=['customer_name','customer_address',
                        'customer_phone', 'courier','status','items' ]
            dict_writer = csv.DictWriter(file,fieldnames=my_field_names)
            dict_writer.writeheader()
            dict_writer.writerows(del_list)
            print('New Updated list is: ', '\n')
            for index_item in del_list:
                print(del_list.index(index_item), '---', index_item)
    except FileNotFoundError as notfound:
        print('Unable to find file', ' ', str(notfound))
    return del_list

#order_delete()


