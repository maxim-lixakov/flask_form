from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user_data_name'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    middle_name = db.Column(db.String())
    bornData = db.Column(db.Date())
    gender = db.Column(db.String())


class User_data(db.Model):
    __tablename__ = 'user_data'

    id = db.Column(db.Integer, primary_key=True)
    citizenship = db.Column(db.String())
    comment = db.Column(db.String())
    education = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user_data_name.id'))

