from flask import Flask, render_template, request, redirect, url_for
import os
import requests

app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('index.template.html')


# @app.route('/contact-us', methods=["GET", "POST"])
# def contact_us():
#     if request.method == "GET":
#         # display the form
#         return render_template('contact_us.template.html')
#     elif request.method == "POST":
#         return "form recieved"

# @app.route('/contact-us', methods=["GET"])
# def contact_us():
#     return render_template('contact_us.template.html')


# @app.route('/contact-us', methods=["POST"])
# def process_contact_us():
#     fullname = request.form.get('fullname')
#     email = request.form.get('email')
#     return render_template('contact_us_success.template.html', 
#     fullname=fullname, email=email)


# @app.route('/calculate')
# def show_calculator():
#     return render_template("calculate.template.html")


# @app.route('/calculate', methods=["POST"])
# def process_calculator():
#     num1 = request.form.get('number1')
#     num2 = request.form.get('number2')
#     total = int(num1) + int(num2)
#     with open('total.txt','a') as fptr:
#         fptr.write(str(total)+'\n')
    
#     return render_template('results.template.html', number1=num1, number2=num2, total=total)

# Pokemon series

# Will be GET by default
@app.route('/pokemon_search')
def show_pokemon_search():
    return render_template('pokemon_search.template.html')

# to link to the default server
@app.route('/pokemon_search', methods=["POST"])
def process_pokemon_search():
    # From the form get the thing that is typed and store as variable
    pokemon_name = request.form.get('search-for')
    # rememeber to use FORMATTED STRING to link the search to the wesite
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    # return the data type
    pokemon_data = r.json()
    return pokemon_data['name']


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

