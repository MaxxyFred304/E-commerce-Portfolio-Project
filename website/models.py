from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from .models import db

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Add a category field

    # You might want to add more fields like image URL, brand, etc.

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}', '{self.category}')"

class Laptop(Product):
    id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    processor = db.Column(db.String(50), nullable=False)
    ram = db.Column(db.Integer, nullable=False)
    storage = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Laptop('{self.name}', '{self.price}', '{self.processor}', '{self.ram}', '{self.storage}')"

class Computer(Product):
    id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    processor = db.Column(db.String(50), nullable=False)
    ram = db.Column(db.Integer, nullable=False)
    storage = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Computer('{self.name}', '{self.price}', '{self.processor}', '{self.ram}', '{self.storage}')"

class Tablet(Product):
    id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    storage_capacity = db.Column(db.String(50), nullable=False)
    screen_size = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Tablet('{self.name}', '{self.price}', '{self.storage_capacity}', '{self.screen_size}')"
