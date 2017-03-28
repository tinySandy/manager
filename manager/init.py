"""
Init class for Albums/Photos
"""
from flask_restful import Resource
import requests
from flask import request, abort


class Init(Resource):
    def __init__(self):
        pass
    def get(self):
        try:
            albums = requests.get("https://jsonplaceholder.typicode.com/albums").json()
            photos = requests.get('https://jsonplaceholder.typicode.com/photos').json()
            return 'Data has been initialized'
        except:
            return 500
