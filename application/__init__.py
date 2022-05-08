import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from . import auth
from . import blog

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, instance_relative_config=True)

app.debug = True

app.config['DATABASE'] = os.path.join(app.root_path, 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'dev'
app.config['SECRET_KEY'] = 'dev'


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

app.register_blueprint(auth.bp)

app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    username = ''

    def __init__(self, title, body, author_id):
        self.title = title
        self.body = body
        self.author_id = author_id

    @staticmethod
    def withUser(post, user):
        return {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'created': post.created,
            'author_id': post.author_id,
            'username': user.username
        }



# Only use for initializing the db
# db.create_all()
# db.session.commit()

