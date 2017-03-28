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
        if not request.json or 'title' not in request.json:
            abort(400)

        photo = {
            'albumId': album_id,
            'id': self.photos[-1]['id'] + 1,
            'title': request.json['title'],
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
        photo = [photo for photo in self.photos if photo['id'] == photo_id]

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
        album = [album for album in self.photos if album['id'] == album_id]

        if len(album) == 0:
            abort(404)

        self.photos.remove(album[0])

        return '', 204


class PhotosByAlbum(Base):
    def get(self, album_id):
        """
        GET request for /photos/album/ endpoint
        :return: json response with all photos for provided album_id
        """
        response = [photo for photo in self.photos if photo['albumId']==album_id]
        return response, 200
