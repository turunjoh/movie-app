from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/page1")
def page1():
    return "Tämä on sivu 1"

@app.route("/page2")
def page2():
    return "Tämä on sivu 2"


@app.route("/test")
def test():
    content = ""
    for i in range(1, 101):
        content += str(i) + " "
    return content


@app.route("/page/<int:page_id>")
def page(page_id):
    return "Tämä on sivu " + str(page_id)

#@app.route("/")
#def index():
#    return "<b>Tervetuloa</b> <i>sovellukseen</i>!"

@app.route("/")
def index():
    words = ["apina", "banaani", "cembalo"]
    return render_template("index.html", message="Tervetuloa!", items=words)


@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    message = request.form["message"]
    return render_template("result.html", message=message)


@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/result_pizza", methods=["POST"])
def result_pizza():
    pizza = request.form["pizza"]
    extras = request.form.getlist("extra")
    message = request.form["message"]
    return render_template("result_pizza.html", pizza=pizza, extras=extras, message=message)
