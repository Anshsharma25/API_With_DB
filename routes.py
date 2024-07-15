from flask import request, jsonify, Blueprint
from models import Bank, Branch  # Import your SQLAlchemy models
from app import db  # Import the db object from your Flask app


api_bp = Blueprint('api', __name__)

@api_bp.route('/banks', methods=['GET'])
def get_banks():
    from models import Bank  # Delayed import to avoid circular dependency
    banks = Bank.query.all()
    return jsonify([{'id': bank.id, 'name': bank.name} for bank in banks])

@api_bp.route('/banks/<int:bank_id>/branches', methods=['GET'])
def get_bank_branches(bank_id):
    from models import Branch  # Delayed import to avoid circular dependency
    branches = Branch.query.filter_by(bank_id=bank_id).all()
    return jsonify([{'id': branch.id, 'branch': branch.branch} for branch in branches])

@api_bp.route('/branches/search', methods=['GET'])
def search_branches():
    from models import Branch  # Delayed import to avoid circular dependency
    branch_name = request.args.get('name')
    branches = Branch.query.filter(Branch.branch.contains(branch_name)).all()
    return jsonify([{'id': branch.id, 'branch': branch.branch, 'bank': branch.bank.name} for branch in branches])

def register_blueprints(app):
    app.register_blueprint(api_bp)
