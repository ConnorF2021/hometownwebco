from flask import Blueprint, request, jsonify
import re
import bleach
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

webappform_api = Blueprint('webappsubmit', __name__)
limiter = Limiter(key_func=get_remote_address)

# Global rate limit: maximum 100 form submissions per hour
limiter.limit("100/hour", error_message='Too many form submissions, please try again later, or email hometownwebcompany@gmail.com with your request.')(webappform_api)

@webappform_api.route('/webappsubmit', methods=['POST'])
@limiter.limit("10/minute")  # Rate limit per IP: maximum 10 requests per minute
def webappsubmit():
    form_data = request.form

    # Data from webapp form. name of form is webapp_form
    name = bleach.clean(form_data.get('name'))
    email = bleach.clean(form_data.get('email'))

    # Validate input
    if not all([name, email]):
        response = jsonify({'webapp_form-response': 'Form submission failure: Fill out the form!'})
        return response

    # Validate email format
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        response = jsonify({'webapp_form-response': 'Form submission failure: Invalid email address!'})
        return response

    response = jsonify({'webapp_form-response': 'Form submitted successfully, inquiry received!'})
    return response

