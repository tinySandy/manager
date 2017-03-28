"""
CRUD operations for Albums
"""
from flask_restful import Resource
from flask import request, abort

albums = [
    {
        'id': 1,
        'title': u'Hello',
    },
    {
        'id': 2,
        'title': u'Good Bye',
    }
]


class Albums(Resource):
    def __init__(self):
        pass

    def get(self):
        """
        GET request for /albums/ endpoint
        :return: json response with all albums available
        """
        if len(albums) == 0:
            abort(404)

        return albums, 200

    def post(self):
        """
        POST request for /albums/ endpoint
        :return: creates new album with provided data
        """
        if not request.json or 'title' not in request.json:
            abort(400)

        album = {
            'id': albums[-1]['id'] + 1,
            'title': request.json['title'],
        }
        albums.append(album)

        return album, 201

    def put(self, album_id):
        """
        PUT(update) request for /albums/ endpoint
        :param album_id: id of the album to update
        :return: json response with updated album
        """
        album = [album for album in albums if album['id'] == album_id]

        if len(album) == 0:
            abort(404)
        if not request.json or 'title' not in request.json:
            abort(400)

        album[0]['title'] = request.json['title']

        return album[0]

    def delete(self, album_id):
        """
        DELETE request for /albums/ endpoint
        :param album_id: id of the album to delete
        :return: empty string and 204 code
        """
        album = [album for album in albums if album['id'] == album_id]

        if len(album) == 0:
            abort(404)

        albums.remove(album[0])

        return '', 204
