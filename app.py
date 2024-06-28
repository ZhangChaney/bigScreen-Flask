# coding: utf-8
# author: chaney
# file  : app.py
# time  : 2024-06-19
from bigScreen import create_app, db
from bigScreen.models import User

app = create_app()


def generate_users():
    user1 = User(username='admin', email='admin@chaney.edu', password='123456', phone='13188995566', role=1)
    user2 = User(username='jackson', email='jackson@chaney.edu', password='123456', phone='13288995567')
    user3 = User(username='kris', email='kris@chaney.edu', password='123456', phone='13388995568')
    user4 = User(username='janey', email='janey@chaney.edu', password='123456', phone='13488995569')
    db.session.add_all([user1, user2, user3, user4])
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        generate_users()
    app.run(host='0.0.0.0', port=8888)
