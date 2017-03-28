from flask_restful import Resource
from flask import request, abort

photos = [
    {
        'albumId': 1,
        'id': 1,
        'title': u'Song',
        'url': u'song url'
    },
    {
        'albumId': 2,
        'id': 1,
        'title': u'Song',
        'url': u'song url'
    }
]


class Photos(Resource):
    def __init__(self):
        pass

    def get(self):
        """
        GET request for /photos/ endpoint
        :return: json response with all photos available
        """
        if len(photos) == 0:
            abort(404)

        return photos, 200

    def post(self, album_id):
        """
        POST request for /photos/ endpoint
        :return: creates new photos under specified album
        """
        if not request.json or 'title' not in request.json:
            abort(400)

        photo = {
            'albumId': album_id,
            'id': photos[-1]['id'] + 1,
            'title': request.json['title'],
        }
        photos.append(photo)

        return photo, 201

    def put(self, album_id, photo_id):
        """
        PUT(update) request for /photos/ endpoint
        :param album_id: id of the album where photo is
        :param photo_id: id of photo to update
        :return: json response with updated album
        """
        photo = [photo for photo in photos if photo['id'] == photo_id]

        if len(photo) == 0:
            abort(404)
        if not request.json or 'title' not in request.json:
            abort(400)

        photo[0]['title'] = request.json['title']

        return photo[0]

    def delete(self, album_id, photo_id):
        """
        DELETE request for /photos/ endpoint
        :param album_id: id of the album where photo is
        :param photo_id: id of the photo to delete
        :return: empty string and 204 code
        """
        album = [album for album in photos if album['id'] == album_id]

        if len(album) == 0:
            abort(404)

        photos.remove(album[0])

        return '', 204
