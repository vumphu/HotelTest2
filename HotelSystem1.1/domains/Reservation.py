from domains.Room import *
from domains.Person import *

class Reservation(Room, Person):
    def __init__(self, no, rid, gid, checkin, checkout, paymentdate, creditcard, billing):
        self.__no = no
        self.__rid = rid
        self.__gid = gid
        self.__checkin = checkin
        self.__checkout = checkout
        self.__paymentdate = paymentdate
        self.__creditcard = creditcard
        self.__billing = billing
    
    def get_no(self):
        return self.__no
    def get_rid(self):
        return self.__rid
    def get_gid(self):
        return self.__gid
    def get_checkin(self):
        return self.__checkin
    def get_checkout(self):
        return self.__checkout
    def get_paymentdate(self):
        return self.__paymentdate
    def get_creditcard(self):
        return self.__creditcard
    def get_billing(self):
        return self.__billing
    
    def set_no(self,no):
        self.__no= no
    def set_rid(self,rid):
        self.__rid= rid
    def set_gid(self,gid):
        self.__gid= gid
    def set_checkin(self,checkin):
        self.__checkin= checkin
    def set_checkout(self,checkout):
        self.__checkout= checkout
    def set_paymentdate(self, paymentdate):
        self.__paymentdate= paymentdate
    def set_creditcard(self, creditcard):
        self.__creditcard= creditcard
    def set_billing(self,billing):
        self.__billing= billing
        
        