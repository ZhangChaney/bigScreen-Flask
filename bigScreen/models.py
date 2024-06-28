from bigScreen import db


class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), unique=False, nullable=False)
    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(64), unique=True)
    role = db.Column(db.Integer, nullable=False)

    def __init__(self, username, password, phone=None, email=None, role=2):
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.role = role

    def __repr__(self):
        return f'<User {self.username!r}>'

    def to_dict(self):
        return {
            'userid': self.userid,
            'username': self.username,
            'phone': self.phone,
            'email': self.email,
            'role': self.role
        }
