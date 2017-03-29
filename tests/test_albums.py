"""
Integration Test Suites for Albums endpoint
Requires Debugging server to be up and running (run api.py in order to proceed)
"""
import unittest
import json
from requests import get, post, put, delete


class AlbumsTest(unittest.TestCase):
    def test_all_albums_can_be_fetched(self):
        # adding 5 albums
        for album_id in range(1, 6):
            post('http://localhost:5000/manager/albums',
                 data=json.dumps({'title': "Test{}".format(album_id)}),
                 headers={'content-type': 'application/json'})

        # verifying there are 5 albums available
        albums = get('http://localhost:5000/manager/albums').json()
        self.assertEqual(len(albums), 5)
        self.assertTrue(albums[0]['id'] == 1)
        self.assertTrue(albums[0]['title'] == 'Test1')

    def test_404_is_returned_if_list_of_albums_is_empty_when_fetching_album(self):
        # verifying 404 is returned when the albums list is empty
        response = get('http://localhost:5000/manager/album/1')
        self.assertEqual(response.status_code, 404)

    def test_404_is_returned_if_album_with_provided_id_is_not_there_when_fetching_albums(self):
        # adding album 1 for test
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # verifying 404 is returned when there is no album with requested id
        response = get('http://localhost:5000/manager/album/2')
        self.assertEqual(response.status_code, 404)

    def test_400_is_returned_if_json_data_is_missing_when_creating_an_album(self):
        # verifying 400 returns if data json is missing
        response = post('http://localhost:5000/manager/albums',
                        data='',
                        headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_400_is_returned_if_title_is_missing_in_data_json_when_creating_an_album(self):
        # verifying 400 return is title key is missing from data json
        response = post('http://localhost:5000/manager/albums',
                        data=json.dumps({'test': "Test"}),
                        headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_existing_album_can_be_updated(self):
        # adding test album
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # updating recently added album
        put('http://localhost:5000/manager/albums/1',
            data=json.dumps({'title': "New Test"}),
            headers={'content-type': 'application/json'})

        # verifying title has been updated
        album = get('http://localhost:5000/manager/album/1').json()
        self.assertTrue(album['title'] == 'New Test')

    def test_400_is_returned_if_json_data_is_missing_when_updating_an_album(self):
        # adding new album
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "New Test"}),
             headers={'content-type': 'application/json'})

        # verifying can not update existing album when json data is missing from the request
        response = put('http://localhost:5000/manager/albums/1',
                       data='',
                       headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_400_is_returned_if_title_is_missing_in_data_json_when_updating_an_album(self):
        # adding new album
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        response = put('http://localhost:5000/manager/albums/1',
                       data=json.dumps({'test': "Test"}),
                       headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 400)

    def test_404_is_returned_if_trying_to_update_non_existent_album(self):
        # verifying 404 is returned when updating the non existent album
        response = put('http://localhost:5000/manager/albums/1',
                       data=json.dumps({'title': "Test"}),
                       headers={'content-type': 'application/json'})
        self.assertTrue(response.status_code == 404)

    def test_existing_empty_album_can_be_deleted(self):
        # adding test album without photos
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # verifying it can be deleted
        response = delete('http://localhost:5000/manager/albums/1')
        self.assertTrue(response.status_code == 204)

    def test_non_empty_album_can_not_be_deleted(self):
        # adding test album
        post('http://localhost:5000/manager/albums',
             data=json.dumps({'title': "Test"}),
             headers={'content-type': 'application/json'})

        # adding photo to previously created album
        post('http://localhost:5000/manager/photos/1',
             data=json.dumps({'title': "Test", 'url': 'test url', 'albumId': 1}),
             headers={'content-type': 'application/json'})

        # verifying it can be deleted
        response = delete('http://localhost:5000/manager/albums/1')
        self.assertTrue(response.status_code == 403)

    def test_404_is_returned_if_trying_to_delete_non_existent_album(self):
        # verifying 404 is returned when trying to delete non existent album
        response = delete('http://localhost:5000/manager/albums/1')
        self.assertTrue(response.status_code == 404)

    def tearDown(self):
        # cleaning test data
        get('http://localhost:5000/manager/reload')
