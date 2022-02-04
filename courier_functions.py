##not using this function, was just created at start, to input list in text file
def write_courier():
    our_courier = ['Jhon','Aron','William','David']
    write_file = open('courier.txt', 'w')
    for product in our_courier:
        write_file.write(product+ '\n','\n')
        print(product , '\n')
    write_file.close()

# printing data from the text file 
def print_courier(current_list):
    with open('courier.txt', 'r') as print_file:
        current_list = print_file.readlines()
        for each_line in current_list:
            print(current_list.index(each_line), '-----------------',each_line)
        print( '\n')

#### add a new courier  to the filwe
def add_courier(add_courier):
    add_file = open('courier.txt', 'a')
    add_file.write(add_courier)
    print(add_courier , '\n')
    add_file.close()
    #return add_courier

def read_courier():
    with open('courier.txt', "r") as read_file:
        get_content= read_file.readlines()
    
    print_courier(get_content)
    
    return get_content
    #print(get_content, '\n')


def update_courier():
    update_list = read_courier()

    print_courier(update_list)
    
    print('\n','Please enter a number for the product you want to update')
    item_index =int(input())
    print('Please enter a new courier name')
    item_str =input()
    update_list[int(item_index)] = item_str +'\n'
    with open ('courier.txt', 'w') as file:
        file.writelines(update_list)
        print('\n','Courier updated successfully', ' and new list is','\n')
        print_courier(update_list)
    file.close()


def delete_courier():
    with open('courier.txt', 'r') as file:
        data = file.readlines()
        print_courier(data)
        print('Please enter a number of the product, wich you want to delete:')
        delete_index = int(input())
        data.pop(delete_index)
    with open('courier.txt','w') as file:
        for item in data:
                file.write(item)
        print('Item deleted successfully')
    file.close()


