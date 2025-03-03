import sqlite3

def updateUsers(userID , **ketword):
    conn = sqlite3.connect('my_medicalshop.db')
    cursor = conn.cursor()
    
    for key, value in ketword.items():
        if key == "name":
            cursor.execute("UPDATE Users SET name =? WHERE user_id =?", (value, userID))
        elif key == "email":
            cursor.execute("UPDATE Users SET email =? WHERE user_id =?", (value, userID))
        elif key == "phone_number":
            cursor.execute("UPDATE Users SET phone_number =? WHERE user_id =?", (value, userID))
        elif key == "password":
            cursor.execute("UPDATE Users SET password =? WHERE user_id =?", (value, userID))
        elif key == "isApproved":
            cursor.execute("UPDATE Users SET isApproved =? WHERE user_id =?", (value,userID))
        elif key == "block":
            cursor.execute("UPDATE Users SET block =? WHERE user_id =?", (value,userID))
        elif key == "image_id":
            cursor.execute("UPDATE Users SET image_id =? WHERE user_id =?", (value, userID))

    conn.commit()
    conn.close() 
     
def updateProduct(productID, **ketword):
    conn = sqlite3.connect('my_medicalshop.db')
    cursor = conn.cursor()
    
    for key, value in ketword.items():


        if key == "name":
            cursor.execute("UPDATE Products SET name =? WHERE product_id =?", (value, productID))
        elif key == "price":
            cursor.execute("UPDATE Products SET price =? WHERE product_id =?", (value, productID))
        elif key == "stock":
            cursor.execute("UPDATE Products SET stock =? WHERE product_id =?", (value, productID))
        elif key == "category":
            cursor.execute("UPDATE Products SET category =? WHERE product_id =?", (value, productID))
        elif key == "expiry_date":
            cursor.execute("UPDATE Products SET expiry_date =? WHERE product_id =?", (value, productID))
        elif key == "product_rating":
            cursor.execute("UPDATE Products SET product_rating =? WHERE product_id =?", (value, productID))
        elif key == "product_description":
            cursor.execute("UPDATE Products SET product_description =? WHERE product_id =?", (value, productID))
        elif key == "product_power":
            cursor.execute("UPDATE Products SET product_power =? WHERE product_id =?", (value, productID))
        elif key == "product_image_id":
            cursor.execute("UPDATE Products SET product_image_id =? WHERE product_id =?", (value, productID))

    conn.commit()
    conn.close()

def updateOrders(orderID, **ketword):
    conn = sqlite3.connect('my_medicalshop.db')
    cursor = conn.cursor()
    
    for key, value in ketword.items():
       
        if key == "user_id":
            cursor.execute("UPDATE Orders SET user_id =? WHERE order_id =?", (value, orderID))
        elif key == "product_id":
            cursor.execute("UPDATE Orders SET product_id =? WHERE order_id =?", (value, orderID))
        elif key == "product_name":
            cursor.execute("UPDATE Orders SET product_name =? WHERE order_id =?", (value, orderID))
        elif key == "user_name":
            cursor.execute("UPDATE Orders SET user_name =? WHERE order_id =?", (value, orderID))
        elif key == "isApproved":
            cursor.execute("UPDATE Orders SET isApproved =? WHERE order_id =?", (value, orderID))
        elif key == "quantity":
            cursor.execute("UPDATE Orders SET quantity =? WHERE order_id =?", (value, orderID))
        elif key == "price":
            cursor.execute("UPDATE Orders SET price =? WHERE order_id =?", (value, orderID))
        elif key == "total_price":
            cursor.execute("UPDATE Orders SET total_price =? WHERE order_id =?", (value, orderID))
        elif key == "subtotal_price":
            cursor.execute("UPDATE Orders SET subtotal_price =? WHERE order_id =?", (value, orderID))
        elif key == "order_date":
            cursor.execute("UPDATE Orders SET order_date =? WHERE order_id =?", (value, orderID))
        elif key == "category":
            cursor.execute("UPDATE Orders SET category =? WHERE order_id =?", (value, orderID))
        elif key == "message":
            cursor.execute("UPDATE Orders SET message =? WHERE order_id =?", (value, orderID))
        elif key == "product_image_id":
            cursor.execute("UPDATE Orders SET product_image_id =? WHERE order_id =?", (value, orderID))
        elif key == "delivery_charge":
            cursor.execute("UPDATE Orders SET delivery_charge =? WHERE order_id =?", (value, orderID))
        elif key == "tax_charge":
            cursor.execute("UPDATE Orders SET tax_charge =? WHERE order_id =?", (value, orderID))
        elif key == "user_address":
            cursor.execute("UPDATE Orders SET user_address =? WHERE order_id =?", (value, orderID))
        elif key == "user_pincode":
            cursor.execute("UPDATE Orders SET user_pincode =? WHERE order_id =?", (value, orderID))
        elif key == "user_mobile":
            cursor.execute("UPDATE Orders SET user_mobile =? WHERE order_id =?", (value, orderID))
        elif key == "user_email":
            cursor.execute("UPDATE Orders SET user_email =? WHERE order_id =?", (value, orderID))
        elif key == "order_status":
            cursor.execute("UPDATE Orders SET order_status =? WHERE order_id =?", (value, orderID))
        elif key == "order_cancel_status":
            cursor.execute("UPDATE Orders SET order_cancel_status =? WHERE order_id =?", (value, orderID))
        elif key == "user_street":
            cursor.execute("UPDATE Orders SET user_street =? WHERE order_id =?", (value, orderID))
        elif key == "user_city":
            cursor.execute("UPDATE Orders SET user_city =? WHERE order_id =?", (value, orderID))
        elif key == "user_state":
            cursor.execute("UPDATE Orders SET user_state =? WHERE order_id =?", (value, orderID))
        elif key == "discount_price":
            cursor.execute("UPDATE Orders SET discount_price =? WHERE order_id =?", (value, orderID))
        elif key == "shipped_date":
            cursor.execute("UPDATE Orders SET shipped_date =? WHERE order_id =?", (value, orderID))
        elif key == "out_of_delivery_date":
            cursor.execute("UPDATE Orders SET out_of_delivery_date =? WHERE order_id =?", (value, orderID))
        elif key == "delivered_date":
            cursor.execute("UPDATE Orders SET delivered_date =? WHERE order_id =?", (value, orderID))

    conn.commit()
    conn.close()