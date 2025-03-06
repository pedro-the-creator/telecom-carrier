from flask import Blueprint, request, jsonify
from app import db
from app.models import DIDNumber

bp = Blueprint("api", __name__)

@bp.route("/numbers", methods=["POST"])
def create_number():
    data = request.get_json()
    
    if not data or "value" not in data:
        return jsonify({"error": "Invalid data: missing required fields"}), 400
    
    try:
        monthly_price = float(data.get("monthly_price", 0))
        setup_price = float(data.get("setup_price", 0))
        
        if monthly_price < 0:
            return jsonify({"error": "Monthly price cannot be negative"}), 400
        
        if setup_price < 0:
            return jsonify({"error": "Setup price cannot be negative"}), 400
        
        number = DIDNumber(
            value=data["value"],
            monthly_price=monthly_price,
            setup_price=setup_price,
            currency=data["currency"]
        )
        
        db.session.add(number)
        db.session.commit()
        return jsonify({"message": "Number created", "id": number.id}), 201
        
    except ValueError:
        return jsonify({"error": "Invalid price format"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to create number: {str(e)}"}), 500

@bp.route("/numbers", methods=["GET"])
def list_numbers():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("size", 10, type=int)
    numbers = DIDNumber.query.paginate(page=page, per_page=per_page)
    result = [{
        "id": n.id,
        "value": n.value,
        "monthly_price": float(n.monthly_price),  
        "setup_price": float(n.setup_price),      
        "currency": n.currency
    } for n in numbers.items]
    
    return jsonify(result)

@bp.route("/numbers/<int:id>", methods=["GET"])
def get_number(id):
    number = DIDNumber.query.get_or_404(id)
    result = {
        "id": number.id,
        "value": number.value,
        "monthly_price": float(number.monthly_price),  
        "setup_price": float(number.setup_price),      
        "currency": number.currency    
    }
    return jsonify(result)

@bp.route("/numbers/<int:id>", methods=["PUT"])
def update_number(id):
    number = DIDNumber.query.get_or_404(id)
    data = request.get_json()
    
    try:
        if "monthly_price" in data:
            monthly_price = float(data["monthly_price"])
            if monthly_price < 0:
                return jsonify({"error": "Monthly price cannot be negative"}), 400
            number.monthly_price = monthly_price
        
        if "setup_price" in data:
            setup_price = float(data["setup_price"])
            if setup_price < 0:
                return jsonify({"error": "Setup price cannot be negative"}), 400
            number.setup_price = setup_price
        
        if "value" in data:
            number.value = data["value"]
        if "currency" in data:
            number.currency = data["currency"]
        
        db.session.commit()
        return jsonify({"message": "Updated successfully"})
    except ValueError:
        return jsonify({"error": "Invalid price format"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to update: {str(e)}"}), 500

@bp.route("/numbers/<int:id>", methods=["DELETE"])
def delete_number(id):
    number = DIDNumber.query.get_or_404(id)
    try:
        db.session.delete(number)
        db.session.commit()
        return jsonify({"message": "Deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to delete: {str(e)}"}), 500
    