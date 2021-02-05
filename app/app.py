from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Import BookService here


app = Flask(__name__)

# Add the Flask routes here


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
