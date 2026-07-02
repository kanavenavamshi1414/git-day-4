from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():


    return "Welcome to vamshi Python!"


# API route
@app.route('/api/books', methods=['GET'])
def get_books():
    books = [
        {"id": 1, "title": "Python Basics", "author": "John Doe"},
        {"id": 2, "title": "Flask for Beginners", "author": "Jane Smith"}
    ]
    return jsonify(books)

# POST route
@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({
            "success": False,
            "message": "Title is required"
        }), 400

    return jsonify({
        "success": True,
        "message": "Book added successfully",
        "book": data
    }), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
