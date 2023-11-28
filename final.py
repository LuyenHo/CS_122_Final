# import the Flask class from the flask module
from flask import Flask
import analysis as an

# import the render_template function
from flask import render_template

# create a Flask object called app
app = Flask(__name__)

# define a route to the home page
# create a template_display function
@app.route("/")
@app.route("/home")

def template_display():
    # render the cs122.html script
    an.download_map()
    return render_template('final.html')