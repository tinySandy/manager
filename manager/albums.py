"""
CRUD endpoint for Albums
"""
from flask import request, abort
from manager.base import Base

class Albums(Base):
    def get(self):
        """
        GET request for /albums/ endpoint
        :return: json response with all albums available
        """
        _temp_album = self.albums
        for album in _temp_album:
            album['photos'] = [photo for photo in self.photos if photo['albumId']==album['id']]
        return self.albums, 200

    def post(self):
        """
        POST request for /albums/ endpoint
        :return: creates new album with provided data
        """
        if not request.json or 'title' not in request.json:
            abort(400)

        album = {
            'id': self.albums[-1]['id'] + 1,
            'title': request.json['title'],
        }
        self.albums.append(album)

        return album, 201

    def put(self, album_id):
        """
        PUT(update) request for /albums/ endpoint
        :param album_id: id of the album to update
        :return: json response with updated album
        """
        album = [album for album in self.albums if album['id'] == album_id][0]

        if not album:
            abort(404)
        if not request.json or 'title' not in request.json:
            abort(400)

        album['title'] = request.json['title']

        return album

    def delete(self, album_id):
        """
        DELETE request for /albums/ endpoint
        :param album_id: id of the album to delete
        :return: empty string and 204 code
        """
        album = [album for album in self.albums if album['id'] == album_id][0]
        album_is_not_empty = [photo for photo in self.photos if photo.get('albumId', '') == album['id']]

        if not album:
            abort(404)

        if album_is_not_empty:
            return "Deleting non empty albums is not permitted", 403

        else:
            self.albums.remove(album)

        return 'Requested album has been deleted', 204
