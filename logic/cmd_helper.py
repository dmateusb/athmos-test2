import re
from models.meta import singleton

class CmdHelper(metaclass=singleton.Singleton):
        
    def get_number_field(self, field):
        flag = False        
        id = None
        while not flag:
            try:
                id = int(input("Please input the {}: ".format(field)))
                flag = True
            except ValueError:
                print("Please input an integer")
        return id
    
    
    def get_text_field(self, field):
        return input("Please input your {}: ".format(field))
    
    def get_id(self):
        return self.get_number_field("id")
    
    
    def get_names(self):
        return self.get_text_field("names")
    
    def get_last_names(self):
        return self.get_text_field("last names")
    
    def get_age(self):
        return self.get_number_field("age")
    
    def get_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        flag = False
        email = ""
        while not flag:
            email = input("Please input your email: ")
            if re.fullmatch(regex, email):
                flag = True
            else:
                print("Please input a valid email")
        return email
    
    def get_create_fields(self):
        names = self.get_names()
        last_names = self.get_last_names()
        age = self.get_age()
        email = self.get_email()
        return [ names, last_names, age, email ]
    
    def get_update_fields(self):
        return self.get_create_fields()
    