from datetime import datetime
from app import db

class BudgetTransaction(db.Model):
    __tablename__ = 'BudgetTransaction'
    __table_args__ = {'extend_existing=True'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

class Task(db.Model):
    __tablename__ = 'Task'
    __table_args__ = {'extend_existing=True'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    due_date = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Task('{self.title}', '{self.due_date}', '{self.completed}')"

class Workout(db.Model):
    __tablename__ = 'workout'
    __table_args__ = {'extend_existing=True'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)
    
class Mood(db.Model):
    __tablename__ = 'Mood'
    __table_args__ = {'extend_existing=True'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Mood('{self.title}', '{self.date}')"
    
class CodingEntry(db.Model):
    __tablename__ = 'CodingEntry'
    __table_args__ = {'extend_existing=True'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"CodingEntry('{self.title}', '{self.date_posted}')"
    
class CommunityPost(db.Model):
    __tablename__ = 'CommunityPost'
    __table_args__ = {'extend_existing=True'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"CommunityPost('{self.title}', '{self.author}', '{self.date_posted}')"

class Workout(db.Model):
    __tablename__ = 'workout'
    __table_args__ = {'extend_existing=True'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)  # duration in minutes

    def __repr__(self):
        return f"Workout('{self.title}', '{self.date}', '{self.duration}')"

class MotivationalQuote(db.Model):
    __tablename__ = 'MotivationalQuote'
    __table_args__ = {'extend_existing=True'}
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"MotivationalQuote('{self.author}', '{self.date_posted}')"


class Habit(db.Model):
    __tablename__ = 'habit'
    __table_args__ = {'extend_existing=True'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    records = db.relationship('HabitRecord', backref='habit', lazy=True)
    

    def __repr__(self):
        return f"Habit('{self.name}', '{self.creation_date}')"

class HabitRecord(db.Model):
    __tablename__ = 'habitRecord'
    __table_args__ = {'extend_existing=True'}
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    status = db.Column(db.Boolean, nullable=False, default=False)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)

    def __repr__(self):
        return f"HabitRecord('{self.date}', '{self.status}')"


# Add similar models for mood journal, coding journal, community board, motivational app, and weather app
