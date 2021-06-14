from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>Deployment on Azure cloud for UJ classes</h1>"
