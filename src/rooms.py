class Room:
    def __init__(self, name, guests, songs):
        self.name = name 
        self.guests = guests  
        self.songs = songs 
      


    def checkin_guest(self, guest):
        self.guests.append(guest)

    
    
    def checkout_guest(self, guest):
        for guest in self.guests:
            if guest == guest:
                self.guests.remove(guest)     
    