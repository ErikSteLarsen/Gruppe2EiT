"""
routes.py
"""
import json
from flask import request, jsonify
from app import app


@app.route('/')
def hello():
    """
    GET /

    Respond 200 OK with human-readable instructions
    """
    return "Hello, this is the backend, see app/routes.py for available routes"


@app.route('/measurement', methods=['POST'])
def add_measurement():
    """
    POST /measurement

    TODO
    """
    # echo request back to client
    return jsonify(request.form)


@app.route('/measurements/latest-result')
def get_most_recent_result():
    """
    GET /measurements/latest-result

    Returns the most recent measurement (TEMPORARY DUMMY DATA)
    """
    with open('dummy_data.json', 'r') as dummy_data:
        return json.load(dummy_data)['measurement_result']
