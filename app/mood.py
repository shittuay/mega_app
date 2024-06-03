from flask import Blueprint, render_template, url_for, flash, redirect
from app import db
from app.models import Mood
from app.forms import MoodForm

mood_bp = Blueprint('mood', __name__)

@mood_bp.route('/')
def index():
    moods = Mood.query.order_by(Mood.date.desc()).all()
    return render_template('mood/index.html', moods=moods)

@mood_bp.route('/add', methods=['GET', 'POST'])
def add_mood():
    form = MoodForm()
    if form.validate_on_submit():
        mood = Mood(
            title=form.title.data, 
            description=form.description.data
        )
        db.session.add(mood)
        db.session.commit()
        flash('Mood added!', 'success')
        return redirect(url_for('mood.index'))
    return render_template('mood/add_mood.html', form=form)
