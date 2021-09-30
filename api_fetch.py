import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def json_test():
    return jsonify(courses)


courses = [
    {
        'id' : 0,
        'name' : 'CSCI 223',
        'instructor' : 'Ben Johnson',
        'mode' : 'in person',
        'semester' : 'fall',
        'timeslot' : 200
    }
]