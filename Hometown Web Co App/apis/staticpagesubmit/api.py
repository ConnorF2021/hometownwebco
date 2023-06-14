from flask import Blueprint, request, jsonify
import re
import bleach
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

staticpageform_api = Blueprint('staticpagesubmit', __name__)
limiter = Limiter(key_func=get_remote_address)

# Global rate limit: maximum 100 form submissions per hour
limiter.limit("100/hour", error_message='Too many form submissions, please try again later, or email hometownwebcompany@gmail.com with your request.')(staticpageform_api)

@staticpageform_api.route('/staticpagesubmit', methods=['POST'])
@limiter.limit("10/minute")  # Rate limit per IP: maximum 10 requests per minute
def staticpagesubmit():
    form_data = request.form

    # Data from static page form. name of form is staticpage_form
    name = bleach.clean(form_data.get('name'))
    email = bleach.clean(form_data.get('email'))

    # Validate input
    if not all([name, email]):
        response = jsonify({'staticpage_form-response': 'Form submission failure: Fill out the form!'})
        return response

    # Validate email format
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        response = jsonify({'staticpage_form-response': 'Form submission failure: Invalid email address!'})
        return response

    response = jsonify({'staticpage_form-response': 'Form submitted successfully, inquiry received!'})
    return response

