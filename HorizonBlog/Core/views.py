from flask import render_template, request , Blueprint, redirect, url_for, flash
from HorizonBlog.Core.forms import ContactForm
from HorizonBlog.models import Post, User
core= Blueprint('core', __name__)


@core.route('/')
def index():
    author = User.query.get_or_404(7)
    first_post = Post.query.filter_by(author=author).first()
    second_post = Post.query.filter_by(author=author).offset(1).first()
    third_post = Post.query.filter_by(author=author).offset(2).first()

    total_items = 30
    items_per_page = 5
    total_pages = (total_items + items_per_page - 1) // items_per_page
    return render_template('index.html',total_pages=total_pages,first_post=first_post,second_post=second_post,third_post=third_post , author=author)

@core.route('/info')
def info():
    latest_posts = Post.query.order_by(Post.date.desc()).all()
    total_items = 30
    items_per_page = 5
    total_pages = (total_items + items_per_page - 1) // items_per_page
    return render_template('blogsbyTopic.html',total_pages=total_pages,latest_posts=latest_posts )

@core.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('core.contact'))

    return render_template('contact.html', form=form)

@core.route('/ourstory')
def ourstory():
    return render_template('ourstory.html')