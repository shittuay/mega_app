from flask import Blueprint, render_template, url_for, flash, redirect
from app import db
from app.models import CommunityPost
from app.forms import CommunityPostForm

community_bp = Blueprint('community', __name__)

@community_bp.route('/')
def index():
    posts = CommunityPost.query.order_by(CommunityPost.date_posted.desc()).all()
    return render_template('community/index.html', posts=posts)

@community_bp.route('/add', methods=['GET', 'POST'])
def add_post():
    form = CommunityPostForm()
    if form.validate_on_submit():
        post = CommunityPost(
            title=form.title.data, 
            author=form.author.data, 
            content=form.content.data
        )
        db.session.add(post)
        db.session.commit()
        flash('Your post has been added!', 'success')
        return redirect(url_for('community.index'))
    return render_template('community/add_post.html', form=form)
