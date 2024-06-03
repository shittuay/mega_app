from flask import Blueprint, render_template, url_for, flash, redirect
from app import db
from app.models import BudgetTransaction
from app.forms import BudgetTransactionForm

budget_bp = Blueprint('budget', __name__)

@budget_bp.route('/')
def index():
    transactions = BudgetTransaction.query.order_by(BudgetTransaction.date.desc()).all()
    return render_template('budget/index.html', transactions=transactions)

@budget_bp.route('/add', methods=['GET', 'POST'])
def add_transaction():
    form = BudgetTransactionForm()
    if form.validate_on_submit():
        transaction = BudgetTransaction(
            title=form.title.data, 
            amount=form.amount.data, 
            type=form.type.data
        )
        db.session.add(transaction)
        db.session.commit()
        flash('Transaction added!', 'success')
        return redirect(url_for('budget.index'))
    return render_template('budget/add_transaction.html', form=form)
