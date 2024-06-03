from flask import Blueprint, render_template, url_for, flash, redirect, request
from app import db
from app.models import Habit, HabitRecord
from app.forms import HabitForm, HabitRecordForm
from datetime import date

habit_bp = Blueprint('habit', __name__)

@habit_bp.route('/')
def index():
    habits = Habit.query.all()
    return render_template('habit/index.html', habits=habits)

@habit_bp.route('/add', methods=['GET', 'POST'])
def add_habit():
    form = HabitForm()
    if form.validate_on_submit():
        habit = Habit(name=form.name.data, description=form.description.data)
        db.session.add(habit)
        db.session.commit()
        flash('Your habit has been added!', 'success')
        return redirect(url_for('habit.index'))
    return render_template('habit/add_habit.html', title='Add Habit', form=form)

@habit_bp.route('/<int:habit_id>', methods=['GET', 'POST'])
def habit_detail(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    form = HabitRecordForm()
    if form.validate_on_submit():
        today = date.today()
        record = HabitRecord.query.filter_by(habit_id=habit.id, date=today).first()
        if record:
            record.status = form.status.data
        else:
            record = HabitRecord(date=today, status=form.status.data, habit_id=habit.id)
            db.session.add(record)
        db.session.commit()
        flash('Your habit record has been updated!', 'success')
        return redirect(url_for('habit.habit_detail', habit_id=habit.id))
    records = HabitRecord.query.filter_by(habit_id=habit.id).order_by(HabitRecord.date.desc()).all()
    return render_template('habit/habit_detail.html', title=habit.name, habit=habit, form=form, records=records)
