def register_routes(app):
    from .prospect_routes import prospect_bp
    app.register_blueprint(prospect_bp)
