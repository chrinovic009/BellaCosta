from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired

class MenuForm(FlaskForm):
    nom = StringField("Nom du plat", validators=[DataRequired()])
    description = TextAreaField("Description")
    prix = FloatField("Prix", validators=[DataRequired()])
    category_id = SelectField("Catégorie", coerce=int)
    is_featured = BooleanField("Plat recommandé")
    submit = SubmitField("Enregistrer")

class CategoryForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()])
    ordre = StringField("Ordre d'affichage")
    submit = SubmitField("Enregistrer")

class ChefForm(FlaskForm):
    nom = StringField("Nom", validators=[DataRequired()])
    poste = StringField("Poste")
    bio = TextAreaField("Biographie")
    submit = SubmitField("Ajouter")

class ReservationForm(FlaskForm):
    nom_client = StringField("Nom", validators=[DataRequired()])
    telephone = StringField("Téléphone", validators=[DataRequired()])
    email = StringField("Email")
    date = StringField("Date", validators=[DataRequired()])
    heure = StringField("Heure")
    personnes = StringField("Personnes", validators=[DataRequired()])
    message = TextAreaField("Message")
    submit = SubmitField("Réserver")

class TestimonialForm(FlaskForm):
    nom = StringField("Nom")
    note = SelectField("Note", choices=[(i, i) for i in range(1, 6)], coerce=int)
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Envoyer")

