"""
Integration Test Suites for Photos endpoint
Requires Debugging server to be up and running (run api.py in order to proceed)
"""
import unittest
import json
from requests import get, post, put, delete


class PhotosTest(unittest.TestCase):
    def test_all_photos_can_be_fetched(self):
        # adding 5 albums and photos to each one of them
        for _id in range(1, 6):
            post('http://localhost:5000/manager/albums',
                 data=json.dumps({'title': "Test{}".format(_id)}),
                 headers={'content-type': 'application/json'})

            post('http://localhost:5000/manager/photos/{}'.format(_id),
                 data=json.dumps({'albumId': _id, 'title': 'Test{}'.format(_id), 'url': 'test url{}'.format(_id)}),
                 headers={'content-type': 'application/json'})

        # verifying there are 5 photos available
        photos = get('http://localhost:5000/manager/photos').json()
        self.assertEqual(len(photos), 5)
        self.assertTrue(photos[0]['albumId'] == 1)
        self.assertTrue(photos[0]['id'] == 1)
        self.assertTrue(photos[0]['title'] == 'Test1')
        self.assertTrue(photos[0]['url'] == 'test url1')

    #
    def test_400_is_returned_if_json_data_is_missing_when_adding_photo(self):
        # verifying 400 returns if data json is missing
        response = post('http://localhost:5000/manager/albums',
                        data='',
                        headers={'content-type': 'application/json'})
        post('http://localhost:5000/manager/photos/1',
             data='',
             headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_400_is_returned_if_title_is_missing_in_data_json_when_adding_photo(self):
        # verifying 400 return is title key is missing from data json
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})
        response = post('http://localhost:5000/manager/photos/1',
                        data=json.dumps({'albumId': 1, 'url': 'test url'}),
                        headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_400_is_returned_if_album_id_is_missing_in_data_json_when_adding_photo(self):
        # verifying 400 return is albumId key is missing from data json
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})
        response = post('http://localhost:5000/manager/photos/1',
                        data=json.dumps({'title': 'Test', 'url': 'test url'}),
                        headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_existing_photo_can_be_updated(self):
        # adding album
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # adding photo to the album
        post('http://localhost:5000/manager/photos/1',
             data=json.dumps({'albumId': 1, 'title': 'Test', 'url': 'test url'}),
             headers={'content-type': 'application/json'})

        # updating recently added photo
        put('http://localhost:5000/manager/photos/1/1',
            data=json.dumps({'title': "New Test", "url": "New url", "albumId": 1}),
            headers={'content-type': 'application/json'})

        # verifying title and url have been updated
        response = get('http://localhost:5000/manager/album/1').json()
        self.assertTrue(response['photos'][0]['title'] == 'New Test')
        self.assertTrue(response['photos'][0]['url'] == 'New url')

    def test_400_is_returned_if_json_data_is_missing_when_updating_a_photo(self):
        # adding album
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # adding photo to the album
        post('http://localhost:5000/manager/photos/1',
             data=json.dumps({'albumId': 1, 'title': 'Test', 'url': 'test url'}),
             headers={'content-type': 'application/json'})

        # updating recently added photo
        response = put('http://localhost:5000/manager/photos/1/1',
                       data='',
                       headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_400_is_returned_if_title_is_missing_in_data_json_when_updating_a_photo(self):
        # adding album
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # adding photo to the album
        post('http://localhost:5000/manager/photos/1',
             data=json.dumps({'albumId': 1, 'title': 'Test', 'url': 'test url'}),
             headers={'content-type': 'application/json'})

        # updating recently added photo
        response = put('http://localhost:5000/manager/photos/1/1',
                       data=json.dumps({"url": "New url"}),
                       headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_400_is_returned_if_url_is_missing_in_data_json_when_updating_a_photo(self):
        # adding album
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # adding photo to the album
        post('http://localhost:5000/manager/photos/1',
             data=json.dumps({'albumId': 1, 'title': 'Test', 'url': 'test url'}),
             headers={'content-type': 'application/json'})

        # updating recently added photo
        response = put('http://localhost:5000/manager/photos/1/1',
                       data=json.dumps({"title": "New title"}),
                       headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_400_is_returned_if_album_id_is_missing_in_data_json_when_updating_a_photo(self):
        # adding album
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # adding photo to the album
        post('http://localhost:5000/manager/photos/1',
             data=json.dumps({'albumId': 1, 'title': 'Test', 'url': 'test url'}),
             headers={'content-type': 'application/json'})

        # updating recently added photo
        response = put('http://localhost:5000/manager/photos/1/1',
                       data=json.dumps({"url": "New url", "title": "New title"}),
                       headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_404_is_returned_if_trying_to_update_non_existent_a_photo(self):
        # adding album
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # updating non existent photo
        response = put('http://localhost:5000/manager/photos/1/1',
                       data=json.dumps({"url": "New url"}),
                       headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 404)

    def test_existing_photo_can_be_deleted(self):
        # adding test album without photos
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # adding test photo
        post('http://localhost:5000/manager/photos/1',
             data=json.dumps({'albumId': 1, 'title': 'Test', 'url': 'test url'}),
             headers={'content-type': 'application/json'})

        # verifying it can be deleted
        delete('http://localhost:5000/manager/photos/1/1')
        response = get('http://localhost:5000/manager/album/1').json()
        self.assertTrue(not response['photos'])

    def test_404_is_returned_if_trying_to_delete_non_existent_photo(self):
        # verifying 404 is returned when trying to delete non existent album
        response = delete('http://localhost:5000/manager/albums/1')
        self.assertTrue(response.status_code == 404)

    def tearDown(self):
        # cleaning test data
        get('http://localhost:5000/manager/reload')
