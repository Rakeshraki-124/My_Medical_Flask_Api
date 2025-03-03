import sqlite3


def createTables():
    conn=sqlite3.connect("my_medicalshop.db")

######################### Table for Users #########################

    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id varchar(255),
                   name varchar(255),
                   email varchar(255),
                   phone_number varchar(255),
                   password varchar(255),
                   level int,
                   date_of_account_created date,
                   isApproved boolean,
                   block boolean,
                   pinCode varchar(255),
                   address varchar(255),
                   image_id varchar(255)


    );''')
 
 ####################### Table for Products #########################
 
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_id varchar(255),
                   product_name varchar(255),
                   price int,
                   stock int,
                   category varchar(255),
                   expiry_date date,
                   product_description varchar(255),
                   product_image_id varchar(255),
                   product_power varchar(255),
                   product_rating Double


    );''')
######################## Avaliable Product #########################

    # cursor = conn.cursor()
    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS Available_Products (
    #                id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                product_id varchar(255),
    #                product_name varchar(255),
    #                price int,
    #                stock int,
    #                category varchar(255),
    #                user_id (varchar(255),
    #                user_name varchar(255)
    # );''')
    

    
######################## Table for Orders #########################

    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   order_id varchar(255),
                   user_id varchar(255),
                   product_id varchar(255),
                   product_name varchar(255),
                   user_name varchar(255),
                   isApproved boolean,
                   quantity int,
                   price float,
                   total_price float,
                   subtotal_price varchar(255),
                   order_date date,
                   category varchar(255),
                   message varchar(255),
                   product_image_id varchar(255),
                   delivery_charge float,
                   tax_charge float,
                   user_address varchar(255),
                   user_pincode varchar(255),
                   user_mobile varchar(255),
                   user_email varchar(255),
                   order_status varchar(255),
                   order_cancel_status varchar(255),
                   user_street varchar(255),
                   user_city varchar(255),
                   user_state varchar(255),
                   discount_price varchar(255),
                   shipped_date varchar(255),
                   out_of_delivery_date varchar(255),
                   delivered_date varchar(255)


           

    );''')

######################## Sell & History #########################

    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sell_History (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   sell_id varchar(255),
                   user_id varchar(255),
                   product_id varchar(255),
                   product_name varchar(255),
                   user_name varchar(255),
                   quantity int,
                   price float,
                   total_price float,
                   sell_date date,
                   product_category varchar(255),
                   remaining_stock int
                  
                   

    );''')

    conn.commit()
    conn.close()


