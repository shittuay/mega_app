# app/task.py

from flask import Blueprint, render_template

task_bp = Blueprint('task', __name__)

@task_bp.route('/')
def index():
    return render_template('index.html')
