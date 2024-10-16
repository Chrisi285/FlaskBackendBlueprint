import json
import os

from flask import Blueprint, request
from api import response_generator as r

setup = Blueprint('setup', __name__, url_prefix='/api/v1/setup')


@setup.route('/test', methods=["GET"])
def return_com_ports():
    return r.respond()
