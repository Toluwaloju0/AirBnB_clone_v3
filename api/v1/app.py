#!/usr/bin/python3
"""A script to create an instance of flas and other paths"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception=None):
    storage.close()

@app.errorhandler(404)
def error_404(error):
    return jsonify({'error': "Not found"})

if __name__ == '__main__':
    from os import getenv

    host = '0.0.0.0'
    port = '5000'

    if getenv('HBNB_API_HOST'):
        host = getenv('HBNB_API_HOST')
    if getenv('HBNB_API_PORT'):
        port = getenv('HBNB_API_PORT')

    app.run(host=host, port=port, threaded=True)
