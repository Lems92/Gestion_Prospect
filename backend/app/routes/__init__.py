def register_routes(app):
    from .prospect_routes import prospect_bp
    from .company_routes import company_bp
    from .file_upload_routes import file_upload_bp
    app.register_blueprint(prospect_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(file_upload_bp)