from flask_sqlalchemy import SQLAlchemy
from main import app

# SQLAlchemy会自动的从app对象中的DevConfig中加载链接数据库的配置项
db = SQLAlchemy(app)


class User(db.Model):
    """Represents Protected users"""

    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # backref是用于制定表之间的双向关系。lazy制定SQLAlchemy加载关联对象的方式，dynamic代表在使用的时候，对象才会被加载，如果需要返回的是巨量很大，建议使用这种方式。
    # subquery会在加载post对象之后将与post相关联的对象全部加载。
    posts = db.relationship('Post', backref='users', lazy='dynamic')

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        """define the string format for the instance of user"""
        return "<Model User'{}'>".format(self.username)


class Post(db.Model):
    """Represents Protected posts"""

    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # set the foreign key for Post
    # 用来保证每一篇post都能对应找到一个user，而且一个user能够对应多篇post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Model Post '{}'>".format(self.title)
