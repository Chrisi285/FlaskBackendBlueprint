import os
import threading
import waitress
import logging
from flask import Flask, redirect
from flask_cors import CORS
from routes.setup_routes import setup

app = Flask(__name__)
app.register_blueprint(setup)

CORS(app)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # write_info_log({"message": "API started, Version 0.3.0"})
    waitress.serve(app, port=5000)
