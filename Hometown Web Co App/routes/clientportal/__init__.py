from flask import Blueprint

# Create the blueprint object
main_bp = Blueprint('main', __name__)

# Import the views associated with the blueprint
from . import views