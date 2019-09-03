from flask import Flask, render_template, jsonify, send_from_directory
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model')
def model():
	json_data =  json.loads(open('models/model.json').read())
	return jsonify(json_data)


@app.route('/<path:path>')
def load_shards(path):
    return send_from_directory('models', path)

@app.route('/classNames')
def classNames():
	json_data = open('models/class_names.txt').read()
	return json_data

if __name__ == '__main__':
	app.run(debug=True)