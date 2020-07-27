from flask import Flask, render_template, request, redirect, url_for
import os
import requests


app = Flask(__name__)

@app.route("/currency")
def check_currency():
    return render_template("layout.template.html")

@app.route("/currency", methods=["POST"])
def convert_currency():
    from_cur = request.form.get("from_cur")
    to_cur = request.form.get("to_cur")
    API_URL = "https://www.alphavantage.co/query"
    data = { 
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": from_cur,
        "to_currency": to_cur,
        "apikey": "QHY0RUC998EYGH10"
    }
    response = requests.get(API_URL, data)
    data = response.json()
    exchange = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    #print(from_cur, to_cur) to check if its working

    return render_template("currency.exchange.template.html", from_cur=from_cur, to_cur=to_cur, exchange_rate=exchange_rate)
    # jp_conversion = float(jpy)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)