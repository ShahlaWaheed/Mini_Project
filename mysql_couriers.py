import pymysql
import os
from dotenv import load_dotenv
import re

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
def view_couriers():
    try:
        cursor.execute('SELECT courier_id, courier_name,courier_phone  FROM couriers')
        # Gets all rows from the table
        rows = cursor.fetchall()
        #print ("{:<8} {:<15} {:<10}".format('courier_id','courier_name','courier_phone_number'))
        print ("{:<15} {:<15} {:<15}".format('Courier_Id','Courier_Name','Courier_Mob'))

        for row in rows:

            print ("{:<15} {:<15} {:<15}".format(row[0],str(row[1]),str(row[2])))
        # cursor.close()
        # connection.close()
        return rows
    except:
       print ('Please enter valid input')

# Add code here to insert a new record
def add_courier_into_table():
# ###either this way to insert record
    try:
        print("Please enter new Courier name: ",'\n')
        courier_name = input()
        print("Please enter Contact Number of courier:  ",'\n')
        courier_mob = input()
        sql_add = "insert into couriers (courier_name ,courier_phone) VALUES (%s,%s)"
        values = (courier_name,courier_mob)
        cursor.execute(sql_add,values)

        print(sql_add)
        connection.commit()
        print(courier_name,' ',courier_mob,' ', 'added successfully and new list is: ')
        view_couriers()
        cursor.close()
        connection.close()
    except:
        print('Please enter valid input.')

def courier_update_table():
    try:
        view_couriers()
        update_list =[]
        my_sql = 'update couriers set '
        courier_id = int(input('Please enter Courier_id you want to update: '))
        courier_name = input('Please enter courier name you want to update (or press enter): ')
        #prod_price =float( input('Please enter Product price you want to update (or press enter): '))
        courier_mob =input('Please enter contact number you want to update (or press enter): ')

        if courier_name=='':
            pass
        else:
            my_sql =  my_sql + 'courier_name = %s '
            update_list.append(courier_name)
            if courier_name!='':
                if courier_mob!='':
                    my_sql= my_sql + ',' 

        if courier_mob=='':
            pass
        else:
            my_sql= my_sql + 'courier_phone = %s'
            update_list.append(courier_mob)
        my_sql =my_sql +  ' where courier_id = %s'
        update_list.append(courier_id)
        #cursor.execute(stripped_mysql, update_list)
        cursor.execute(my_sql,update_list)
        connection.commit()

        print("Courier's details updated successfully!:")
        view_couriers()
    except:
        print('Please enter valid input')
        #cursor.close()
        #connection.close()
def del_courier_from_table():
    try:
        view_couriers()
        courier_id =int(input('Please enter Courier_id you want to delete: '))
        print( 'Are you sure you want to delete this courier?' ,'\n')
        confirm_del =input ( 'Y to Delete or N  to Cancel: ')
        if confirm_del =='n' or confirm_del =='N':
            view_couriers()
            #pass
        elif confirm_del =='y' or confirm_del== 'Y':
            del_sql = 'DELETE FROM couriers where courier_id = %s'
            val = courier_id
            cursor.execute(del_sql,val)
            connection.commit()

        print('Courier deleted successfully')
        view_couriers()
    except:
        print('Please enter valid input')

    


#view_couriers()
#add_courier_into_table()
#courier_update_table()
#del_courier_from_table()
 
