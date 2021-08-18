#! /usr/bin/env python3

import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html",
                           material=json.load(open('questions.json', 'r')))


if __name__ == "__main__":
    app.run(debug=True)
