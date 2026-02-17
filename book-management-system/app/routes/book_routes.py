from flask import Blueprint, request, jsonify
from app.models import db, Book, Author, Genre

book_bp = Blueprint("book_bp", __name__)

# Create Book
@book_bp.route("/books", methods=["POST"])
def add_book():
    data = request.json

    # -------- Handle Author --------
    author_data = data.get("author")
    author = Author.query.filter_by(name=author_data["name"]).first()

    if not author:
        author = Author(
            name=author_data["name"],
            bio=author_data.get("bio")
        )
        db.session.add(author)
        db.session.flush()  # gets ID without committing

    # -------- Handle Genre --------
    genre_data = data.get("genre")
    genre = Genre.query.filter_by(name=genre_data["name"]).first()

    if not genre:
        genre = Genre(
            name=genre_data["name"],
            description=genre_data.get("description")
        )
        db.session.add(genre)
        db.session.flush()

    # -------- Create Book --------
    book = Book(
        title=data["title"],
        published_year=data.get("published_year"),
        total_copies=data.get("total_copies", 1),
        available_copies=data.get("total_copies", 1),
        author_id=author.id,
        genre_id=genre.id
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book, Author, and Genre handled successfully"})

# Get All Books
@book_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()

    result = []
    for book in books:
        result.append({
            "id": book.id,
            "title": book.title,
            "author": book.author.name,
            "genre": book.genre.name
        })

    return jsonify(result)
