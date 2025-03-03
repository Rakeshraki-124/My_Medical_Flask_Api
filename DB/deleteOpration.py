import sqlite3


def deleteUser(user_id):
    conn = sqlite3.connect('my_medicalshop.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Users WHERE user_id = ?", (user_id,))
    
    conn.commit()
    conn.close()
   
def delete_All_Users():
    conn = sqlite3.connect('my_medicalshop.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Users")
    
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect('my_medicalshop.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Products WHERE product_id = ?", (product_id,))
    
    conn.commit()
    conn.close()

def delete_order(order_id):
    conn = sqlite3.connect('my_medicalshop.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Orders WHERE order_id = ?", (order_id,))
    
    conn.commit()
    conn.close()