from flask import render_template, request, flash, redirect, url_for
from app import app
from app.forms import LoginForm
import json

material = json.load(open('questions.json', 'r'))


@app.route("/")
def home():
    return render_template("index.html",
                           title="Home")


@app.route("/placementtest", methods=["POST", "GET"])
def placementtest():
    if request.method == "GET":
        return render_template("placementtest.html",
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data,
            form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Log In', form=form)
