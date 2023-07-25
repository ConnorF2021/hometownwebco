import os
import subprocess
from flask import Blueprint, request, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

update_api = Blueprint('update', __name__)
limiter = Limiter(key_func=get_remote_address)

# Global rate limit: maximum 100 form submissions per hour
limiter.limit("100/hour", error_message='Too many form submissions, please try again later, or email hometownwebcompany@gmail.com with your request.')(update_api)

github_secret = os.environ.get('Xy3@kG#8hT$mN6*p2RqV9oLsZ1Fb&zAe5M7d')  # Replace with your environment variable name

@update_api.route('/update', methods=['POST'])
@limiter.limit("10/minute")  # Rate limit per IP: maximum 10 requests per minute
def update():
    if request.method == 'POST':
        # Verify the GitHub secret
        if github_secret and github_secret == request.headers.get('X-Hub-Signature', ''):
            # Run the deployment script
            subprocess.run(['/path/to/your/deploy.sh'], shell=False)
            return 'Webhook received and deployment triggered successfully!', 200
        else:
            abort(401)  # Unauthorized
    else:
        abort(400)  # Bad request
