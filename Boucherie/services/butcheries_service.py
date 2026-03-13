from flask import Blueprint, jsonify, request

butcheries_bp = Blueprint('butcheries', __name__)

@butcheries_bp.route('/', methods=['GET'])
def list_butcheries():
    # Logic to list butcheries (e.g., from DB, with filters/pagination)
    return jsonify([
        {"id": 1, "name": "Boucherie Jean", "address": "123 Rue de la Viande", "latitude": 47.21, "longitude": -1.55},
        {"id": 2, "name": "La Côte d'Or", "address": "45 Av. des Abattoirs", "latitude": 47.22, "longitude": -1.56}
    ]), 200

@butcheries_bp.route('/<butchery_id>', methods=['GET'])
def get_butchery_details(butchery_id):
    # Logic to fetch specific butchery details
    return jsonify({
        "id": butchery_id,
        "name": f"Boucherie {butchery_id}",
        "address": "Some street, Nantes",
        "phone": "0240XXYYZZ",
        "schedule": {"monday": "08:00-12:00, 14:00-18:00"}
    }), 200

@butcheries_bp.route('/search', methods=['GET'])
def search_butcheries():
    query = request.args.get('q', '')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    # Logic for searching and filtering butcheries, potentially with geolocation
    return jsonify({"message": f"Searching for butcheries with query '{query}', near ({lat}, {lon})"}), 200
