import psycopg2
from flask import Flask,render_template,request,redirect,session,url_for
from dbservice import calc_profit,create_user,add_product,get_data,add_sale

try:
    conn = psycopg2.connect(
        database="myduka_class", user='postgres', password='12345', host='127.0.0.1', port= '5432')
except:
    print('unable to connect to the database')

app=Flask(__name__)

@app.route("/")
def myindex():
    return render_template("index.html")


def login_check():
    if session['email'] != None:
        return redirect("/dashbboard")
    return redirect("/signin")

@app.route("/dashboard")
def my_dashboard():
    dates=[]
    profits=[]
    for i in calc_profit():
        dates.append(str(i[0]))
        profits.append(float(i[1]))
    return render_template("dashboard.html",dates=dates,profits=profits)


@app.route("/signup", methods= ["POST", "GET"])
def create_account():
    if request.method=="POST":
        name=request.form["full_name"]
        email=request.form["email"]
        password=request.form["password"]
        values=(name,email,password)
        create_user(values)
        return redirect("/sign_up")
    return render_template("signup.html")


@app.route("/signup")
def sign_up():
   return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect('/')

@app.route("/products")
def products():
    myprods=get_data('products')
    return render_template("/products.html",myprods=myprods)

@app.route("/add-products", methods=["POST","GET"])
def addproduct():
        name=request.form["name"]
        buying_price=request.form["buying_price"]
        selling_price=request.form["selling_price"]
        stock_quantity=request.form['stock_quantity']
        values=(name,buying_price,selling_price,stock_quantity)
        add_product(values)
        return redirect("/products")

@app.route("/sales")
def sales():
    products=get_data('products')
    sales=get_data('sales')
    return render_template("/sales.html",mysales=sales,myprods=products)

@app.route("/add-sale", methods=["POST","GET"])
def addsale():
        pid=request.form["pid"]
        quantity=request.form["quantity"]
        values=(pid,quantity)
        add_sale(values)
        return redirect("/sales")

app.run(debug=True)