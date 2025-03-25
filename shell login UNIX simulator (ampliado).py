#© (CC) JimmyGraylendor

import time
import sys

auth = False

nombres = ["us22", "alum11", "us11", "prof4"]
passwds = ["1234", "$$99", "11%11", "aaBB"]

while True :
    while auth == False :
        login = input("login: ")
        password = input("password: ")
        if (((login == nombres[0]) and (password == passwds[0])) or ((login == nombres[1]) and (password == passwds[1])) or ((login == nombres[2]) and (password == passwds[2])) or ((login == nombres[3]) and (password == passwds[3]))):
            print("User logged in")
            auth = True
            break
        else:
            print("Login incorrect")
    
    while auth == True :
        command = input(login+" % ")
        if command == "logout" :
            print("User logged out")
            auth = False
            break
        elif command == "time" :
            print(time.asctime())
        elif command == "version" :
            print(sys.version)
        elif command == "exit" :
            exit()
        else:
            print("Invalid command")
