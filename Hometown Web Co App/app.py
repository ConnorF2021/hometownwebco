from flask import Flask

# IMPORTED ROUTES FROM BLUEPRINTS
from routes.home.views import home_bp
from routes.about.views import about_bp
from routes.contact.views import contact_bp
from routes.clientportal.views import clientportal_bp
from routes.tools.views import tools_bp

# IMPORTED APIS FROM BLUEPRINTS
from apis.contactsubmit.api import contactform_api
from apis.staticpagesubmit.api import staticpageform_api
from apis.webappsubmit.api import webappform_api
from apis.customsitesubmit.api import customsiteform_api

app = Flask(__name__)

# REGISTERED AND ACTIVATED ROUTES
app.register_blueprint(home_bp) # Landing page /
app.register_blueprint(about_bp) # About us page /about
app.register_blueprint(contact_bp) # Contact us page /contact
app.register_blueprint(clientportal_bp) # Client portal page /clientportal
app.register_blueprint(tools_bp) # Web tools page /tools

# REGISTERED AND ACTIVATED APIS
app.register_blueprint(contactform_api) # Contact form submit API over /contactsubmit
app.register_blueprint(staticpageform_api) # Inquiry modal submit API over /staticpagesubmit
app.register_blueprint(webappform_api) # Inquiry modal submit API over /webappsubmit
app.register_blueprint(customsiteform_api) # Inquiry modal submit API over /customsitesubmit

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)