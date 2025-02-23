from flask import Flask
from flask import Response
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Create the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the User Authentication API"

# Vercel handler
def handler(event, context):
    # Wrap the Flask app in a WSGI middleware for Vercel compatibility
    wsgi_app = DispatcherMiddleware(app, {
        '/': app
    })

    # Use the WSGI app to handle the event
    response = Response.from_app(wsgi_app, event)
    return {
        'statusCode': response.status_code,
        'headers': dict(response.headers),
        'body': response.get_data().decode('utf-8')
    }

# Run the app locally
if __name__ == '__main__':
    app.run(debug=True)