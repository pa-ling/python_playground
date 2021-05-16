# coding=utf-8
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello():
    items = ["Apfel", "Birne", "Banane"]

    return render_template("start.html", name="Max Mustermann", items=items)


@app.route("/test")
def test():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("test.html", name=name, age=age)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError or TypeError:
        return False


@app.route("/currency")
def currency():
    rate = request.args.get("rate")
    src_currency = request.args.get("src_currency")
    trg_currency = request.args.get("trg_currency")

    exchanges = {}
    if rate is None or not is_number(rate):
        return render_template("currency.html",
                               rate=rate, src_currency=src_currency, trg_currency=trg_currency, exchanges=exchanges)

    amounts = [5, 10, 25, 50, 100, 250, 500, 1000]

    for amount in amounts:
        exchanges[amount] = amount * float(rate)

    return render_template("currency.html",
                           rate=rate, src_currency=src_currency, trg_currency=trg_currency, exchanges=exchanges)
