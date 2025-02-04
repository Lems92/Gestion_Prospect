from flask import Blueprint, jsonify, request
from models import db, Prospect
import pandas as pd

prospect_bp = Blueprint('prospect', __name__)

#recherche filtre prospect
@prospect_bp.route('/prospects', methods=['GET'])
def get_prospects():
    query = Prospect.query
    if 'first_name' in request.args:
        query = query.filter(Prospect.first_name.ilike(f"%{request.args['first_name']}%"))
    if 'last_name' in request.args:
        query = query.filter(Prospect.last_name.ilike(f"%{request.args['last_name']}%"))
    if 'company' in request.args:
        query = query.filter(Prospect.company.ilike(f"%{request.args['company']}%"))
    if 'title' in request.args:
        query = query.filter(Prospect.title.ilike(f"%{request.args['title']}%"))

    prospects = query.all()
    return jsonify([prospect.to_dict() for prospect in prospects])

#prospect unique
@prospect_bp.route('/prospects/<int:id>', methods=['GET'])
def get_prospect(id):
    prospect = Prospect.query.get_or_404(id)
    return jsonify(prospect.to_dict())

#Créer prospect
@prospect_bp.route('/prospects', methods=['POST'])
def create_prospect():
    data = request.json
    prospect = Prospect(**data)
    db.session.add(prospect)
    db.session.commit()
    return jsonify(prospect.to_dict()), 201

# UPDATE prospect
@prospect_bp.route('/prospects/<int:id>', methods=['PUT'])
def update_prospect(id):
    data = request.json
    prospect = Prospect.query.get_or_404(id)
    for key, value in data.items():
        setattr(prospect, key, value)
    db.session.commit()
    return jsonify(prospect.to_dict())

# DELETE prospect
@prospect_bp.route('/prospects/<int:id>', methods=['DELETE'])
def delete_prospect(id):
    prospect = Prospect.query.get_or_404(id)
    db.session.delete(prospect)
    db.session.commit()
    return '', 204

# UPLOAD fichier CSV ou XLSX
@prospect_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        return 'Unsupported file type', 400

    for _, row in df.iterrows():
        prospect = Prospect(
            civility=row.get('civility'),
            first_name=row.get('first_name'),
            last_name=row.get('last_name'),
            company_linkedin=row.get('company_linkedin'),
            linkedin_url=row.get('linkedin_url'),
            intent_signal=row.get('intent_signal'),
            other_1=row.get('other_1'),
            other_2=row.get('other_2'),
            other_3=row.get('other_3'),
            company=row.get('company'),
            title=row.get('title'),
            email=row.get('email'),
            status=row.get('status'),
            priority=row.get('priority'),
            mobile_phone=row.get('mobile_phone'),
            direct_line=row.get('direct_line'),
            switchboard=row.get('switchboard'),
            other_phone_1=row.get('other_phone_1'),
            other_phone_2=row.get('other_phone_2'),
            job_description=row.get('job_description'),
            company_website=row.get('company_website'),
            years_in_position=row.get('years_in_position'),
            years_in_company=row.get('years_in_company'),
            industry=row.get('industry'),
            ca=row.get('ca'),
            company_employee_count=row.get('company_employee_count'),
            company_employee_range=row.get('company_employee_range'),
            company_year_founded=row.get('company_year_founded'),
            company_description=row.get('company_description'),
            vat=row.get('vat'),
            headquarters_pc=row.get('headquarters_pc'),
            headquarters_city=row.get('headquarters_city'),
            address=row.get('address')
        )
        db.session.add(prospect)
    db.session.commit()
    return 'File uploaded successfully', 200