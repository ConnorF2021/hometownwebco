from flask import Blueprint, request, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import re
import bleach
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

clientportalform_api = Blueprint('clientportalsubmit', __name__)
limiter = Limiter(key_func=get_remote_address)

# Global rate limit: maximum 100 form submissions per hour
limiter.limit("100/hour", error_message='Too many form submissions, please try again later, or email hometownwebcompany@gmail.com with your request.')(clientportalform_api)

@clientportalform_api.route('/clientportalsubmit', methods=['POST'])
@limiter.limit("10/minute")  # Rate limit per IP: maximum 10 requests per minute
def clientportalsubmit():
    form_data = request.form

    # Data from static page form. name of form is clientportal_form
    email = bleach.clean(form_data.get('email'))
    password = bleach.clean(form_data.get('password'))

    # Validate input
    if not all([name, email]):
        response = jsonify({'clientportal_form-response': 'Form submission failure: Fill out the form!'})
        return response

    # Validate email format
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        response = jsonify({'clientportal_form-response': 'Form submission failure: Invalid email address!'})
        return response

    response = jsonify({'clientportal_form-response': 'Form submitted successfully, inquiry received!'})
    return response

