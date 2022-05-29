import unittest

from src.guests import Guest 

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("moath")

    def test_guest_has_name(self):
        self.assertEqual("moath", self.guest.name) 

        