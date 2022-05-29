import unittest

from src.guests import Guest 

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("moath", 100,"song123")

    def test_guest_has_name(self):
        self.assertEqual("moath", self.guest.name) 



    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest.cash)         