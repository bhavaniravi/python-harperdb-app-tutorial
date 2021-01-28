from flask import Flask, request, jsonify
from dotenv import load_dotenv
import json

load_dotenv(verbose=True)

# Import BookService here


app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

# Add the Flask routes here


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
