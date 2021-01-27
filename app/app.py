from flask import Flask, request, jsonify
from dotenv import load_dotenv
import json

load_dotenv(verbose=True)

from service import BookService


app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/book", methods=["GET"])
def list_books():
    return jsonify(BookService().get_all())


@app.route("/book", methods=["POST"])
def create_book():
    return jsonify(BookService().create(request.get_json()))


@app.route("/book/<book_id>", methods=["PUT"])
def update_book(book_id):
    return jsonify(BookService().update(book_id, request.get_json()))


@app.route("/book/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    return jsonify(BookService().delete(book_id))

@app.route("/book/<book_id>", methods=["GET"])
def get_book(book_id):
    return jsonify(BookService().get(book_id))


@app.route("/book/<book_id>/note", methods=["POST"])
def add_notes(book_id):
    return jsonify(BookService().add_notes(book_id, request.get_json()))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
