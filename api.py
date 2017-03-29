"""
API runner
"""
from flask import Flask
from flask_restful import Api
from manager.albums import Albums, AlbumsById
from manager.photos import Photos
from manager.init import Init, ReloadManager


class RunnerConfig(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        # In-memory albums and photos
        self.albums = []
        self.photos = []

        # Routing endpoints to Resource classes
        self.api.add_resource(Init,
                              '/manager/init',
                              resource_class_kwargs={'albums': self.albums,
                                                     'photos': self.photos})

        self.api.add_resource(Albums,
                              '/manager/albums',
                              '/manager/albums/<int:album_id>',
                              resource_class_kwargs={'albums': self.albums,
                                                     'photos': self.photos})

        self.api.add_resource(AlbumsById,
                              '/manager/album/<int:album_id>',
                              resource_class_kwargs={'albums': self.albums,
                                                     'photos': self.photos})

        self.api.add_resource(Photos,
                              '/manager/photos',
                              '/manager/photos/<int:album_id>',
                              '/manager/photos/<int:album_id>/<int:photo_id>',
                              resource_class_kwargs={'albums': self.albums,
                                                     'photos': self.photos})

        self.api.add_resource(ReloadManager,
                              '/manager/reload',
                              resource_class_kwargs={'albums': self.albums,
                                                     'photos': self.photos})


if __name__ == '__main__':
    runner = RunnerConfig()
    runner.app.run(debug=True)
