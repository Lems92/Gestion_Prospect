from flask import Blueprint, jsonify, request
from models import db, Company

company_bp = Blueprint('company', __name__)

@company_bp.route('/companies', methods=['GET'])
def get_companies():
    companies = Company.query.all()
    return jsonify([company.to_dict() for company in companies])

@company_bp.route('/companies/<int:id>', methods=['GET'])
def get_company(id):
    company = Company.query.get_or_404(id)
    return jsonify(company.to_dict())

@company_bp.route('/companies', methods=['POST'])
def create_company():
    data = request.json
    company = Company(**data)
    db.session.add(company)
    db.session.commit()
    return jsonify(company.to_dict()), 201

@company_bp.route('/companies/<int:id>', methods=['PUT'])
def update_company(id):
    data = request.json
    company = Company.query.get_or_404(id)
    for key, value in data.items():
        setattr(company, key, value)
    db.session.commit()
    return jsonify(company.to_dict())

@company_bp.route('/companies/<int:id>', methods=['DELETE'])
def delete_company(id):
    company = Company.query.get_or_404(id)
    db.session.delete(company)
    db.session.commit()
    return '', 204

def model_to_dict(model):
    d = {}
    for column in model.__table__.columns:
        d[column.name] = getattr(model, column.name)
    return d

Company.to_dict = lambda self: model_to_dict(self)