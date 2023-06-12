from flask import Blueprint, request

EXAMPLE_api = Blueprint('EXAMPLE', __name__)

@EXAMPLE_api.route('/EXAMPLE', methods=['POST'])
def EXAMPLE():
    form_data = request.form
    # Or alternatively, use request.values to access form data
    # form_data = request.values

    # Accessing individual form fields
    name = form_data.get('name')
    email = form_data.get('email')
    message = form_data.get('message')

    # Perform necessary actions with the form data
    # For example, you can store it in a database, send an email, etc.

    # Return a response or redirect to another page
    return 'Form submitted successfully'
