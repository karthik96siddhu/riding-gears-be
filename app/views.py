from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

@api_bp.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@api_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item not found"}), 404