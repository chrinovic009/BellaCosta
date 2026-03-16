from flask import render_template, flash, redirect, url_for, jsonify, request
from app.utils.home import blueprint
from app import db
from app.utils.home.models import Menu, Category, Chef, Gallery, Reservation, RestaurantInfo
from app.utils.home.forms import MenuForm, CategoryForm, ChefForm, ReservationForm, TestimonialForm




# ---------------------------------------------------------------------------- pour les pages ----------------------------------------------------------------#
# pour la page d'acceuil
@blueprint.route('/')
def home():

    return render_template('home/index.html', page_active="home")

# pour la page d'a propos
@blueprint.route('/about')
def about():

    return render_template('home/about.html', page_active="about")

# pour la page d menu
@blueprint.route('/menu')
def menu():

    return render_template('home/menu.html', page_active="menu")

# pour la page de gallerie
@blueprint.route('/gallery')
def gallery():

    return render_template('home/gallery.html', page_active="gallery")

# pour la page de contact
@blueprint.route('/contact')
def contact():

    return render_template('home/contact.html', page_active="contact")


