import unittest 
from src.guests import Guest
from src.rooms import Room 

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.room = Room("room1" , ["liam", "thomas"], ["song1", "song2" , "song3", "song123"], 2, 20) 
        self.room2 = Room("room2" , ["jack", "john"], ["songA", "songB", "songC",], 4, 30)
        self.guest = Guest("moath", 100,"song123")

    def test_room_has_name(self):
        self.assertEqual("room1", self.room.name)   

    def test_checkin_guest_to_room(self):
        
        self.room.checkin_guest(self.guest.name)
        self.room2.checkin_guest(self.guest.name)   
        self.assertEqual(["liam", "thomas",], self.room.guests) 
        self.assertEqual(["jack", "john", "moath"], self.room2.guests)
        self.assertEqual("check the next room", self.room.checkin_guest("moath"))

    def test_checkout_guest_from_room(self):
        self.room.checkout_guest("liam")
        self.assertEqual(["thomas"], self.room.guests)

    def test_room_has_songs(self):
        self.assertEqual(["song1", "song2" , "song3", "song123"], self.room.songs) 

    def test_cheer_loudly(self):
        self.assertEqual("Whoo", self.room.cheer_loudly(self.guest.fav_song))  

  