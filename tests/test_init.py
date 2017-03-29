"""
Integration Test Suites for Init endpoint
Requires Debugging server to be up and running (run api.py in order to proceed)
"""
import unittest
from requests import get


class InitTest(unittest.TestCase):
    def setUp(self):
        get('http://localhost:5000/manager/init')

    def test_albums_ingested_correctly(self):
        # verifying correct amount of albums ingested
        albums = get('http://localhost:5000/manager/albums').json()
        self.assertEqual(len(albums), 100)

        # verifying album 1 has proper id and title
        album = get('http://localhost:5000/manager/album/1').json()
        self.assertTrue(album['id'] == 1)
        self.assertTrue(album['title'] == 'quidem molestiae enim')

        # verifying first photo under album ingested correctly
        self.assertTrue(album['photos'][0]['albumId'] == 1)
        self.assertTrue(album['photos'][0]['id'] == 1)
        self.assertTrue(album['photos'][0]['title'] == 'accusamus beatae ad facilis cum similique qui sunt')
        self.assertTrue(album['photos'][0]['url'] == 'http://placehold.it/600/92c952')

        # verifying album 1 has correct amount of photos
        self.assertTrue(len(album['photos']) == 50)

    def test_photos_ingested_correctly(self):
        # verifying correct amount of albums ingested
        photos = get('http://localhost:5000/manager/photos').json()
        self.assertEqual(len(photos), 5000)

        # verifying first photo has correct parameters
        self.assertTrue(photos[0]['albumId'] == 1)
        self.assertTrue(photos[0]['id'] == 1)
        self.assertTrue(photos[0]['title'] == 'accusamus beatae ad facilis cum similique qui sunt')
        self.assertTrue(photos[0]['url'] == 'http://placehold.it/600/92c952')

    def tearDown(self):
        # cleaning data
        get('http://localhost:5000/manager/reload')
