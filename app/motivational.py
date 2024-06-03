from flask import Blueprint, render_template, url_for, flash, redirect
from app import db
from app.models import MotivationalQuote
from app.forms import MotivationalQuoteForm

motivational_bp = Blueprint('motivational', __name__)

@motivational_bp.route('/')
def index():
    quotes = MotivationalQuote.query.order_by(MotivationalQuote.date_posted.desc()).all()
    return render_template('motivational/index.html', quotes=quotes)

@motivational_bp.route('/add', methods=['GET', 'POST'])
def add_quote():
    form = MotivationalQuoteForm()
    if form.validate_on_submit():
        quote = MotivationalQuote(
            content=form.content.data, 
            author=form.author.data
        )
        db.session.add(quote)
        db.session.commit()
        flash('Your motivational quote has been added!', 'success')
        return redirect(url_for('motivational.index'))
    return render_template('motivational/add_quote.html', form=form)
