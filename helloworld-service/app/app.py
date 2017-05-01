from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
	return jsonify(greeting="Hello")

@app.errorhandler(404)
def page_not_found(error):
	return jsonify(message='Not Found.'), 404

if __name__ == '__main__':
	app.run(host='0.0.0.0')
