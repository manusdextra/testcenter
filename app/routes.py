from flask import Flask, render_template, request
from app import app
import json

material = json.load(open('questions.json', 'r'))


@app.route("/")
def home():
    return render_template("index.html",
                           title="Home")


@app.route("/placementtest")
def placementtest():
    return render_template("placementtest.html",
                           material=material,
                           title=material["SectionTitle"])


@app.route("/submit", methods=["POST", "GET"])
def submit():
    answers = dict()
    if request.method == "POST":
        for i in range(len(material.get("Questions"))):
            try:
                answers.update({f"q{i}answer": (request.form[f"q{i}"])})
            except KeyError:
                answers.update({f"q{i}answer": None})
        with open('answers.json', 'w') as output:
            json.dump(answers, output)
        return "Thanks for submitting."
    else:
        return "What do you want?"
