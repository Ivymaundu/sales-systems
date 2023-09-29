from flask import Flask,render_template
app=app = Flask(__name__)

@app.route("/")
def myindex():
    return render_template("index.html")

@app.route("/dashboard")
def my_dashboard():
    return render_template("dashboard.html")
app.run()