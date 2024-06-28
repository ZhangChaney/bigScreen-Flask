from bigScreen import db


class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), unique=False)
    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(64), unique=True)

    def __init__(self, username=None, password=None, phone=None, email=None):
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f'<User {self.username!r}>'

    def to_dict(self):
        return {
            'userid': self.userid,
            'username': self.username,
            'phone': self.phone,
            'email': self.email
        }
