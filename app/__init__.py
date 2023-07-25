from flask import Flask

def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    # Register your blueprints here
    from .views import api_bp
    app.register_blueprint(api_bp)
    return app