from flask import Flask
from backend.config import Config
from app.models import db
from app.routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
register_routes(app)
@app.route('/test')
def test():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)

    