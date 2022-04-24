from models.users import Users
from logic import CmdHelper
from models.users_storage import UsersStrorage


def choice_menu(inp, users):
    
    if inp == 0:
        users.all()
    elif inp == 1:
        users.create()
    elif inp == 2:
        users.update()
    elif inp == 3:
        users.delete()
    else:
        exit()

def start():
    users = Users(CmdHelper, UsersStrorage())
    print('\n0: All\n'
        '1: Create\n'
        '2: Update\n'
        '3: Delete\n')
    inp = int(input(""))
    choice_menu(inp, users)

while True:
    start()
