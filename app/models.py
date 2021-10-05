from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.Text)
    answers = db.relationship('Answer', backref='question', lazy=True)

    def __repr__(self):
        return '<Question {}>'.format(self.prompt)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'),
                            nullable=False)
    body = db.Column(db.String(32), unique=True)
    correct = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Answer {}>'.format(self.Answer)
