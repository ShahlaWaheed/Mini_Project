import csv
with open('order_dict.csv','r') as file:
    reader = csv.DictReader(file)
    
    # my_list = list(reader)
    # customer_name = my_list[3]
    # # #print('csv to list ', my_list)
    # # # for row in reader:
    # # #     print(row)
    # # order_status = my_list.index('status')
    # # print(order_status)
    # print(customer_name)