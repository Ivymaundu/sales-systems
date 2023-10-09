import psycopg2
from flask import Flask,render_template,request,redirect
from dbservice import calc_profit,create_user

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
def my_dashboard():
    dates=[]
    profits=[]
    for i in calc_profit():
        dates.append(str(i[0]))
        profits.append(float(i[1]))
    return render_template("dashboard.html",dates=dates,profits=profits)


# @app.route("/signup", methods= ["POST", "GET"])
# def create_account():
#     full_name=request.form["full_name"]
#     email=request.form["email"]
#     password=request.form["password"]
#     values=(full_name,email,password)
#     create_user(values)
#     return redirect("/signin")

@app.route("/signup")
def sign_up():
   return render_template("signup.html")


app.run(debug=True)