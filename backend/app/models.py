from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Prospect(db.Model):
    __tablename__ = 'prospects'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    civility = db.Column(db.String(10))
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    linkedin_url = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    status = db.Column(db.String(50))
    priority = db.Column(db.String(50))
    mobile_phone = db.Column(db.String(50))
    direct_line = db.Column(db.String(50))
    switchboard = db.Column(db.String(50))
    other_phone_1 = db.Column(db.String(50))
    other_phone_2 = db.Column(db.String(50))
    job_description = db.Column(db.Text)
    years_in_position = db.Column(db.Integer)
    years_in_company = db.Column(db.Integer)
    title = db.Column(db.String(255))
    intent_signal = db.Column(db.Text)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id', ondelete='SET NULL'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    company = db.relationship('Company', backref='prospects')

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    linkedin_url = db.Column(db.String(255))
    website = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    revenue = db.Column(db.String(100))  
    employee_count = db.Column(db.Integer)
    employee_range = db.Column(db.String(100))
    year_founded = db.Column(db.Integer)
    description = db.Column(db.Text)
    vat_number = db.Column(db.String(100))
    country = db.Column(db.String(100)) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    addresses = db.relationship('CompanyAddress', backref='company', cascade="all, delete-orphan")
    other_fields = db.relationship('OtherField', secondary='prospect_otherfield_association', back_populates='companies')

class CompanyAddress(db.Model):
    __tablename__ = 'company_addresses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id', ondelete='CASCADE'), nullable=False)
    postal_code = db.Column(db.String(20))
    city = db.Column(db.String(100))
    address = db.Column(db.Text)
    is_headquarters = db.Column(db.Boolean, default=False)
    country = db.Column(db.String(100)) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class OtherField(db.Model):
    __tablename__ = 'other_fields'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prospect_id = db.Column(db.Integer, db.ForeignKey('prospects.id', ondelete='CASCADE'), nullable=False)
    field_name = db.Column(db.String(50), nullable=False)
    field_value = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    prospect = db.relationship('Prospect', backref='other_fields')