import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'constellation_pr0ject'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:bilibo@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False