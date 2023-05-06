from flask import Flask, request, jsonify
from a_star import get_pixel_map, solve
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
pixel_maps = {
    "map500": (500, 500),
}

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/api/get_path', methods=['POST'])
def get_path():
    starting_position = request.form.get('starting_position')
    ending_position = request.form.get('ending_position')
    map_name = request.form.get('map_name')
    width, height = pixel_maps[map_name]
    pixel_map = get_pixel_map(map_name, width, height)
    path = solve(pixel_map, width, height)
    return jsonify({
        'path': path,
        'distance': 0,
        'time': 0,
    })


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)