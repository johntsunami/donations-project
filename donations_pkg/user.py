

def login(database,username,password):
    empty = ''
    if username in database:
        print(database[username])
        if database[username] == password:
            
            print('Welcome back',username +'!')
            return username
        else:
            print('Incorrect password for',username)
            return empty
    else:
        print('User not found, Please Register')
        return empty



        # empty = ''
        # for key,value in database.items():
        # if username == key:
        #     if value == password:
        #         print('Welcome back',username +'!')
        #         return username
        #     else:
        #         print('Incorrect password for',username)
        #         return empty
        # else:
        #     print('User not found, Please Register')
        #     return empty
            ## HOW DO I HAVE IT SEARCH ALL KEYS/VALUES
            #AND KEEP SAME FUNCTIONALITY

 
def register(database,username):
    empty = ''
    if username in database:
        print("Username already registered")
        return empty
    else:
        print('Username' + username + 'has been registered')






