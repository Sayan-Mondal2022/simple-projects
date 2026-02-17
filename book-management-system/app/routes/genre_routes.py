from flask import Blueprint, request, jsonify
from app.models import db, Genre

genre_bp = Blueprint("genre_bp", __name__)

@genre_bp.route("/genres", methods=["POST"])
def add_genre():
    data = request.json

    genre = Genre(
        name=data["name"], 
        description=data.get("description")
    )

    db.session.add(genre)
    db.session.commit()

    return jsonify({"message": "Genre added successfully"})


@genre_bp.route("/genres", methods=["GET"])
def get_genres():
    genres = Genre.query.all()

    result = []
    for genre in genres:
        result.append({
            "id": genre.id,
            "name": genre.name
        })

    return jsonify(result)
