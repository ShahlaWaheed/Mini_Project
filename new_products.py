import csv

##reading from the file
def read_file(file_name):
    product_list = []
    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            product_list = list(reader)
            for product in product_list:
                #product_list.append(product)
                print(product_list.index(product),'-----',product)
    except FileNotFoundError as fnfe:
        print('File not found', fnfe)
    return product_list

#read_file('products.csv')


########Writing to produts.csv###########
def add_products(file_name):
    input_new_product = input('Please enter new product: ')
    input_price = float(input('Enter the price for product: '))

    new_record ={'product_name': input_new_product, 'price':input_price}
    ##adding product to csv file:
    try:
        with open(file_name,'a',newline='') as file:
            headers =['product_name','price']
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow(new_record)
            print(input_new_product ,' added successfully and new list is:','\n')
            # read_file('products.csv')
    except:
        print('File not found')
def update_product(file_name):
    
   # read_file('products.csv')

    my_list = read_file('products.csv')
    index_input = int(input('Please enter a number: '))
    input_product_name = input('Please enter new product name or press enter for no change: ')
    input_product_price = input('Please enter new product price or press enter for no change: ')

    if input_product_name != ''  :
        my_list[index_input]['product_name']=input_product_name

        #print('Name was not changed', my_list)
    if  input_product_price != '':
        #print('Price was not changed', my_list)
        my_list[index_input]['price']=input_product_price


    #else:

    try:
        with open(file_name,'w',newline='') as file:
            update_header = ['product_name','price']
            writer = csv.DictWriter(file,fieldnames=update_header)
            writer.writeheader()
            writer.writerows(my_list)
            print('Product updated successfully')
            print(my_list)
    except:
        print('File not found')
    return my_list

#############delete_product#############
def delete_product(file_name):
    product_list =read_file('products.csv')
    input_index = int(input('Please enter a number for product you want to delete: '))
    product_list.pop(input_index)
    try:
        with open(file_name,'w',newline='') as file:
            my_field_names=['product_name','price' ]
            dict_writer = csv.DictWriter(file,fieldnames=my_field_names)
            dict_writer.writeheader()
            dict_writer.writerows(product_list)
            print('Product deleted successfully')
            print('New Updated list is: ', '\n', product_list)

    except FileNotFoundError as notfound:
        print('Unable to find file', ' ', str(notfound))
    return product_list





#############################---------function calling------####
#add_products('products.csv')
#update_product('products.csv')
#delete_product('products.csv')


#read_list = read_file('products.csv')








