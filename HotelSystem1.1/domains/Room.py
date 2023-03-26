class Room():
    def __init__(self, rid, type, price, status):
        self.__rid = rid
        self.__type = type
        self.__price = price
        self.__status = status
    
    def get_rid(self):
        return self.__rid
    def get_type(self):
        return self.__type
    def get_price(self):
        return self.__price
    def get_status(self):
        return self.__status
    
    def set_rid(self, rid):
        self.__rid = rid
    def set_type(self, type):
        self.__type = type
    def set_price(self, price):
        self.__price = price
    def set_status(self, status):
        self.__status = status

    