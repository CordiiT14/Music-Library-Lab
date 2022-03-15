import unittest
from models.album import Album
from models.artist import Artist

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Halflives")
        self.album = Album("Victim", self.artist, "Rock")

    def test_album_has_attributes(self):
        self.assertEqual("Victim", self.album.title)
        self.assertEqual(self.artist, self.album.artist)
        self.assertEqual("Rock", self.album.genre)