"""
@author Adrian Rybarczyk
"""


from flask_login import UserMixin
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.model):
    id = db.Column(db.Interger, primary_key = True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(150), index=True, unique=True)
    password_hash = db.Column(db.String(150))
    joined_at = db.Column(db.Datetime(), default = datetime.utcnow, index= True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
