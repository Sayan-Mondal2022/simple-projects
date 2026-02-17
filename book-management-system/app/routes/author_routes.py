from flask import Blueprint, request, jsonify
from app.models import db, Author

author_bp = Blueprint("author_bp", __name__)

# Create Author
@author_bp.route("/authors", methods=["POST"])
def add_author():
    data = request.json

    author = Author(
        name=data["name"],
        bio=data.get("bio")
    )

    db.session.add(author)
    db.session.commit()

    return jsonify({"message": "Author added successfully"})


# Get All Authors
@author_bp.route("/authors", methods=["GET"])
def get_authors():
    authors = Author.query.all()

    result = []
    for author in authors:
        result.append({
            "id": author.id,
            "name": author.name
        })

    return jsonify(result)