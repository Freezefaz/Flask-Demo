from flask import Flask, render_template, request, redirect, url_for
import os
import requests

app = Flask(__name__)

@app.route("/bmi")
def bmi():
    return render_template("layout.template.html")

@app.route("/bmi", methods=["POST"])
def calculate_bmi():
    w = request.form.get("weight")
    h = request.form.get("height")
    bmi = float(w) / (float(h) ** 2)
    new_bmi = round(bmi, 2)
    #can start a new template bmi(template): bmi(the answer)
    # return must be a str or NOT INT/ FLOAT
    return str(new_bmi)

#"magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)