import csv

##reading from the file
def read_file(file_name):
    courier_list = []
    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            courier_list = list(reader)
            for courier in courier_list:
                #product_list.append(courier)
                print(courier_list.index(courier),'-----',courier)
    except FileNotFoundError as fnfe:
        print('File not found', fnfe)
    return courier_list

#read_file('couriers.csv')


########Writing to produts.csv###########
def add_couriers(file_name):
    input_new_courier = input('Please enter new courier: ')
    input_phone = input('Enter Phone Number for the courier: ')

    new_record ={'courier_name': input_new_courier, 'phone_number':input_phone}
    ##adding courier to csv file:
    try:
        with open(file_name,'a',newline='') as file:
            headers =['courier_name','phone_number']
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow(new_record)
            print('Courier added successfully and new list is:','\n')
           # return new_record
    except:
        print('File not found')
def update_courier(file_name):
    
    #read_file('couriers.csv')

    my_list = read_file('couriers.csv')
    index_input = int(input('Please enter a number: '))
    input_courier_name = input('Please enter new courier name or press enter for no change: ')
    input_phone = input('Please enter new Phone number or press enter for no change: ')

    if input_courier_name != ''  :
        #print('Name was not changed', my_list)
        my_list[index_input]['courier_name']=input_courier_name

    if  input_phone != '':
        #print('Phone Number was not changed', my_list)
        my_list[index_input]['phone_number']=input_phone

   # else:

    try:
        with open(file_name,'w',newline='') as file:
            update_header = ['courier_name','phone_number']
            writer = csv.DictWriter(file,fieldnames=update_header)
            writer.writeheader()
            writer.writerows(my_list)
            print(my_list)
    except FileNotFoundError as fnf:
        print('File not found', fnf)
    return my_list

#############delete_product#############
def delete_courier(file_name):
    courier_list =read_file('couriers.csv')
    input_index = int(input('Please enter a number for courier you want to delete: '))
    courier_list.pop(input_index)
    
    try:
        with open(file_name,'w',newline='') as file:
            my_field_names=['courier_name','phone_number' ]
            dict_writer = csv.DictWriter(file,fieldnames=my_field_names)
            dict_writer.writeheader()
            dict_writer.writerows(courier_list)
            print('Courier deleted Successfully', '\n')
            print('New Courier list is: ', '\n', courier_list)
            
    except FileNotFoundError as notfound:
        print('Unable to find file', ' ', str(notfound))
    return courier_list





#############################---------function calling------####
#add_couriers('couriers.csv')
#update_courier('couriers.csv')
#delete_courier('couriers.csv')


#read_list = read_file('products.csv')








