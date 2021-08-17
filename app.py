#! /usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form", methods=['POST'])
def form():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
