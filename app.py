#! /usr/bin/env python3

import json
from flask import Flask, render_template, request

app = Flask(__name__)
material = json.load(open('questions.json', 'r'))


@app.route("/")
def home():
    return render_template("index.html", material=material)


@app.route("/form", methods=["POST", "GET"])
def submit():
    answers = dict()
    if request.method == "POST":
        for i in range(len(material.get("Questions"))):
            answers.update({f"q{i}answer": (request.form[f"q{i}"])})
        with open('answers.json', 'w') as output:
            json.dump(answers, output)
        return "Thanks for submitting."
    else:
        return "What do you want?"


if __name__ == "__main__":
    app.run(debug=True)
