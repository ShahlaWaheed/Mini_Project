##not using this function, was just created at start, to input list in text file
def write_text_file():
    our_menu = ['Espresso','Coffee Latte','Cappuccino','Tea']
    write_file = open('product_cafe.txt', 'w')
    for product in our_menu:
        write_file.write(product+ '\n','\n')
        print(product , '\n')
    #write_file.close()

# printing data from the text file 
def print_list(current_list):
    with open('product_cafe.txt', 'r') as print_file:
        current_list = print_file.readlines()
        for each_line in current_list:
            print(current_list.index(each_line), '-----------------',each_line)
        print('----------------------------------------------------------', '\n')


def add_text_file(add_product):
    add_file = open('product_cafe.txt', 'a')
    add_file.write(add_product)
    print(add_product , '\n')
    add_file.close()
    #return update_product

def read_text_file(get_content):
    read_file = open('product_cafe.txt', "r")
    get_content= read_file.read()
    print_list(get_content)
    #print(get_content, '\n')

#read_text_file()
def update_text_file():
    #update_list = read_text_file('product_cafe.txt')

    with open('product_cafe.txt','r') as file:
        update_list = file.readlines()
        for each_product in update_list:
            index1 = update_list.index(each_product)
            print(index1,'-----------', each_product)
    #print_list(update_list)
    print('Please enter a number for the product you want to update')
    item_index =int(input())
    print('Pleas enter a new product name')
    item_str =input()
    update_list[item_index] = item_str +'\n'
    with open ('product_cafe.txt', 'w') as file:
        file.writelines(update_list)

        file.close()
    print(' item has been updated successfully')


def delete_item():
    with open('product_cafe.txt', 'r') as file:
        data = file.readlines()
        print_list(data)
        print('Please enter a number of the product, wich you want to delete:')
        delete_index = int(input())
        data.pop(delete_index)
    with open('product_cafe.txt','w') as file:
        for item in data:
                file.write(item)
        print('Item deleted successfully')
    file.close()

