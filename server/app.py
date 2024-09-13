#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

# Animal view by ID
@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get_or_404(id)
    response = f"<ul><li>Name: {animal.name}</li><li>Species: {animal.species}</li>"
    response += f"<li>Zookeeper: {animal.zookeeper.name}</li>"
    response += f"<li>Enclosure: {animal.enclosure.environment}</li></ul>"
    return make_response(response, 200)

# Zookeeper view by ID
@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get_or_404(id)
    response = f"<ul><li>Name: {zookeeper.name}</li><li>Birthday: {zookeeper.birthday}</li>"
    response += "<li>Animals:</li><ul>"
    for animal in zookeeper.animals:
        response += f"<li>{animal.name} ({animal.species})</li>"
    response += "</ul></ul>"
    return make_response(response, 200)

# Enclosure view by ID
@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get_or_404(id)
    response = f"<ul><li>Environment: {enclosure.environment}</li><li>Open to Visitors: {enclosure.open_to_visitors}</li>"
    response += "<li>Animals:</li><ul>"
    for animal in enclosure.animals:
        response += f"<li>{animal.name} ({animal.species})</li>"
    response += "</ul></ul>"
    return make_response(response, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
