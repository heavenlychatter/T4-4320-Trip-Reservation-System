from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration and extension initialization
    app.config['SECRET_KEY'] = 'secret-key'

    from functions import databaseFunctions
    databaseFunctions.register(app)

    # Register blueprints or routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app