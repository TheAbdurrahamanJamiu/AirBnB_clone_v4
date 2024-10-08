#!/usr/bin/python3
'''
Create Flask app. app_views
'''
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """
    Return a JSON response for RESTful API health
    """
    response = ('status': "OK")
    return jsonify(response)

@app_views.route('/stats')
def get_status():
    """

    """
    stats = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'reviews': storage.count('Review'),
            'states': storage.count('State'),
            'users': storage.count('User'),
            }

    return jsonify(stats)
