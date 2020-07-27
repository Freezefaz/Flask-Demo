from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route("/") # route route domain name -> calls home function
# function called through the server is called view fucntion
# Controls what the user can see
def home():
    fname = "Fareez"
    lname = "Aziz"
    return render_template("index.template.html", first_name=fname)

# To received the request
@app.route("/contact", methods=["GET"])
def about_us():
    # Don't put template infront as the folder is already named as such
    return render_template("contact-us.template.html")

# To send request
@app.route("/contact", methods=["POST"])
def process_contact():
    fullname = request.form.get("fullname")
    email = request.form.get("email")
    return render_template("contact-us.template.html", fullname=fullname, email=email)

# # parameterized routes
# @app.route("/add/<n1>/<n2>")
# def add_two(n1, n2):
#     total = int(n1) + int(n2)
#     return render_template("math.template.html", num1=n1, num2=n2, result=total)

# @app.route("/products")
# def show_products():
#     #returns a JSON file if return is a dictionary
#     return {
#         "id": 1,
#         "product-name": "Anvil",
#         "desc": "For dropping"
#     }


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)