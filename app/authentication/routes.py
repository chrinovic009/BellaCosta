from flask import render_template, flash, redirect, url_for, jsonify, request
from app.utils.authentication import blueprint




# ---------------------------------------------------------------------------- pour les pages ----------------------------------------------------------------#
# pour la page de connexion
@blueprint.route('/login')
def login():

    return render_template('login/login.html', page_active="login")
