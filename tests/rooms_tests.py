import unittest 

from src.rooms import Room 

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.room = Room("room1" , ["liam", "thomas"], ["song1", "song2" , "song3"],) 
       

    def test_room_has_name(self):
        self.assertEqual("room1", self.room.name)   

    def test_checkin_guest_to_room(self):
        self.room.checkin_guest("adam")    
        self.assertEqual(["liam", "thomas","adam"], self.room.guests) 
 

    def test_checkout_guest_from_room(self):
        self.room.checkout_guest("liam")
        self.assertEqual(["thomas"], self.room.guests)

    def test_room_has_songs(self):
        self.assertEqual(["song1", "song2" , "song3"], self.room.songs) 