from flask import Blueprint, render_template

clientportal_bp = Blueprint('clientportal', __name__, template_folder='templates')

@clientportal_bp.route('/clientportal')
def clientportal():
    return render_template("clientportal.html")

@clientportal_bp.route('/clientportal/<user>')
def clientportaluser(user):
    return render_template("clientportaluser.html")