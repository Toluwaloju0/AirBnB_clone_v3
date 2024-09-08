#!/usr/bin/python3
"""A module to make a flask blueprint"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status():
    my_dict = {'status': 'OK'}
    return jsonify(my_dict)

@app_views.route('/stats')
def get_all():
    from models import storage
    from models.user import User
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.review import Review
    from models.place import Place

    cls_dict = {
        'users': User, 'states': State, 'cities': City,
        'amenities': Amenity, 'reviews': Review, 'places': Place}
    cls_count = {}

    for key in cls_dict.keys():
        cls_count[key] = storage.count(cls_dict[key])

    return jsonify(cls_count)
