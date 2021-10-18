from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
import json

material = json.load(open('questions.json', 'r'))


@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Home")


@app.route("/placementtest", methods=["POST", "GET"])
@login_required
def placementtest():
    if request.method == "GET":
        return render_template(
            "placementtest.html",
            material=material,
            title=material["SectionTitle"])
    if request.method == "POST":
        answers = dict()
        for i in range(len(material.get("Questions"))):
            try:
                answers.update({f"q{i}answer": (request.form[f"q{i}"])})
            except KeyError:
                answers.update({f"q{i}answer": None})
        with open('answers.json', 'w') as output:
            json.dump(answers, output)
        return render_template("message.html",
                               message="Thanks for submitting.")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Log In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
