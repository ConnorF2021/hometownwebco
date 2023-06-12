from flask import Blueprint, request, jsonify

contactform_api = Blueprint('contactsubmit', __name__)

@contactform_api.route('/contactsubmit', methods=['POST'])
def contactsubmit():
    form_data = request.form

    # Data from contact form. name of form is contact_form
    name = form_data.get('name')
    email = form_data.get('email')
    message = form_data.get('message')

    if name and email and message:
        response = jsonify({'contact_form-response': 'Form submitted successfully, message received!'})
        return response
    else:
        response = jsonify({'contact_form-response': 'Form submission failure: Fill out the form!'})
        return response
