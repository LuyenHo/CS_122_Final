# import the Flask class from the flask module
from flask import Flask, render_template, jsonify, send_file
import function as fn

# create a Flask object called app
app = Flask(__name__)

# define a route to the home page
# create a template_display function

@app.route('/get_fire_map')
def get_fire_map():
    map_html = fn.generate_map_html()
    return jsonify(map_html=map_html)

# Route to generate and serve the counties plot
@app.route('/counties_plot')
def get_counties_plot():
    image_path = fn.generate_counties_plot()
    return send_file(image_path, mimetype='image/png')

# Route to generate and serve the counties plot
@app.route('/chart_plot')
def get_chart_plot():
    image_path = fn.generate_chart()
    return send_file(image_path, mimetype='image/png')


@app.route("/")
@app.route("/home")

def home_page_display():
    # render the final.html script
    fn.download_map()
    return render_template('final.html')


if __name__ == '__main__':
    app.run(debug=True)
