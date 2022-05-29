import unittest 

from src.karaoke import Karaoke 


class TestKaraoke(unittest.TestCase):
    def setUp(self):
        self.karaoke = Karaoke("Karaoke1") 

    def test_karaoke_has_name(self):
        self.assertEqual("Karaoke1", self.karaoke.name)    
 