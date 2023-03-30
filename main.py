import store
import send
import message as msg


def init():

    # view all available products
    all_products = store.get_products()
    print(all_products)

    while True:
        product_id = int(input("Enter the Product ID: "))

        if product_id == 0:
            break

        quantity = int(input("Enter quantity: "))
        sn = 1

        store.cart.append({
            "S/N": sn,
            "Product Name":  store.products[product_id]["Product Name"],
            "Quantity": quantity,
            "Price": store.products[product_id]["Price"],
            "Amount": quantity*store.products[product_id]["Price"]
        })

        sn += 1


    carts = store.get_cart()
    print(carts)

    response = input("Will you like to receive a copy into your email:\n Y: YES N: NO")
    if response.lower() == "y":

        email_receiver = input("Enter your email: ")
        sender_email = msg.SENDER_EMAIL
        sender_password = msg.SENDER_PASSWORD
        receiver_email = email_receiver
        subject = msg.SUBJECT
        body = msg.BODY.format("#1001",carts)
        send.send_email(sender_email,sender_password,receiver_email, subject, body)



if __name__ == "__main__":
    init()


