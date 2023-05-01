"""Flask app for Cupcakes"""

import os

from flask import Flask, render_template, redirect, flash, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db,Cupcake, db


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes")



connect_db(app)

@app.get("/api/cupcakes")
def get_all_cupcakes():

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake = serialized)

@app.post('/api/cupcakes')
def create_cupcake():
    """Create cupcake from posted JSON data & return it.

    Returns JSON {'cupcake': {id, flavor, size, rating, image_url}}
    """

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image_url = request.json['image_url']

    new_cupcake = Cupcake(flavor=flavor,
                          size=size,
                          rating=rating,
                          image_url=image_url)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    # Return w/status code 201 --- return tuple (json, status)
    return (jsonify(cupcake=serialized), 201)




