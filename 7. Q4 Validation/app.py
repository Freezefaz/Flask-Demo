from flask import Flask, render_template, request, redirect, url_for
import os
import requests


app = Flask(__name__)

@app.route("/user")
def show_user():
    return render_template("layout.template.html")

@app.route("/user", methods=["POST"])
def process_user():
    first_name  = request.form.get("first-name") # or "" will give out nan but no logic short circuit
    last_name  = request.form.get("last-name")
    email  = request.form.get("email")

    # using array to check for individual errors and compile them
    errors = []
    #check NONE first then the next so as not to cause logic short circuit
    if first_name is None or len(first_name) <= 3:
        errors.append("First Name need to have 3 characters or more")
    if last_name is None or len(last_name) <= 3:
        errors.append("Last Name need to have 3 characters or more")
    if email is None or "@" not in email:
        errors.append("Invalid")

    if len(errors) == 0:
        return "Success"
    else:
        return render_template("layout.template.html", errors=errors)

# Part 2 of Qn 4

@app.route("/userv2")
def show_advance_user():
    return render_template("user.template.html", errors={}, old_data={}) #to define the errors and old data in the html
    #old data is to retain the info typed out by user and not have it cleared if there is an error

@app.route("/userv2", methods=["POST"])
def process_advance_user():
    first_name  = request.form.get("first-name") # or "" will give out nan but no logic short circuit
    last_name  = request.form.get("last-name")
    email  = request.form.get("email")

    # this is a dictionary
    errors = {}

    if first_name is None or len(first_name) <= 3:
        errors["first_name"] = "First Name need to have 3 characters or more"
    if first_name is None or len(first_name) > 20:
        errors["first_name"] = "Your first name cannot have more than 20 characters"
    if last_name is None or len(last_name) <= 3:
        errors["last_name"] = "Last Name need to have 3 characters or more"
    if last_name is None or len(last_name) > 20:
        errors["last_name"] = "Your last name cannot have more than 20 characters"
    if email is None or "@" not in email:
        errors["eamil"] = "Invalid"

    if len(errors) == 0:
        return "Success"
    else:
        return render_template("user.template.html", errors=errors, old_data=request.form) #requset is a flask object



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)