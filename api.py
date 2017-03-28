"""
API runner
"""
from flask import Flask
from flask_restful import Api
from manager.albums import Albums
from manager.photos import Photos, PhotosByAlbum
from manager.init import Init

app = Flask(__name__)
api = Api(app)

# In-memory albums and photos
albums = []
photos = []


# Routing endpoints to Resource classes
api.add_resource(Init,
                 '/manager/init',
                 resource_class_kwargs={'albums': albums,
                                        'photos': photos})

api.add_resource(Albums,
                 '/manager/albums',
                 '/manager/albums/<int:album_id>',
                 resource_class_kwargs={'albums': albums,
                                        'photos': photos})

api.add_resource(Photos,
                 '/manager/photos',
                 '/manager/photos/<int:photo_id>',
                 resource_class_kwargs={'albums': albums,
                                        'photos': photos})

api.add_resource(PhotosByAlbum,
                 '/manager/photos/album/<int:album_id>',
                 resource_class_kwargs={'albums': albums,
                                        'photos': photos})



if __name__ == '__main__':
    app.run(debug=True)
