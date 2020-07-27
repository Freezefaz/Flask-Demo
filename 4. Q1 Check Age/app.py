from flask import Flask, render_template, request, redirect, url_for
import os
import requests

app = Flask(__name__)

# Do the GET first
@app.route("/ask")
def voter_age():
    return render_template("layout.template.html")

# Do the POST
@app.route("/ask", methods=["POST"])
def age_check():
    # int cannot put at the variable
    age = request.form.get("age-check")
    # must be int if using conditions with int
    if int(age) > 21:
        return "You are able to vote"
    else:
        return "Try again in 5 years time"

#"magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)