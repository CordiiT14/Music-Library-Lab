import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Bjork")
    
    def test_has_name(self):
        self.assertEqual("Bjork", self.artist.name)