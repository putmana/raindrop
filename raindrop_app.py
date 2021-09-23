from flask import Flask
app = Flask(__name__)

@app.route('/')
def raindrop_app():
    return "Hello world!"