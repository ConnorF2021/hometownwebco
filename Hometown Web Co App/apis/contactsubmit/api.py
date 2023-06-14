from flask import Blueprint, request, jsonify
import re
import bleach
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

contactform_api = Blueprint('contactsubmit', __name__)
limiter = Limiter(key_func=get_remote_address)

# Global rate limit: maximum 100 form submissions per hour
limiter.limit("100/hour", error_message='Too many form submissions, please try again later, or email hometownwebcompany@gmail.com with your request.')(contactform_api)

@contactform_api.route('/contactsubmit', methods=['POST'])
@limiter.limit("10/minute")  # Rate limit per IP: maximum 10 requests per minute
def contactsubmit():
    form_data = request.form

    # Data from contact form. name of form is contact_form
    name = bleach.clean(form_data.get('name'))
    email = bleach.clean(form_data.get('email'))
    message = bleach.clean(form_data.get('message'))

    # Validate input
    if not all([name, email, message]):
        response = jsonify({'contact_form-response': 'Form submission failure: Fill out the form!'})
        return response

    # Validate email format
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        response = jsonify({'contact_form-response': 'Form submission failure: Invalid email address!'})
        return response

    response = jsonify({'contact_form-response': 'Form submitted successfully, message received!'})
    return response

