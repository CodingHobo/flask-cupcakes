"""Flask app for Cupcakes"""

import os

from flask import Flask, render_template, redirect, flash, request
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")



connect_db(app)

@app.get("/api/cupcakes")
def get_all_cupcakes():

    cupcakes = Cupcake.query.all()
    serialized = [c.serialized() for c in cupcakes]

    return jsonify(cupcakes=serialized)
