from models.user import User
from pprint import pprint
import copy

class Users:

    def get_create_fields(self):
        [self.__names, self.__last_names, 
        self.__age, self.__email] = self.__field_helper().get_create_fields()

    def get_update_fields(self):
        [self.__names, self.__last_names, 
        self.__age, self.__email] = self.__field_helper().get_update_fields()

        
    def all(self):
        pprint(self.__users)

    def create(self):
        self.get_create_fields()
        user = User(self.__names, self.__last_names, self.__age, self.__email)
        self.__storage.insert(self.__users, user)
        self.__storage.save(self.__users)
        print(user)
        
    def update(self):
        id = self.__field_helper().get_id()
        self.get_update_fields()
        new_user = User(self.__names, self.__last_names,
                        self.__age, self.__email)
        self.__users[id] = new_user
        self.__storage.save(self.__users)
        print(new_user)
        
    def delete(self):
        id = self.__field_helper().get_id()
        deleted_user = copy.copy(self.__users[id])
        del self.__users[id]
        self.__storage.save(self.__users)
        print(deleted_user)
            
    def set_field_helper(self, field_helper):
        self.__field_helper = field_helper

    def set_storage(self, storage):
        self.__storage = storage

    def set_users(self, users):
        self.__users = users
            
    def get_field_helper(self):
        return self.__field_helper

    def get_storage(self):
        return self.__storage

    def get_users(self):
        return self.__users

    
    def __init__(self, field_helper, storage):
        self.__field_helper = field_helper
        self.__storage = storage
        self.__users = self.__storage.load()
        self.__names = ""
        self.__last_names = ""
        self.__age = ""
        self.__email = ""
        