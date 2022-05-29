import unittest 

from src.songs import Song 


class TestSong(unittest.TestCase):
    def setUp(self):

        self.song = Song("song222") 


    def test_song_has_name(self):
        self.assertEqual("song222", self.song.name)     