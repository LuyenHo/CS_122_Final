# import the Flask class from the flask module
from flask import Flask

# create a Flask object called app
app = Flask(__name__)

# define a route to the home page
# create a hey_there function
@app.route("/")
def hey_there():
    return "Hey there, welcome to my web application!"

@app.route("/about")
def about_page():
    return "About Page"