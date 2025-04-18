from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timezone, timedelta

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for('rwd'))


@app.route("/rwd")
def rwd():
    return render_template("rwd.html")


if __name__ == "__main__":
    app.run()