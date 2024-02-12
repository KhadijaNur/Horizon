from flask import render_template, request , Blueprint, redirect, url_for, flash
from flask_login import current_user, login_required
from HorizonBlog import db 
from HorizonBlog.models import Post
from HorizonBlog.Posts.forms import PostForm


posts= Blueprint('posts', __name__)




@posts.route('/create', methods=['GET','POST'])
@login_required
def create():
    form= PostForm()
    if form.validate_on_submit():
        post= Post(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form )


@posts.route('/<int:post_id>', methods=['GET','POST'])
def post(post_id):
    post= Post.query.get_or_404(post_id)
    latest_posts = Post.query.filter(Post.id != post_id).order_by(Post.date.desc()).limit(4).all()
    text= post.text
    formatted_sql = text.replace('\n', '<br>').replace(' ', '&nbsp;')

    return render_template('post.html', title=post.title, date=post.date, post=post , latest_posts=latest_posts, text=formatted_sql)

@posts.route('/<int:post_id>/update', methods=['GET','POST'])
@login_required
def update(post_id):
    post= Post.query.get_or_404(post_id)
    if post.author != current_user: 
        abort(403)
    form= PostForm()
    if form.validate_on_submit():

        post.title=form.title.data
        post.text=form.text.data
        db.session.commit()
        flash('Post was updated')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method== 'GET':
        form.title.data=post.title
        form.text.data=post.text

    return render_template('create_post.html', title='Update Post', form=form )

@posts.route('/<int:post_id>/delete', methods=['GET','POST'])
@login_required
def delete(post_id):
    post= Post.query.get_or_404(post_id)
    if post.author != current_user: 
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post was deleted')
    return redirect(url_for('core.index'))

