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
            for elem in albums:
                if elem not in self.albums:
                    self.albums.append({'id': elem['id'],
                                        'title': elem['title']})

            photos = requests.get('https://jsonplaceholder.typicode.com/photos').json()
            for elem in photos:
                if elem not in self.photos:
                    self.photos.append({'albumId': elem['albumId'],
                                        'id': elem['id'],
                                        'title': elem['title'],
                                        'url': elem['url']})
            return 'Successfully ingested data to albums and photos', 200
        except:
            abort(500)
