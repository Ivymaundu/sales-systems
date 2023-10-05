import psycopg2
from flask import Flask,render_template,request,redirect
from dbservice import get_data,add_product,add_sale,calc_profit

try:
    conn = psycopg2.connect(
        database="myduka_class", user='postgres', password='12345', host='127.0.0.1', port= '5432')
except:
    print('unable to connect to the database')

app=Flask(__name__)

@app.route("/")
def myindex():
    return render_template("index.html")

@app.route("/dashboard")
def profit1():       
    dates=[str(i[0]) for i in calc_profit()]
    profits=[float(i[1]) for i in calc_profit()]

    return render_template("dashboard.html", dates = dates, profits=profits)


# @app.route("/add-products" ,methods = ["POST"])
# def add_products():
#     name=request.form["name"]
#     buying_price=request.form["buying_price"]
#     selling_price=request.form["selling_price"]
#     stock_quantity=request.form["stock_quantity"]
#     values=(name,buying_price,selling_price,stock_quantity)
#     add_product(values)
#     return redirect("/products")



# @app.route("/products")
# def products():
#     myprods=get_data("products")
#     return render_template("products.html", myprods=myprods)


# @app.route("/add-sale",method="POST")
# def add_sale(values):
#     pid=request.form["pid"]
#     quantity=request.form["quantity"]
#     values(pid,quantity)
#     add_sale(values)
#     return redirect("/sales")

# @app.route("/sales")
# def sales():
#     products = get_data('products') 
#     sales=get_data('sales')

#     return render_template("sales.html", myprods=products,mysales=sales)


app.run(debug=True)