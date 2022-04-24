import os
import pickle

class UsersStrorage:

    

    def insert(self, users, new_user):
        if not users:
            users[0] = new_user
        else:
            max_number = max(list(map(lambda i: i, users)))
            users[max_number + 1] = new_user
        return users
            
    def load(self):
        if os.path.exists('./mypickle.pickle'):
            with open('mypickle.pickle', 'rb') as f:
                users = pickle.load(f)
                return users
        else:
            return {}
        
    def save(self, users):
        with open('mypickle.pickle', 'wb') as f:
            pickle.dump(users, f)