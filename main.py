from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def myindex():
    return render_template("index.html")

@app.route("/dashboard")
def my_dashboard():
    return render_template("dashboard.html")

@app.route("/products")
def my_dashboard():
    return render_template("products.html")
app.run()