from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager 


app= Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = 'Khadija123'

db= SQLAlchemy(app)
Migrate(app,db)


login_manager= LoginManager()
login_manager.init_app(app)
login_manager.login_view='users.login'

def truncate_text(text, length=130):
    if len(text) > length:
        return text[:length] + "..."
    else:
        return text


app.jinja_env.filters['truncate_text'] = truncate_text


from HorizonBlog.Core.views import core 
from HorizonBlog.error_pages.handlers import error_pages
from HorizonBlog.Users.views import users
from HorizonBlog.Posts.views import posts
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(posts)
