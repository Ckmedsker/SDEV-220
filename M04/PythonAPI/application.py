from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.book_name} was written by {self.author}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'book name': book.book_name, 'author': book.author}

        output.append(book_data)

    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'book name': book.book_name, 'author': book.author}


@app.route('/books', methods=['POST'])
def add_book(id):
    book = Book(book_name=request.json['book_name'],
                author=request.json['author'],
                publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}


@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = book.query.get(id)
    if book is None:
        return {"error": "book not found"}
    db.session.delete(book)
    db.session.commit()
    return {'message': "yeet!@"}