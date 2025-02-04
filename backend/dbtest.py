import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from app import app, db


with app.app_context():
    try:
        conn = db.engine.connect()
        print("Connexion à la base réussie !")
        conn.close()
    except Exception as e:
        print(f"Erreur de connexion : {e}")