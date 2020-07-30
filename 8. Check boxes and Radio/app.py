from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__)

@app.route("/survey")
def survey_form():
    return render_template("survey.template.html")

@app.route("/survey", methods=["POST"])
def process_survey_time():
    region_text = {
        'north': "North (Yishun, AMK etc.)",
        'east': "East (Marina Parade, East Coast etc.)",
        'south': "South (Marina Bay, Tiong Bahru etc.)",
        'west': "Jurong, Boon Lay, Tuas"
    }

    response_time = request.form.get('response-time')
    service = request.form.get('service')
    attribution = request.form.getlist('attribution')
    region = request.form.get('region')
    return render_template('thank-you.template.html',
                           response_time=response_time,
                           service=service,
                           attribution=", ".join(attribution),
                           region=region_text.get(region)
                           )

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)