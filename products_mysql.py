import pymysql
import os
from dotenv import load_dotenv

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
def view_products():
    try:
        cursor.execute('SELECT product_id, product_name,product_price  FROM products')

        # Gets all rows from the result
        rows = cursor.fetchall()
        #print ("{:<8} {:<15} {:<10}".format('courier_id','courier_name','courier_phone_number'))
        print ("{:<15} {:<15} {:<15}".format('Product_Id','Product_Name','Product_Price'))

        for row in rows:

            print ("{:<15} {:<15} {:<15}".format(row[0],str(row[1]),str(row[2])))
        # cursor.close()
        # connection.close()
        return rows
    except:
        print('Please enter valid ID')

# Add code here to insert a new record
def add_product_into_table():
# ###either this way to insert record
    try:
        print("Please enter new product name: ",'\n')
        product_input = input()
        print("Please enter price for new product:  ",'\n')
        product_price = float(input())
        sql_add = "insert into products (product_name ,product_price) VALUES (%s,%s)"
        values = (product_input,product_price)
        cursor.execute(sql_add,values)

        print(sql_add)
        connection.commit()
        print(product_input,' added successfully and new list is: ')
        view_products()
        # cursor.close()
        # connection.close()
    except:
        print('Please enter valid input')

def product_update_table():
    try:
        view_products()
        my_list =[]
        my_sql = 'update products set '
        pro_id = int(input('Please enter Product_id you want to update: '))
        prod_name = input('Please enter Product name you want to update (or press enter): ')
        #prod_price =float( input('Please enter Product price you want to update (or press enter): '))
        prod_price =input('Please enter Product price you want to update (or press enter): ')

        if prod_name=='':
            pass
        else:
            my_sql=  my_sql + 'product_name = %s'
            my_list.append(prod_name)
            if prod_name!='':
                my_sql= my_sql  
                if prod_price!='':
                    my_sql = my_sql + ','
        
        if prod_price=='':
            pass
        else:
            my_sql= my_sql + 'product_price = %s '
            float(prod_price)
            my_list.append(prod_price)
        my_sql = my_sql + 'where product_id = %s'
        my_list.append(pro_id)
        print(my_sql)
        cursor.execute(my_sql, my_list)
        connection.commit()

        print('Product updated successfully:')
        view_products()
        # cursor.close()
        # connection.close()
    except:
         print('Please enter valid input')
def del_product_from_table():
    try:
        view_products()
        product_id =int(input('Please enter Product_id you want to delete: '))
        print( 'Are you sure you want to delete this courier?' ,'\n')
        confirm_del =input ( 'Y to Delete or N  to Cancel: ')
        if confirm_del =='n' or confirm_del =='N':
            view_products()
            #pass
        elif confirm_del =='y' or confirm_del== 'Y':
            del_sql = 'DELETE FROM products where product_id = %s'
            val = product_id
            cursor.execute(del_sql,val)
            connection.commit()

        print('Product deleted successfully')
        view_products()
    except:
        print('Please enter a valid input')


#view_products()
#add_product_into_table()
#product_update_table()
#del_product_from_table()
 
