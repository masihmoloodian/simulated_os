import datetime
from colorama import Fore
from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017')
db = client['azos']
col = db['root']

print("JesusOS beta")
username = input("Login as:")
get_password = input("Password:")
password= '123'
if get_password == password and username=='masih':
    print('login successfully')
    print(datetime.datetime.now())
else:
    print("Access denied")
    exit()
flag = '/'

while True:

    command = input(f'{Fore.GREEN}{username}@machine:{Fore.BLUE+flag}{Fore.WHITE}$ ')

    if 'mkdir' in command:
        dir_name = command.split()[1]
        dic = {'node': flag+dir_name,
               'parent': flag}
        col.insert_one(dic)

    if 'touch' in command:
        file_name = command.split()[1]
        dic = {'node': flag+file_name,
               'parent': flag}
        col.insert_one(dic)

    if 'cd' in command:
        path = ''
        path += command.split()[1]
        flag += path
        flag += '/'

    if command == 'pwd':
        print(flag)

    if command == 'ls':
        for x in col.find({'parent': flag}):
            x = x['node']
            x = str(x)
            x = x.split('/')
            length = len(x)
            print(x[length - 1])

    if 'cp' in command:
        source = command.split()[1] # name of file
        destination = command.split()[2]
        dic = {'node': destination+source,
               'parent': destination}
        col.insert_one(dic)

    if 'mv' in command:
        source = command.split()[1] # name of file
        destination = command.split()[2]
        dic = {'node': destination+'/'+source,
               'parent': destination}
        col.insert_one(dic)
        query = {'node': flag+source}
        col.delete_one(query)

    if command == 'cd ~':
        flag = '/'

    if 'rm' in command:
        file_name = command.split()[1]
        dic = {'node': flag+file_name}
        col.delete_one(dic)

    if 'rmdir' in command:
        file_name = command.split()[1]
        dic = {'node': flag+file_name}
        col.delete_one(dic)
