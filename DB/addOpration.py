import sqlite3
import uuid
from datetime import date

######################### For Add Users #######################################
def createUser(name, email, password,pinCode,phoneNumber,address):

    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    user_id = str(uuid.uuid4())
    image_id = 'https://i.pinimg.com/736x/c0/74/9b/c0749b7cc401421662ae901ec8f9f660.jpg'

    date_of_account_created = date.today()

    cursor.execute('''
    INSERT INTO Users ( 
                   user_id, 
                   name,
                   email,
                   phone_number,
                   password,
                   level,
                   date_of_account_created,
                   isApproved,
                   block,
                   pinCode,                  
                   address,
                   image_id

    )
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    ''', (user_id, name, email, phoneNumber, password,1,date_of_account_created, 0,0,pinCode, address,image_id))

    conn.commit()
    conn.close()
    return user_id

########################## For Add Products ######################################

def addProduct(product_name,price,stock ,category,expiry_date,product_description,product_image_id,product_power,product_rating):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()
    product_id = str(uuid.uuid4())
    # expiry_date = date

    cursor.execute('''
    INSERT INTO Products ( 
                   product_id, 
                   product_name,
                   price,
                   stock,
                   category,
                   expiry_date,
                   product_description,
                   product_image_id,
                   product_power,
                   product_rating)

                   VALUES (?,?,?,?,?,?,?,?,?,?)
                   ''',(product_id,product_name,price,stock,category,expiry_date,product_description,product_image_id,product_power,product_rating))
    conn.commit()
    conn.close()
    return product_id

########################### For Add Orders #####################################

def addOrder(
    userID, 
    productID, 
    productName, 
    userName, 
    quantity, 
    price, 
    totalPrice, 
    subtotalPrice, 
    category, 
    message, 
    product_image_id, 
    delivery_charge, 
    tax_charge, 
    user_address, 
    user_pincode, 
    user_mobile, 
    user_email, 
    order_status, 
    order_cancel_status, 
    user_street, 
    user_city, 
    user_state, 
    discount_price, 
    shipped_date, 
    out_of_delivery_date, 
    delivered_date
):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    order_id = str(uuid.uuid4())
    order_date = date.today()

    cursor.execute('''
    INSERT INTO Orders (
        order_id,
        user_id,
        product_id,
        product_name,
        user_name,
        isApproved,
        quantity,
        price,
        total_price,
        subtotal_price,
        order_date,
        category,
        message,
        product_image_id,
        delivery_charge,
        tax_charge,
        user_address,
        user_pincode,
        user_mobile,
        user_email,
        order_status,
        order_cancel_status,
        user_street,
        user_city,
        user_state,
        discount_price,
        shipped_date,
        out_of_delivery_date,
        delivered_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
    ''', (
        order_id, 
        userID, 
        productID, 
        productName, 
        userName, 
        0,  # isApproved (default to 0)
        quantity, 
        price, 
        totalPrice, 
        subtotalPrice, 
        order_date, 
        category, 
        message, 
        product_image_id, 
        delivery_charge, 
        tax_charge, 
        user_address, 
        user_pincode, 
        user_mobile, 
        user_email, 
        order_status, 
        order_cancel_status, 
        user_street, 
        user_city, 
        user_state, 
        discount_price, 
        shipped_date, 
        out_of_delivery_date, 
        delivered_date
    ))

    conn.commit()
    conn.close()
    return order_id

###########################  sell & history #####################################

def sellHistory(userId, productId,userName ,productName,price,totalPrice,quantity,product_category,remainingStock):
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()

    sell_id = str(uuid.uuid4())
    sell_date = date.today()

    cursor.execute('''
    INSERT INTO Sell_History ( 
                   sell_id,
                   user_id,
                   user_name,
                   product_id,
                   product_name,
                   price,
                   total_price,
                   sell_date,
                   quantity,
                   product_category,
                   remaining_stock)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?)

                   ''',(sell_id,userId,userName,productId,productName,price,totalPrice, sell_date,quantity,product_category,remainingStock ))
    conn.commit()
    conn.close()
    return sell_id


                   