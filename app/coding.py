from flask import Blueprint, render_template, url_for, flash, redirect, request
from app import db
from app.models import CodingEntry
from app.forms import CodingEntryForm

coding_bp = Blueprint('coding', __name__)

@coding_bp.route('/')
def index():
    entries = CodingEntry.query.order_by(CodingEntry.date_posted.desc()).all()
    return render_template('coding/index.html', entries=entries)

@coding_bp.route('/add', methods=['GET', 'POST'])
def add_entry():
    form = CodingEntryForm()
    if form.validate_on_submit():
        entry = CodingEntry(
            title=form.title.data, 
            content=form.content.data
        )
        db.session.add(entry)
        db.session.commit()
        flash('Your coding entry has been added!', 'success')
        return redirect(url_for('coding.index'))
    return render_template('coding/add_entry.html', form=form)

@coding_bp.route('/<int:entry_id>', methods=['GET'])
def coding_detail(entry_id):
    entry = CodingEntry.query.get_or_404(entry_id)
    return render_template('coding/coding_detail.html', entry=entry)
