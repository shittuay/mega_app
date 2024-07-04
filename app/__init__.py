from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate, init, migrate as migrate_command, upgrade
from config import Config
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    with app.app_context():
        if not os.path.exists(os.path.join(app.root_path, 'migrations')):
            db.create_all()
            init()
            migrate_command(message='Initial migration')
            upgrade()

    # Register blueprints
    from app.budget import budget_bp
    from app.habit import habit_bp
    from app.task import task_bp
    from app.fitness import fitness_bp
    from app.mood import mood_bp
    from app.coding import coding_bp
    from app.community import community_bp
    from app.motivational import motivational_bp
    from app.weather import weather_bp

    app.register_blueprint(budget_bp, url_prefix='/budget')
    app.register_blueprint(habit_bp, url_prefix='/habit')
    app.register_blueprint(task_bp, url_prefix='/task')
    app.register_blueprint(fitness_bp, url_prefix='/fitness')
    app.register_blueprint(mood_bp, url_prefix='/mood')
    app.register_blueprint(coding_bp, url_prefix='/coding')
    app.register_blueprint(community_bp, url_prefix='/community')
    app.register_blueprint(motivational_bp, url_prefix='/motivational')
    app.register_blueprint(weather_bp, url_prefix='/weather')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
