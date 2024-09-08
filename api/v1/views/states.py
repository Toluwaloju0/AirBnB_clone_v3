#!/usr/bin/python3
"""A module to perform http actions on the state class"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
@app_views.route('/states/<state_id>')
def get_state(state_id=None):
    """Api to get a state"""
    if state_id is None:
        cls_dict = storage.all(State)
    else:
        # Get the class using storage.get()
        cls = storage.get(State, state_id)
        if cls:
            return jsonify(cls.to_dict())
        else:
            abort(400)
    state_list = []
    if cls_dict:
        for key in cls_dict.keys():
            state_list.append(cls_dict[key].to_dict())
        return jsonify(state_list)
    else:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """api to delete a state"""
    state = storage.get(State, state_id)
    if state:
        state.delete()
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create():
    """To create a new state instance and save it"""
    if not request.is_json:
        abort(400)
    data = request.get_json()
    if 'name' not in data.keys():
        abort(400)
    # create the new stae instance
    new_state = State(**data)
    new_state.save()

    return jsonify(new_state.to_dict())


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update(state_id):
    """To update a state instance using its id"""
    if not request.is_json:
        abort(400)
    data = request.get_json()
    print(data)

    # get and update the state instance
    state = storage.get(State, state_id)
    if state is None:
        abort(400)
    if data.get('name'):
        state.name = data['name']
    storage.save()
    return jsonify(state.to_dict())
