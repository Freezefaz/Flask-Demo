<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome Freezefaz,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

QUESTIONS TO ANSWER

Form Processing Practise
Q1: Check age

Create a route /ask that will display a form to ask for the user's age.

In the POST version of the route, the code will determine if age is above 21. If so, return the string "You are able to vote" or else display "Try again in 5 years time".

Q2: BMI

Create a route /bmi that will display two textfields, one for the weight (in kg) and one for the height (in metres).

In the POST versin of the route, display the user's BMI.

Q3: Currency Search

Use a route to display two textboxes and ask the user to enter two currency symbol.

In the POST version of the route, use the https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo API to retrieve and display the exchange rate.

You need to provide your own api key.

Q4: Validation

In a route, display the form to ask the user for their first name, last name and email address.

After processing the form, if the user has entered at least:

    Entered three characters for the first name
    Entered three characters for the last name
    email address contains a '@'

Then display in the template "Sign up successful".

If there any field doesn't match its rule, display in the template "There are some issues signing up". Display in an unordered list (i.e, bullet point) the criteria that the user didn't meet.

Advanced: Change the form to Bootstrap, and use Bootstrap error class to display the issues. See https://getbootstrap.com/docs/4.0/components/forms/#server-side for some hints.
