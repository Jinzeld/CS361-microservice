from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the User Authentication API"

def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run(debug=True)