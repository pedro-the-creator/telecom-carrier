from flask import Blueprint, request, jsonify
from app import db
from app.models import DIDNumber

bp = Blueprint("api", __name__)

@bp.route("/numbers", methods=["POST"])
def create_number():
    data = request.get_json()
    if not data or "value" not in data:
        return jsonify({"error": "Invalid data"}), 400

    try:
        number = DIDNumber(**data)
        db.session.add(number)
        db.session.commit()
        return jsonify({"message": "Number created", "id": number.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/numbers", methods=["GET"])
def list_numbers():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("size", 10, type=int)
    numbers = DIDNumber.query.paginate(page=page, per_page=per_page)
    return jsonify([{"id": n.id, "value": n.value} for n in numbers.items])

@bp.route("/numbers/<int:id>", methods=["GET"])
def get_number(id):
    number = DIDNumber.query.get_or_404(id)
    return jsonify({"id": number.id, "value": number.value})

@bp.route("/numbers/<int:id>", methods=["PUT"])
def update_number(id):
    number = DIDNumber.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(number, key, value)
    db.session.commit()
    return jsonify({"message": "Updated successfully"})

@bp.route("/numbers/<int:id>", methods=["DELETE"])
def delete_number(id):
    number = DIDNumber.query.get_or_404(id)
    db.session.delete(number)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"})