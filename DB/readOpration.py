import sqlite3


def dict_factory(cursor, row):
    d = {}
    if cursor.description is not None:
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
    return d


################################ Get all users ###############################
def getAllUsers():
    conn = sqlite3.connect("my_medicalshop.db")
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT * FROM Users
    """
    )

    users = cursor.fetchall()

    userJson = []
    for user in users:
        userJson.append(user)

        conn.close()
    return userJson

################################ Get Spacific users###############################
def getSpacificUser(userID):
    
    conn = sqlite3.connect("my_medicalshop.db")
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE user_id =?",(userID,))

    user = cursor.fetchone()
    

    conn.close()

    return user


################################ Get all Products #############################

def getAllProducts():
    conn = sqlite3.connect("my_medicalshop.db")
    conn.row_factory = dict_factory

    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT * FROM Products
    """
    )

    products = cursor.fetchall()

    productJson = []

    for product in products:
        productJson.append(product)

    conn.close()
    return productJson

################################ Get specific Products ########################

def getSpacificProduct(productId):
    conn=sqlite3.connect("my_medicalshop.db")
    conn.row_factory=dict_factory
    cursor =conn.cursor()

    cursor.execute("SELECT * FROM Products WHERE product_id=?",(productId,))

    product=cursor.fetchone()
    conn.close()

    return product


################################ Get all Orders ###############################

def getAllOrders():

    conn = sqlite3.connect("my_medicalshop.db")
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Orders ")
    
    orders = cursor.fetchall()
    
    orderJson = []
    
    for order in orders:
        orderJson.append(order)
        
    conn.close()
    return orderJson

################################ Get Spacific Order ###############################
def getSpacificOrder(orderId):

    conn=sqlite3.connect("my_medicalshop.db")
    conn.row_factory=dict_factory
    cursor=conn.cursor()
    
    cursor.execute("SELECT * FROM Orders WHERE order_id=? ",(orderId,))
    
    order=cursor.fetchone()
    conn.close()

    return order

