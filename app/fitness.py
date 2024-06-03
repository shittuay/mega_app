from flask import Blueprint, render_template, url_for, flash, redirect
from app import db
from app.models import Workout
from app.forms import WorkoutForm

fitness_bp = Blueprint('fitness', __name__)

@fitness_bp.route('/')
def index():
    workouts = Workout.query.order_by(Workout.date.desc()).all()
    return render_template('fitness/index.html', workouts=workouts)

@fitness_bp.route('/add', methods=['GET', 'POST'])
def add_workout():
    form = WorkoutForm()
    if form.validate_on_submit():
        workout = Workout(
            title=form.title.data, 
            description=form.description.data, 
            duration=form.duration.data
        )
        db.session.add(workout)
        db.session.commit()
        flash('Your workout has been added!', 'success')
        return redirect(url_for('fitness.index'))
    return render_template('fitness/add_workout.html', form=form)
