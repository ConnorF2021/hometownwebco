from flask import Blueprint, render_template

adminpanel_bp = Blueprint('adminpanel', __name__, template_folder='templates')

@adminpanel_bp.route('/adminpanel')
def adminpanel():
    return render_template("adminpanel.html")