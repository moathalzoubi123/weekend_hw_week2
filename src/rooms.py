from src.guests import Guest

class Room:
    def __init__(self, name, guests, songs, capacity, room_fees,):
        self.name = name 
        self.guests = guests  
        self.songs = songs 
        self.capacity = capacity 
        self.room_fees = room_fees 
        

        
        
        self.guest = Guest("moath", 100, "song123") 


    def checkin_guest(self, guest):
        

        if self.capacity > len(self.guests) and self.guest.cash > self.room_fees: 
             self.guests.append(guest)
        return "check the next room"


    def checkout_guest(self, guest):
        for guest in self.guests:
            if guest == guest:
                self.guests.remove(guest)  
    

    def cheer_loudly(self, fav_song):
        if fav_song in self.songs:
            return "Whoo" 