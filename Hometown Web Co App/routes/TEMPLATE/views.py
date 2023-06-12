from flask import Blueprint, render_template

example_bp = Blueprint('example', __name__, template_folder='templates')

@example_bp.route('/EXAMPLEROUTE')
def EXAMPLEROUTE():
    return 'This is an example route'