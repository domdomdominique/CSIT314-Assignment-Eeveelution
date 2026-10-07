from flask import Flask

from app.entity.db import db


def create_app(test_config=None):
    """Application factory: builds and configures the Flask app."""
    app = Flask(__name__, template_folder="boundary/templates")
    app.config.update(
        SECRET_KEY="dev-change-me",
        SQLALCHEMY_DATABASE_URI="sqlite:///eeveelution.db",
    )
    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    # Boundary layer: one blueprint per actor
    from app.boundary.auth_boundary import auth_bp
    from app.boundary.customer_boundary import customer_bp
    from app.boundary.admin_boundary import admin_bp
    from app.boundary.designer_boundary import designer_bp
    from app.boundary.platform_boundary import platform_bp

    for bp in (auth_bp, customer_bp, admin_bp, designer_bp, platform_bp):
        app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app
