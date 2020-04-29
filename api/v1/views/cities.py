#!/usr/bin/python3
"""
Index route for AirBnB clone v3 API v1
"""


from models import storage
from models.state import State
from models.city import City
from api.v1.views import app_views
from flask import jsonify, Response, abort, request
import json


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def cities(state_id):
    """
    This route return a list of cities given by the status id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = storage.all(City)
    cities_list = []
    for key, city in cities.items():
        if city.state_id == state_id:
            cities_list.append(city.to_dict())
    js = json.dumps(cities_list)
    print(type(js), js)
    resp = Response(json.loads(json.dumps(cities_list,
                                          indent=2,
                                          sort_keys=True)),
                    200,
                    mimetype='application/json')
    return resp


@app_views.route('/cities/<city_id>', methods=['GET'])
def single_city(city_id):
    """
    Return the Json of a City by its id
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city = city.to_dict()
    resp = Response(json.loads(json.dumps(city,
                                          indent=2,
                                          sort_keys=True)),
                    200,
                    mimetype='application/json')
    return resp
