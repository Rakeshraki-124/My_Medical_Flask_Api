from sqlite3 import OperationalError
from flask import Flask, request, jsonify
from DB.addOpration import createUser, addProduct,addOrder,sellHistory
from DB.CreatTableOpration import createTables
from DB.readOpration import getAllUsers, getAllProducts,getSpacificUser,getAllOrders,getSpacificOrder,getSpacificProduct
from DB.auth import user_auth
from DB.updateOpration import updateUsers ,updateProduct ,updateOrders
from DB.deleteOpration import deleteUser,delete_All_Users,delete_product,delete_order
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.json.sort_keys = False


@app.route("/", methods=["GET"])
def home():
    return "WELL COME TO RAKESH WORLD"

################################ (USER SINGUP) ########################################
@app.route("/signUp", methods=["POST"])
def singup():
    try:
        name = request.form["name"]
        password = request.form["password"]
        email = request.form["email"]
        phone = request.form["phone"]
        address = request.form["address"]
        pincode = request.form["pincode"]

        data = createUser(
        name=name,
        password=password,
        email=email,
        phoneNumber=phone,
        address=address,
        pinCode=pincode,
    )
        if data:
            return jsonify({"status": 200, "message": data})
        else:
            return jsonify({"status": 400, "message": "User not created"})
    
    except  OperationalError as e:
        return jsonify({"status": 400 ,"message" : e.args})

################################ (GET All USER) #######################################

@app.route("/getUsers", methods=["GET"])
def get_users():
    users = getAllUsers()
    return jsonify(users)

################################# (LOGIN USER) #####################################

@app.route("/login", methods=["POST"])
def login():

    try: 
        email = request.form['email']
        password = request.form["password"]

        login_data = user_auth(email =email, password =password)

        if login_data:
         
            return jsonify({"status":200,"message":"SingIn Succsesful","LoginInfo": login_data['user_id']})
        else:
            return jsonify({"status":300,"message":"Invalid id password"})
      
    except  OperationalError as e:

        return jsonify({"status": 400 ,"message" : e.args})
    
################################ (GET SPACIFIC USER) #####################################


@app.route('/getSpacificUser', methods = ['POST'])    
def spacificser():

    try:
        user_id = request.form['user_id']
        
        user = getSpacificUser(user_id)

        if user:
            return jsonify({"status":200,"message":user})
        else:
            return jsonify({"status":300,"message":"User not found"})
        
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})

################################# (UPDATE USER) #####################################

def save_image(file):
    if file:
        filename = secure_filename(file.filename)  # Sanitize the filename
        file_path = os.path.join('path/to/save/images', filename)  # Save to this directory
        file.save(file_path)  # Save the file to the server
        return file_path  # Return the file path
    return None
    
@app.route('/updateUserFeild' , methods=['PATCH'])
def updateUserFeild():
    try:
        user_id = request.form['user_id']
        allFields = request.form.items()

        updateUser = {}

        for key ,value in allFields:
            if key != 'user_id':
                updateUser[key] = value


         # Handle image upload
        image_file = request.files.get('pic')  # Get the uploaded image file
        if image_file:
            image_path = save_image(image_file)  # Save the image and get the file path
            updateUser['image_id'] = image_path  # Add image_id to the update fields


        updateUsers(userID=user_id , **updateUser)
        
        return jsonify({"status":200,"message":"User updated successfully"})
    
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})
    
################################# (DELETE USER) ####################################

@app.route('/deleteUser', methods=["DELETE"])
def deleteuser():

    try:
        user_id = request.form['user_id']
        
        deleteUser(user_id=user_id)
        
        
        return jsonify({"status":200,"message":"User deleted successfully"})
    
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})    
    
################################# (DELETE All USER) ####################################
@app.route('/deleteAllUsers', methods=['DELETE'])
def deleteAllUsers():
    try:
        delete_All_Users()
        
        return jsonify({"status":200,"message":"All users deleted successfully"})
    
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})

################################ (ADD PRODUCT) ######################################


@app.route("/addProduct", methods=["POST"])
def products():
 
    try:
        name = request.form["product_name"]
        price = request.form["price"]
        stock = request.form["stock"]
        category = request.form["category"]
        expiry_date = request.form["expiry_date"]
        product_description = request.form["product_description"]
        product_image_id = request.form["product_image_id"]
        product_power = request.form["product_power"]
        product_rating = request.form["product_rating"]

        product_data = addProduct(
        product_name=name,
        price=price,
        stock=stock,
        category=category,
        expiry_date=expiry_date,
        product_description=product_description,
        product_image_id=product_image_id,
        product_power=product_power,
        product_rating=product_rating
    )
        return jsonify({"status": 200, "message": product_data})    

    except OperationalError as e:
        return jsonify({"status": 400 ,"message" :str(e)})
    
    
################################ (GET ALL PRODUCTS) #####################################

@app.route("/getProducts", methods=["GET"])
def get_products():
    product = getAllProducts()
    return jsonify(product)

################################ (GET SPACIFIC PRODUCT) ##############################

@app.route('/getSpacificProduct', methods = ['post'])    
def spacificProduct():

    try:
        product_id = request.form['product_id']
        
        product = getSpacificProduct(product_id)
        if product:
            return jsonify({"status":200,"message":product})
        else:
            return jsonify({"status":300,"message":"Product not found"})
        
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})
    
################################ (UPDATE PRODUCTS) ###################################

@app.route('/updateProduct', methods=['PATCH'])
def updateProductFiled():
    try:
        product_id = request.form['product_id']
        allFields = request.form.items()

        updateProducts = {}

        for key, value in allFields:
            if key!= 'product_id':
                updateProducts[key] = value
        updateProduct(productID=product_id , **updateProducts)
        
        return jsonify({"status":200,"message":"Product updated successfully"})
    
    except OperationalError as e:

        return jsonify({"status": 400,"message":"There is a issue with db", "db_msg" : str(e.args)})
    
    except AttributeError as e:
        return jsonify({"status": 400,"message":str(e.args)})

################################ (Delete Product) ########################################
@app.route('/deleteProduct', methods=['DELETE'])

def deleteProduct():
    try:
        product_id = request.form['product_id']
        
        delete_product(product_id=product_id)
        
        return jsonify({"status":200,"message":"Product deleted successfully"})
    
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})

################################ (ADD ORDERS) ########################################
    
@app.route("/addOrders", methods=["POST"])
def addOrders():

    try:
        userId= request.form['user_id']
        productId = request.form['product_id']
        productName= request.form['product_name']
        userName = request.form['user_name']
        quantity = request.form['quantity']
        Order_price = request.form['price']
        totalPrice = request.form['total_price']
        subtotal_price = request.form['subtotal_price']
        order_categories = request.form['category']
        message = request.form['message']
        product_image_id = request.form['product_image_id']
        delivery_charge = request.form['delivery_charge']
        tax_charge = request.form['tax_charge']
        user_address = request.form['user_address']
        user_pincode = request.form['user_pincode']
        user_mobile = request.form['user_mobile']
        user_email = request.form['user_email']
        order_status = request.form['order_status']
        order_cancel_status = request.form['order_cancel_status']
        user_street = request.form['user_street']
        user_city = request.form['user_city']
        user_state = request.form['user_state']
        discount_price = request.form['discount_price']
        shipped_date = request.form['shipped_date']
        out_of_delivery_date = request.form['out_of_delivery_date']
        delivered_date = request.form['delivered_date']

        order_data = addOrder(
        userID = userId,
        productName = productName,
        productID = productId,
        userName = userName,
        quantity = quantity,
        price = Order_price,
        totalPrice = totalPrice,
        subtotalPrice=subtotal_price,
        category = order_categories,
        message = message,
        product_image_id=product_image_id,
        delivery_charge=delivery_charge,
        tax_charge=tax_charge,
        user_address=user_address,
        user_pincode=user_pincode,
        user_mobile=user_mobile,
        user_email=user_email,
        order_status=order_status,
        order_cancel_status=order_cancel_status,
        user_street=user_street,
        user_city=user_city,
        user_state=user_state,
        discount_price=discount_price,
        shipped_date=shipped_date,
        out_of_delivery_date=out_of_delivery_date,
        delivered_date=delivered_date
    )

        return jsonify({"status":200, "massage":"Order Added", "orderData":order_data})
    
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})
    
############################### (GET All ORDERS) #####################################


@app.route('/getOrders', methods=['GET'])
def getOrders():
    try:
        orders = getAllOrders()
        return jsonify(orders)
    
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})

################################ (Get  SPACIFIC ORDERS) #####################################
@app.route('/getSpacificOrders', methods=['POST'])
def getSpacificOrders():

    try:
        order_id = request.form['order_id']
        orders = getSpacificOrder(order_id)
        
    
        if orders:
            return jsonify({"status":200,"message":orders})
        else:
            return jsonify({"status":300,"message":"Order not found"})
    
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})

################################ (Update order) ########################################

@app.route('/updateOrder', methods=['PATCH'])
def updateOrderFiled():
    try:
        order_id = request.form['order_id']
        allFields = request.form.items()
        updateOrder = {}
        for key, value in allFields:
            if key!= 'order_id':
                updateOrder[key] = value
        updateOrders(orderID=order_id , **updateOrder)
        
        return jsonify({"status":200,"message":"Order updated successfully"})
    
    except OperationalError as e:
        return jsonify({"status": 400,"message" : str(e.args)}) 


################################ (Delete order) ########################################
@app.route('/deleteOrder', methods=['DELETE'])

def deleteOrder():
    try:
        order_id = request.form['order_id']
        
        delete_order(order_id=order_id)
        
        return jsonify({"status":200,"message":"Order deleted successfully"})
    
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})
################################ (sell history) #####################################
@app.route('/sell_history',methods=['POST'])
def sell_history():

    try:
        
        user_id = request.form['user_id']
        user_name=request.form['user_name']
        product_id = request.form['product_id']
        product_name = request.form['product_name']
        sell_price = request.form['price']
        total_price = request.form['total_price']
        quantity = request.form['quantity']
        product_category = request.form['product_category']
        remaining_stock = request.form['remaining_stock']


        sell_data = sellHistory(
        userId = user_id,
        userName= user_name,
        productId= product_id,
        productName = product_name,
        price = sell_price,
        totalPrice = total_price,
        quantity = quantity,
        product_category = product_category,
        remainingStock = remaining_stock,
        )
        return sell_data
    
    except OperationalError as e:
        return jsonify({"status": 400,"message":str(e.args)})

if __name__ == "__main__":
    createTables()
    app.run(debug=True)


