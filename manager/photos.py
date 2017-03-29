"""
CRUD endpoint for Photos
"""
from flask import request, abort
from manager.base import Base


class Photos(Base):
    def get(self):
        """
        GET request for /photos/ endpoint
        :return: json response with all photos available
        """
        return self.photos, 200

    def post(self, album_id):
        """
        POST request for /photos/ endpoint
        :return: creates new photos under specified album
        """
        if not request.json or 'title' not in request.json or 'albumId' not in request.json:
            abort(400)

        if self.photos:
            _id = self.photos[-1]['id'] + 1
        else:
            _id = 1

        photo = {
            'albumId': album_id,
            'id': _id,
            'title': request.json['title'],
            'url': request.json['url']
        }
        self.photos.append(photo)

        return photo, 201

    def put(self, album_id, photo_id):
        """
        PUT(update) request for /photos/ endpoint
        :param album_id: id of the album where photo is
        :param photo_id: id of photo to update
        :return: json response with updated album
        """
        photo = [photo for photo in self.photos if photo['albumId'] == album_id and photo['id'] == photo_id]

        if not photo:
            abort(404)

        if not request.json \
                or 'title' not in request.json \
                or 'url' not in request.json\
                or 'albumId' not in request.json:
            abort(400)

        photo[0]['title'] = request.json['title']
        photo[0]['url'] = request.json['url']
        photo[0]['albumId'] = request.json['albumId']

        return photo

    def delete(self, album_id, photo_id):
        """
        DELETE request for /photos/ endpoint
        :param album_id: id of the album where photo is
        :param photo_id: id of the photo to delete
        :return: empty string and 204 code
        """
        photo = [photo for photo in self.photos if photo['albumId'] == album_id and photo['id'] == photo_id]

        if not photo:
            abort(404)

        self.photos.remove(photo[0])

        return '', 204
