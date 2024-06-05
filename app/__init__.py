from flask import Flask
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

class Workout(db.Model):
    __tablename__ = 'workout'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)

class Workout(db.Model):
    __tablename__ = 'budget'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    # rest of your model definition...

class Workout(db.Model):
    __tablename__ = 'habit'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)

class Workout(db.Model):
    __tablename__ = 'task'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    
class Workout(db.Model):
    __tablename__ = 'mood'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    
class Workout(db.Model):
    __tablename__ = 'weather'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    
class Workout(db.Model):
    __tablename__ = 'coding'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    
class Workout(db.Model):
    __tablename__ = 'motivational'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    
class Workout(db.Model):
    __tablename__ = 'community'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)

def create_app():
    app = Flask(__name__)  # Define the "app" variable

    with app.app_context():
        if not os.path.exists(os.path.join(app.root_path, 'migrations')):
            db.create_all()
            from flask_migrate import init, migrate, upgrade
            init()
            migrate(message='Initial migration')
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

    return app
