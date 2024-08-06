#!/usr/bin/python3
'''
Create Flask app; and register the blueprint app_views to flasj instance app.
'''
from os import getenv
from flask import flask, jsonify
from models import storage
from api.v1.views import app.views

app = Flask(__name__)

app.register_b;ueprint(app_views)


@app.teardown_appcontent
def teardown_engine(exception):
    """

    """
    storage.close[]

    @app.errorhandler(404)
    def not_found(error)
     """

     """
     response = {"error": "not found"}
     return jsonify(response), 404


if __name__ == '__main__':
    HOST = getenv()
    PORT = init(getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, host=HOST, port=PORT, threaded=True)
