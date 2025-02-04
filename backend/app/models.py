from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Prospect(db.Model):
    __tablename__ = 'prospects'

    id = db.Column(db.Integer, primary_key=True)
    civility = db.Column(db.String(100))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    company_linkedin = db.Column(db.String(255))
    linkedin_url = db.Column(db.Text)
    intent_signal = db.Column(db.String(255))
    other_1 = db.Column(db.String(255))
    other_2 = db.Column(db.String(255))
    other_3 = db.Column(db.String(255))
    company = db.Column(db.String(255))
    title = db.Column(db.String(255))
    email = db.Column(db.String(255))
    status = db.Column(db.String(50))
    priority = db.Column(db.String(50))
    mobile_phone = db.Column(db.String(50))
    direct_line = db.Column(db.String(50))
    switchboard = db.Column(db.String(50))
    other_phone_1 = db.Column(db.String(50))
    other_phone_2 = db.Column(db.String(50))
    job_description = db.Column(db.Text)
    company_website = db.Column(db.Text)
    years_in_position = db.Column(db.Integer)
    years_in_company = db.Column(db.Integer)
    industry = db.Column(db.String(255))
    ca = db.Column(db.Text)
    company_employee_count = db.Column(db.Integer)
    company_employee_range = db.Column(db.String(50))
    company_year_founded = db.Column(db.Text)
    company_description = db.Column(db.Text)
    vat = db.Column(db.String(50))
    headquarters_pc = db.Column(db.String(255))
    headquarters_city = db.Column(db.String(255))
    address = db.Column(db.Text)

    def __repr__(self):
        return f"<Prospect {self.first_name} {self.last_name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "civility": self.civility,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "company_linkedin": self.company_linkedin,
            "linkedin_url": self.linkedin_url,
            "intent_signal": self.intent_signal,
            "other_1": self.other_1,
            "other_2": self.other_2,
            "other_3": self.other_3,
            "company": self.company,
            "title": self.title,
            "email": self.email,
            "status": self.status,
            "priority": self.priority,
            "mobile_phone": self.mobile_phone,
            "direct_line": self.direct_line,
            "switchboard": self.switchboard,
            "other_phone_1": self.other_phone_1,
            "other_phone_2": self.other_phone_2,
            "job_description": self.job_description,
            "company_website": self.company_website,
            "years_in_position": self.years_in_position,
            "years_in_company": self.years_in_company,
            "industry": self.industry,
            "ca": self.ca,
            "company_employee_count": self.company_employee_count,
            "company_employee_range": self.company_employee_range,
            "company_year_founded": self.company_year_founded,
            "company_description": self.company_description,
            "vat": self.vat,
            "headquarters_pc": self.headquarters_pc,
            "headquarters_city": self.headquarters_city,
            "address": self.address
        }
