# relation between guest and room 
class Guest_Room():
    def __init__(self, guestID, roomID):
        self.__guestID = guestID
        self.__roomID = roomID
    
    def get_guestID(self):
        return self.__guestID
    def get_roomID(self):
        return self.__roomID
    
    def set_GuestID(self, guestID):
        self.__guestID = guestID
    def set_RoomID(self, roomID):
        self.get_roomID = roomID

