"""
Init endpoint for Albums/Photos
"""
from flask import abort
import requests
from manager.base import Base


class Init(Base):
    def get(self):
        """
        Ingesting albums and photos data from jsonplaceholder REST API
        :return:
        """
        try:
            albums = requests.get("https://jsonplaceholder.typicode.com/albums").json()
            for album in albums:
                if not any(one_album['id'] == album['id'] for one_album in self.albums):
                    self.albums.append({'id': album['id'],
                                        'title': album['title']})

            photos = requests.get('https://jsonplaceholder.typicode.com/photos').json()
            for photo in photos:
                if not any(one_photo['id'] == photo['id'] for one_photo in self.photos):
                    self.photos.append({'albumId': photo['albumId'],
                                        'id': photo['id'],
                                        'title': photo['title'],
                                        'url': photo['url']})
            return 'Successfully ingested data to albums and photos', 200
        except:
            abort(500)


class ReloadManager(Base):
    def get(self):
        """
        Reloading albums and photos to initial values
        :return:
        """
        del self.albums[:]
        del self.photos[:]
        return "Reloaded", 200
