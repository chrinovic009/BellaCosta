from app import login_manager
from app.extensions import db, bcrypt, csrf
from flask_login import UserMixin
from datetime import datetime

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    ordre = db.Column(db.Integer, default=0)

    menus = db.relationship("Menu", backref="category", lazy=True)

class Menu(db.Model):
    __tablename__ = "menus"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    prix = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255))
    is_featured = db.Column(db.Boolean, default=False)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

class Chef(db.Model):
    __tablename__ = "chefs"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    poste = db.Column(db.String(100))
    bio = db.Column(db.Text)
    photo = db.Column(db.String(255))

class Reservation(db.Model):
    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True)
    nom_client = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))
    date = db.Column(db.Date, nullable=False)
    heure = db.Column(db.String(10))
    personnes = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class Testimonial(db.Model):
    __tablename__ = "testimonials"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    note = db.Column(db.Integer)
    message = db.Column(db.Text)
    is_visible = db.Column(db.Boolean, default=True)

class Gallery(db.Model):
    __tablename__ = "gallery"

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100))
    image = db.Column(db.String(255))

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id", name="fk_gallery_category"),
        nullable=False
    )

    category = db.relationship("Category", backref="gallery_items")

class RestaurantInfo(db.Model):
    __tablename__ = "restaurant_info"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    adresse = db.Column(db.String(255))
    telephone = db.Column(db.String(50))
    email = db.Column(db.String(120))
    map_iframe = db.Column(db.Text)
