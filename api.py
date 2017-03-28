"""
API runner
"""
from flask import Flask
from flask_restful import Api
from manager.albums import Albums
from manager.photos import Photos
from manager.init import Init

app = Flask(__name__)
api = Api(app)

api.add_resource(Init, '/manager/init')

api.add_resource(Albums, '/manager/albums',
                         '/manager/albums/<int:album_id>')

api.add_resource(Photos, '/manager/photos',
                         '/manager/photos/<int:photo_id>')

if __name__ == '__main__':
    app.run(debug=True)
