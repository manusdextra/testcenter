from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    teacher = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    questions = db.relationship('Question', backref='exampaper', lazy=True)

    def __repr__(self):
        return '<Exam {}>'.format(self.name)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam = db.Column(
        db.Integer,
        db.ForeignKey('exam.id'),
        nullable=False)
    prompt = db.Column(db.Text)
    answers = db.relationship('Answer', backref='questionnumber', lazy=True)

    def __repr__(self):
        return '<Question {}>'.format(self.prompt)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'),
                            nullable=False)
    body = db.Column(db.String(32), unique=True)
    correct = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Answer {}>'.format(self.body)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
