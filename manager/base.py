"""
Abstraction class for Resource
"""
from flask_restful import Resource


class Base(Resource):
    def __init__(self, albums, photos):
        self.albums = albums
        self.photos = photos

    def get(self, *args):
        raise NotImplemented

    def post(self, *args):
        raise NotImplemented

    def put(self, *args):
        raise NotImplemented

    def delete(self, *args):
        raise NotImplemented