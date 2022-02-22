import csv

# REUSABLE FUNCTIONS
def read_csv(file_name):
    data = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def write_csv(file_name, data):
    with open(file_name, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def update_order(orders):
    for index, order in enumerate(orders):
        print(index, order)

    chosen_order_index = int(input("pick an order: "))

    for index, status in enumerate(statuses):
        print(index, status)

    chosen_status_index = int(input("pick a status: "))

    orders[chosen_order_index]["status"] = statuses[chosen_status_index]

    return orders


# GLOBAL VARIABLES
products = ["coke", "fanta"]
couriers = ["john"]
statuses = ["preparing", "out-for-delivery", "delivered"]
orders = read_csv("new_order_dict.csv")


# App
update_order(orders)
write_csv("new_order_dict.csv", orders)