from flask import Blueprint, render_template

tools_bp = Blueprint('tools', __name__, template_folder='templates')

@tools_bp.route('/tools')
def tools():
    return render_template("tools.html")