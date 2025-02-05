from flask import Blueprint, jsonify, request
from app.models import db, Prospect
import pandas as pd

prospect_bp = Blueprint('prospect', __name__)

# Recherche filtrée des prospects
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

# Prospect unique
@prospect_bp.route('/prospects/<int:id>', methods=['GET'])
def get_prospect(id):
    prospect = Prospect.query.get_or_404(id)
    return jsonify(prospect.to_dict())


# Mettre à jour un prospect
@prospect_bp.route('/prospects/<int:id>', methods=['PUT'])
def update_prospect(id):
    data = request.json
    prospect = Prospect.query.get_or_404(id)
    for key, value in data.items():
        setattr(prospect, key, value)
    db.session.commit()
    return jsonify(prospect.to_dict())



# Upload de fichier 
@prospect_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return 'No file provided', 400
    
    if not (file.filename.endswith('.csv') or file.filename.endswith('.xlsx')):
        return 'Unsupported file type', 400
    
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)

    expected_columns = ['Civility', 'First Name', 'Last Name', 'Company linkedIn', 'Linkedin Url', 
                        'Intent signal', 'Other 1', 'Other 2', 'Other 3', 'Company', 'Title', 'E-mail', 
                        'Status', 'Priority', 'Mobile Phone', 'Direct line', 'Switchboard', 'Other phone 1', 
                        'Other phone 2', 'Job description', 'Company website', 'Years in position', 
                        'Years in company', 'Industry', 'CA', 'Company employee count', 
                        'Company employee range', 'Company year founded', 'Company description', 'VAT', 
                        'HEADQUARTERS PC', 'HEADQUARTERS CITY', 'Adress']
    
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        return jsonify({'error': f'Missing columns: {", ".join(missing_columns)}'}), 400
    
    print("Données extraites du fichier :")
    print(df.head())

    # Remplacer les valeurs NaN par des valeurs par défaut
    df = df.fillna({
        'E-mail':'NaN',
        'Years in position': 0,
        'Years in company': 0,
        'CA': 0,
        'Company employee count': 0,
        'Company year founded': 0
    })

    for _, row in df.iterrows():
        try:
            prospect = Prospect(
                civility=row.get('Civility'),
                first_name=row.get('First Name'),
                last_name=row.get('Last Name'),
                company_linkedin=row.get('Company linkedIn'),
                linkedin_url=row.get('Linkedin Url'),
                intent_signal=row.get('Intent signal'),
                other_1=row.get('Other 1'),
                other_2=row.get('Other 2'),
                other_3=row.get('Other 3'),
                company=row.get('Company'),
                title=row.get('Title'),
                email=row.get('E-mail'),
                status=row.get('Status'),
                priority=row.get('Priority'),
                mobile_phone=row.get('Mobile Phone'),
                direct_line=row.get('Direct line'),
                switchboard=row.get('Switchboard'),
                other_phone_1=row.get('Other phone 1'),
                other_phone_2=row.get('Other phone 2'),
                job_description=row.get('Job description'),
                company_website=row.get('Company website'),
                years_in_position=row.get('Years in position'),
                years_in_company=row.get('Years in company'),
                industry=row.get('Industry'),
                ca=row.get('CA'),
                company_employee_count=row.get('Company employee count'),
                company_employee_range=row.get('Company employee range'),
                company_year_founded=row.get('Company year founded'),
                company_description=row.get('Company description'),
                vat=row.get('VAT'),
                headquarters_pc=row.get('HEADQUARTERS PC'),
                headquarters_city=row.get('HEADQUARTERS CITY'),
                address=row.get('Adress')
            )
            db.session.add(prospect)
        except Exception as e:
            print(f"Erreur lors de l'ajout du prospect: {e}")

    db.session.commit()
    return 'File uploaded successfully', 200
