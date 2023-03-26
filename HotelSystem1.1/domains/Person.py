class Person():
    def __init__(self,gid,name,gend,dob,phone,email,address):
        self.__gid= gid
        self.__name= name
        self.__gend= gend
        self.__dob= dob
        self.__phone= phone
        self.__email= email
        self.__address= address
    
    def get_gid(self):
        return self.__gid
    def get_name(self):
        return self.__name
    def get_gend(self):
        return self.__gend
    def get_dob(self):
        return self.__dob
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email
    def get_address(self):
        return self.__address
    
    
    def set_gid(self,gid):
        self.__gid= gid
    def set_name(self,name):
        self.__name= name
    def set_gend(self,gend):
        self.__gend= gend
    def set_dob(self,dob):
        self.__dob= dob
    def set_phone(self,phone):
        self.__phone= phone
    def set_email(self, email):
        self.__email= email
    def set_address(self, address):
        self.__address= address
        
        
class Staff(Person):
    def __init__(self,gid,name,gend,dob,phone,email,address):
        super().__init__(gid,name,gend,dob,phone,email,address)
        self.__salary= 0
        self.__position= '_'
        self.__IsStaff = True
        
    def get_position(self):
        return self.__position
    
    def get_salary(self):
        return self.__salary
    
    def set_position(self,position):
        self.__position= position
        
    def set_salary(self,salary):
        self.__salary= salary
        
    def IsStaff(self):
        return self.__IsStaff
    

class Guest(Person):
    def __init__(self,gid,name,gend,dob,phone,email,address):
        super().__init__(gid,name,gend,dob,phone,email,address)
        self.__IsStaff = False
    
    def IsStaff(self):
        return self.__IsStaff