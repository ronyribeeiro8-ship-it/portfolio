from flask import Flask
from config import config


def create_app(env="development"):
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="static",
    )
    app.config.from_object(config[env])

    # Registra blueprints (rotas)
    from .controllers.home_controller import home_bp
    from .controllers.projects_controller import projects_bp
    from .controllers.contact_controller import contact_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(contact_bp)

    return app
