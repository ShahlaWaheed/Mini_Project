from msilib.schema import Error
import pymysql
import os
from dotenv import load_dotenv

from products_mysql import view_products
from mysql_couriers import view_couriers

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

def view_order_status():
    cursor.execute ('Select * from status_order')
    rows = cursor.fetchall()
    print ("{:<15} {:<15}".format('Status_Id','Status'))
    for row in rows:
        print("{:<15} {:<15}".format(row[0], str(row[1])))
    return rows
#view_order_status()
    
def view_orders_from_table():
    cursor.execute('''select orders.order_id, orders.customer_name,orders.customer_address,
                    orders.customer_phone,orders.courier_id,orders.status_id,
                    products.product_name
                    from orders
                    join products_orders on orders.order_id = products_orders.order_id
                    join products on products.product_id = products_orders.product_id       
                ''')

    # Gets all rows from the result
    rows = cursor.fetchall()
    #print ("{:<8} {:<15} {:<10}".format('courier_id','courier_name','courier_phone_number'))
    print ("{:<10} {:<15} {:<20}{:<15} {:<15} {:<12}{:<8}".format('Order_Id','Customer_Name','Customer_Address', 'Customer_Mob', 'Courier_ID','Status_ID','Product_Name'  ))

    for row in rows:

        print ('{:<10} {:<15} {:<20}{:<15} {:<15} {:<12}{:<8}'.format(row[0],str(row[1]),str(row[2]),str(row[3]),row[4], row[5], str(row[6])))
    # cursor.close()
    # connection.close()
    return rows
#view_orders_from_table()

#code here to insert a new record
def add_order_into_table():
    try:
        order_list= []
        customer_name = input("Please enter new Customer's name: ")
        order_list.append(customer_name)
        customer_address = input("Please enter Customer's address:  ")
        order_list.append(customer_address)
        customer_mob = input("Please enter Customer's contact number:  ")
        order_list.append(customer_mob)
        # couriers from couriers table
        view_couriers()
        courier_id =int(input("Please enter ID of the courier:  "))
        order_list.append(courier_id)

        view_order_status()

        print("Please enter Order Status ID:  ",'\n')
        order_status = int(input())
        order_list.append(order_status)
        # getting product list from products table
        view_products()

        sql_add_order = '''insert into orders (customer_name ,customer_address,
        customer_phone,courier_id,status_id) VALUES (%s,%s,%s,%s,%s)'''
        cursor.execute(sql_add_order,order_list)
        connection.commit()
        ##get id of last row added 
        last_inserted_id = cursor.lastrowid
        new_list = []
        order_item = input('Please enter order items: ')
        product_order = order_item.split(',')
        for item in product_order:
            new_list.append((last_inserted_id,item))
    # print(new_list)
        sql_one ='INSERT INTO products_orders (order_id,product_id) VALUES(%s,%s)'
        cursor.executemany(sql_one,new_list)
        connection.commit()

        print( 'Order added successfully and new list is: ')
        view_orders_from_table()
    except:
        print('Please enter a valid ID')
    
#add_order_into_table()

#     # cursor.close()
#     # connection.close()

def update_order_status():
    try:
        view_orders_from_table()

        order_input = input('Please enter Order id you want to change: ')
        view_order_status()

        update_input =input('Please enter Status id you want to change: ')
        sql_update= ("UPDATE orders SET status_id =%s where order_id = %s")
        value =(update_input,order_input)
        cursor.execute(sql_update,value)
        connection.commit()

        print("Order status updated successfully!:")
        view_orders_from_table
        # cursor.close()
        # connection.close()
    except:
        print('Please enter a valid ID')
#update_order_status()
    #view_couriers()
# #     #cursor.close()
# #     #connection.close()

def update_order_table():
    try:
        update_list =[]
        view_orders_from_table()
        order_input_two = int(input('Please enter Order id you want to change: '))
        customer_name = input("Please enter customer's name: ")#(or press enter for no change) :
        update_list.append(customer_name)
        customer_address = input("Please enter customer's address: ")#(or press enter for no change)
        update_list.append(customer_address)
        
        customer_mob = input("Please enter customer's mob number: ") #(or press enter for no change) 
       
        update_list.append(customer_mob)


        del_query = 'Delete from products_orders where order_id = %s'
        cursor.execute(del_query, order_input_two)
        
        connection.commit()
       
        view_products()
        sql_query = ('Select order_id from orders where order_id =%s')
        cursor.execute(sql_query,order_input_two)
        row = cursor.fetchone()
        print(row)

        customer_order = input("Please enter customer's products id (e.g 1,4,6,7): ")
        products =[]
        order_product =customer_order.split(',')
        for item in order_product:
            products.append((row,item))
        print(products)
        ##query to change product's id in orders_products table
        del_query = 'Delete from products_orders where order_id = %s'
        cursor.execute(del_query, order_input_two)
        connection.commit()
        insert_query= 'INSERT INTO products_orders (order_id,product_id) VALUES(%s,%s)'
        cursor.executemany(insert_query,products)
        connection.commit()


        
        view_couriers()
        courier_input = int(input("Please enter courier_ID: " ))#(or press enter for no change) :")

        update_list.append(courier_input)
        

        update_list.append(order_input_two)

        sql_query=('''update orders set customer_name = %s,
                        customer_address = %s,customer_phone=%s,
                        courier_id =%s 
                        where order_id = %s''')
        cursor.execute(sql_query,update_list)
        connection.commit()
        print('Order updated successfully')
        
        
        view_orders_from_table()


        ### products from products table
    except:
        print('Please insert a valid input')
update_order_table()





def del_order_from_table():
    view_orders_from_table()
    order_id =int(input('Please enter Order_id you want to delete: '))
    print( 'Are you sure you want to delete this courier?' ,'\n')
    confirm_del =input ( 'Y to Delete or N  to Cancel: ')
    if confirm_del =='n'or confirm_del=='N':
        view_orders_from_table()
        #pass
    if confirm_del =='y' or confirm_del=='Y':
        del_sql = 'DELETE FROM orders where order_id = %s'
        val = order_id
        cursor.execute(del_sql,val)
        connection.commit()

        print('Order deleted successfully')
        view_orders_from_table()

    
#del_order_from_table()
 
