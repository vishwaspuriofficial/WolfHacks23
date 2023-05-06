from flask import Flask, request, jsonify, send_from_directory
from a_star import get_pixel_map, solve
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
pixel_maps = {
    "map500": (500, 500),
    "map500new": (500, 500),
}

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return send_from_directory('../Frontend', 'index.html')


@app.route('/api/get_path', methods=['POST'])
def get_path():
    staring_x = int(request.form.get('starting_x'))
    staring_y = int(request.form.get('starting_y'))
    ending_x = int(request.form.get('ending_x'))
    ending_y = int(request.form.get('ending_y'))
    map_name = request.form.get('map_name')
    width, height = pixel_maps[map_name]
    pixel_map = get_pixel_map(map_name, width, height)
    print(f"solving at {staring_x}, {staring_y} to {ending_x}, {ending_y}")
    path = solve(pixel_map, width, height, (staring_x, staring_y), (ending_x, ending_y))
    return jsonify({
        'path': path,
        'distance': 0,
        'time': 0,
    })

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory(".", path)

if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)