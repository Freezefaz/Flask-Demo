# boilerplate code
# pip install Flask paste at control terminal
# Target the folder by going to it and open in terminal
# Then python3 app.py to open the browser
# templates folder ***NOT TEMPLATE***

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route("/") # route route domain name -> calls home function
# function called through the server is called view fucntion
# Controls what the user can see
def home():
    fname = "Fareez"
    lname = "Aziz"
    return render_template("home.template.html",
    first_name=fname, last_name=lname)

# Will show about us
@app.route("/about")
def about_us():
    # Don't put template infront as the folder is already named as such
    return render_template("about.template.html")

# parameterized routes
@app.route("/add/<n1>/<n2>")
def add_two(n1, n2):
    total = int(n1) + int(n2)
    return render_template("math.template.html", num1=n1, num2=n2, result=total)

@app.route("/products")
def show_products():
    #returns a JSON file if return is a dictionary
    return {
        "id": 1,
        "product-name": "Anvil",
        "desc": "For dropping"
    }


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
