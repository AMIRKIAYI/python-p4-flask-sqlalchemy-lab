from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Naming convention to handle migrations more smoothly
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# Zookeeper Model
class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String, nullable=False)

    # Relationship to animals (One-to-many)
    animals = db.relationship('Animal', backref='zookeeper', lazy=True)

    def __repr__(self):
        return f'<Zookeeper {self.name}, born on {self.birthday}>'

# Enclosure Model
class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String, nullable=False)  # e.g., grass, sand, water
    open_to_visitors = db.Column(db.Boolean, default=True)

    # Relationship to animals (One-to-many)
    animals = db.relationship('Animal', backref='enclosure', lazy=True)

    def __repr__(self):
        return f'<Enclosure {self.environment}, Open to visitors: {self.open_to_visitors}>'

# Animal Model
class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)

    # Foreign keys to zookeeper and enclosure
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), nullable=False)

    def __repr__(self):
        return f'<Animal {self.name} ({self.species})>'
