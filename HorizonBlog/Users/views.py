from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required 
from HorizonBlog import db
from HorizonBlog.models import User, Post
from HorizonBlog.Users.forms import RegistrationForm, LoginForm, UpdateUserForm
from HorizonBlog.Users.picture_handler import add_profile_pic


users= Blueprint('users', __name__)

@users.route('/register', methods=["GET", "POST"])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        user= User(email=form.email.data, name=form.name.data, username=form.username.data, password=form.password.data )
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering!')
        return redirect(url_for('users.login'))
    return render_template('registration.html', form=form)

@users.route('/login', methods=["GET", "POST"]) 
def login():
    form= LoginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Log in success!')

            next= request.args.get('next')
            if next == None or not next[0]=='/':
                next=url_for('core.index')
            return redirect(next)
    return render_template('login.html', form= form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))

@users.route('/account', methods=["GET", "POST"]) 
@login_required
def account():
    form= UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username= current_user.username
            pic= add_profile_pic(form.picture.data, username)
            current_user.profile_image= pic
        
        current_user.name= form.name.data
        current_user.username=form.username.data
        current_user.email= form.email.data
        db.session.commit()
        flash('Your account is updated!')
        return redirect(url_for('users.account'))
    elif request.method== 'GET':
        form.name.data= current_user.name
        form.username.data= current_user.username
        form.email.data= current_user.email
    profile_image= url_for('static', filename='profile_pictures/'+current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)
    
@users.route('/<username>') 
def user_posts(username): 
    page= request.args.get('page',1, type=int )
    user= User.query.filter_by(username= username).first_or_404()
    blog_posts= Post.query.filter_by(author=user).order_by(Post.date.desc()).pageinate(page=page,per_page=6)
    return render_template( 'author_posts.html' ,blog_posts=blog_posts, user=user)





