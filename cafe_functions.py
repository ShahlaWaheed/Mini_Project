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
        print('\n')


def add_text_file(add_product):
    add_file = open('product_cafe.txt', 'a')
    add_file.write(add_product)
    print(add_product , '\n')
    add_file.close()
    
def read_text_file():
    with open('product_cafe.txt', "r") as read_file:
        get_content = read_file.readlines()
    print_list(get_content)
    return get_content

def update_text_file():
    #update_list will read and print the list from mentioned fuctions 
    update_list = read_text_file()
    #print('\n','Please enter a number for the product you want to update')
    print('Please enter a number for the product you want to update')
    item_index =int(input())
    print('Pleas enter a new product name')
    item_str =input()
    update_list[item_index] = item_str +'\n'
    with open ('product_cafe.txt', 'w') as file:
        file.writelines(update_list)
    print_list(update_list)

    file.close()
    print(' item has been updated successfully')


def delete_item():
    delete_product = read_text_file()
    print('Please enter a number of the product, which you want to delete: ')
    delete_index = int(input())
    delete_product.pop(delete_index)
    with open('product_cafe.txt','w') as file:
        for item in delete_product:
                file.write(item)
        print('Item deleted successfully')
    file.close()

