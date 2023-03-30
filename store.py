from prettytable import PrettyTable


products = [
    {"Id":1, "Product Name": "Iphone 14", "Price": 400.00, "In Stock": 5},
    {"Id":2, "Product Name": "Hp Laptop", "Price": 250.00, "In Stock": 3},
    {"Id":3, "Product Name": "Table", "Price": 650.00, "In Stock": 3},
    {"Id":4, "Product Name": "Fan", "Price": 700.00, "In Stock": 6},
    {"Id":5, "Product Name": "Chair", "Price": 320.00, "In Stock": 4},
]

cart = []


def get_products():
    pretty_products = PrettyTable()
    pretty_products.title = "PRODUCTS AVAILABLE"
    pretty_products.field_names = ["ID", "Product Name", "Price(#)", "In Stock"]

    for items in products:
        pretty_products.add_row([items["Id"], items["Product Name"], items["Price"], items["In Stock"]])

    return pretty_products

def edit_products(id):
    products[id] = {}
    pass

def delete_products(id):
    products.pop(id)

def get_cart():
    
    total_amount = 0
    pretty_cart = PrettyTable()

    pretty_cart.title = "CART DETAILS"  
    pretty_cart.field_names = ["Quantity", "Product", "Price/Unit", "Amount"]
    
    for items in cart:
        total_amount += items["Amount"]
        pretty_cart.add_row([items["Quantity"], items["Product Name"], items["Price"], items["Amount"]])

    pretty_cart.add_row(["-----------","------------","-------------", "-------------"])
    pretty_cart.add_row(["","","Total Amount:","#{}".format(total_amount)])
    return pretty_cart