from flask import Blueprint, request, jsonify
from models import db, Prospect, Company
import pandas as pd

file_upload_bp = Blueprint('file_upload', __name__)

@file_upload_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        return 'Unsupported file type', 400

    for _, row in df.iterrows():
        company = Company.query.filter_by(name=row.get('company')).first()
        if not company:
            company = Company(name=row.get('company'))
            db.session.add(company)
            db.session.commit()

        prospect = Prospect(
            civility=row.get('civility'),
            first_name=row.get('first_name'),
            last_name=row.get('last_name'),
            linkedin_url=row.get('linkedin_url'),
            email=row.get('email'),
            status=row.get('status'),
            priority=row.get('priority'),
            mobile_phone=row.get('mobile_phone'),
            direct_line=row.get('direct_line'),
            switchboard=row.get('switchboard'),
            other_phone_1=row.get('other_phone_1'),
            other_phone_2=row.get('other_phone_2'),
            job_description=row.get('job_description'),
            years_in_position=row.get('years_in_position'),
            years_in_company=row.get('years_in_company'),
            title=row.get('title'),
            intent_signal=row.get('intent_signal'),
            company_id=company.id
        )
        db.session.add(prospect)
    db.session.commit()
    return 'File uploaded successfully', 200