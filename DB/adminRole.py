import sqlite3

def updateApprovalStatus(userID, isApproved):

    conn = sqlite3.connect('my_medicalshop.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Users SET isApproved =? WHERE user_id =?", (isApproved, userID))
    
    conn.commit()
    conn.close()
