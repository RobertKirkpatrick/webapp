from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    # Flask-Login provides a mixin class called UserMixin that includes generic
    # implementations that are appropriate for most user model classes.
    id = db.Column(db.Integer, primary_key=True) #id field is a primary key
    username = db.Column(db.String(64), index=True, unique=True)
    twofact = db.Column(db.String(10), index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    #The __repr__ method tells Python how to print objects of this class, which is going to be useful for debugging.
    #You can see the __repr__() method in action in the Python interpreter session below:
    def __repr__(self):
        return '<User {}>'.format(self.username)

# flask-login extension expects that the application will
# configure a user loader function, that can be called to load a user given the ID.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))