from flask import Blueprint, jsonify, request
from models import db, Prospect, Company

prospect_bp = Blueprint('prospect', __name__)

@prospect_bp.route('/prospects', methods=['GET'])
def get_prospects():
    query = Prospect.query
    if 'first_name' in request.args:
        query = query.filter(Prospect.first_name.ilike(f"%{request.args['first_name']}%"))
    if 'last_name' in request.args:
        query = query.filter(Prospect.last_name.ilike(f"%{request.args['last_name']}%"))
    if 'company' in request.args:
        query = query.join(Prospect.company).filter(Company.name.ilike(f"%{request.args['company']}%"))
    if 'job_description' in request.args:
        query = query.filter(Prospect.job_description.ilike(f"%{request.args['job_description']}%"))

    prospects = query.all()
    return jsonify([prospect.to_dict() for prospect in prospects])

@prospect_bp.route('/prospects/<int:id>', methods=['GET'])
def get_prospect(id):
    prospect = Prospect.query.get_or_404(id)
    return jsonify(prospect.to_dict())

@prospect_bp.route('/prospects', methods=['POST'])
def create_prospect():
    data = request.json
    prospect = Prospect(**data)
    db.session.add(prospect)
    db.session.commit()
    return jsonify(prospect.to_dict()), 201

@prospect_bp.route('/prospects/<int:id>', methods=['PUT'])
def update_prospect(id):
    data = request.json
    prospect = Prospect.query.get_or_404(id)
    for key, value in data.items():
        setattr(prospect, key, value)
    db.session.commit()
    return jsonify(prospect.to_dict())

@prospect_bp.route('/prospects/<int:id>', methods=['DELETE'])
def delete_prospect(id):
    prospect = Prospect.query.get_or_404(id)
    db.session.delete(prospect)
    db.session.commit()
    return '', 204

def model_to_dict(model):
    d = {}
    for column in model.__table__.columns:
        d[column.name] = getattr(model, column.name)
    return d

Prospect.to_dict = lambda self: model_to_dict(self)