from colorsys import yiq_to_rgb
from threading import local
import time
import os
from tkinter import Y
from turtle import clear
from unicodedata import name
from tqdm import tqdm
#pip3 install tqdm
import numpy as np
import copy
import sys


MOBS_KILLED = 0


def print_Title():

    print("   ▄████████    ▄████████  ▄████████    ▄████████    ▄███████▄    ▄████████  ")
    print("  ███    ███   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███  ")
    print("  ███    █▀    ███    █▀  ███    █▀    ███    ███   ███    ███   ███    █▀   ")
    print(" ▄███▄▄▄       ███        ███          ███    ███   ███    ███  ▄███▄▄▄      ")
    print("▀▀███▀▀▀     ▀███████████ ███        ▀███████████ ▀█████████▀  ▀▀███▀▀▀      ")
    print("  ███    █▄           ███ ███    █▄    ███    ███   ███          ███    █▄   ")
    print("  ███    ███    ▄█    ███ ███    ███   ███    ███   ███          ███    ███  ")
    print("  ██████████  ▄████████▀  ████████▀    ███    █▀   ▄████▀        ██████████  ")
    print("                                                                                                                           ")
    print("    ███        ▄█    █▄       ▄████████      ████████▄  ███    █▄  ███▄▄▄▄      ▄██████▄     ▄████████  ▄██████▄  ███▄▄▄▄  ")
    print("▀█████████▄   ███    ███     ███    ███      ███   ▀███ ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ███▀▀▀██▄")
    print("   ▀███▀▀██   ███    ███     ███    █▀       ███    ███ ███    ███ ███   ███   ███    █▀    ███    █▀  ███    ███ ███   ███")
    print("    ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄          ███    ███ ███    ███ ███   ███  ▄███         ▄███▄▄▄     ███    ███ ███   ███")
    print("    ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀          ███    ███ ███    ███ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███ ███   ███")
    print("    ███       ███    ███     ███    █▄       ███    ███ ███    ███ ███   ███   ███    ███   ███    █▄  ███    ███ ███   ███")
    print("    ███       ███    ███     ███    ███      ███   ▄███ ███    ███ ███   ███   ███    ███   ███    ███ ███    ███ ███   ███")
    print("   ▄████▀     ███    █▀      ██████████      ████████▀  ████████▀   ▀█   █▀    ████████▀    ██████████  ▀██████▀   ▀█   █▀ ")

def bar_loop():
    for i in tqdm(range(10)):
        time.sleep(1)
    global loading_value
    loading_value = False
    os.system('clear')


print("\n")
class Person():
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def is_alive(self, health):
        if health <= 0:
            return False
        return True

class User(Person):
    #health for user is automatically 100
    health = 100
    #position of the user
    def __init__(self, name, user_location_X=1,user_location_Y=1):
        self.user_location_X = user_location_X
        self.user_location_Y = user_location_Y
        super().__init__(name)
    def get_health(self):
        return self.health

    def set_health(self,num):
        self.health = num

    def get_user_location_X(self):
        return self.user_location_X

    def set_user_location_X(self, x):
        self.user_location_X = x

    def get_user_location_Y(self):
        return self.user_location_Y

    def set_user_location_Y(self, y):
        self.user_location_Y = y

    
class Enemy(Person):
   # enemies = {
        # "Devil child": 50,
        #"Corrupted Human": 100,
        #"Goliath": 150,
        # "Tree person": 200,
        #"Golem": 250
    #}
    def __init__(self, name, health, attack, attack_damage):
        super().__init__(name)
        self.health = health
        self.attack = attack
        self.attack_damage = attack_damage
    
    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack
    def get_attack_damage(self):
        return self.attack_damage


# make an object so you can have different rooms like bathroom, gym, etc def __init__(room) self.room = room
class Map():
    global map
    map = [["|   |" for  a in range(3)]for b in range(3)]
    def __init__(self, room):
        self.room = room

    def print_map(self):

        for i in map:
            print("----- ----- -----")
            print(" ".join(i))
            print("----- ----- -----")
    def get_map():
        return map
    def set_map(self,x,y, value):
        map[x][y] = value
#map will be a list of map objects 
def game():
    #dictionary for dialogue
    devil_child = Enemy("Devil Child", 50, "Curse", 15)
    corrupted_human = Enemy("Corrupted Human", 100, "Punch", 30)
    goliath = Enemy("Goliath", 150, "Destroy", 150)
    tree_person = Enemy("Tree person", 200, "Root grab", 10)
    golem = Enemy("Golem", 250, "Rock throw", 10)

    enemies = [ devil_child,
                corrupted_human,
                goliath,
                tree_person,
                golem
    ]

    username = input("Enter your name: ")
    user = User(username)
    
    cavern_room = Map("Cavern")
    lower_cavern_room = Map("Lower Cavern")
    below_the_water = Map("Below the Water")
    cavern_side_path_room = Map("Cavern Side Path")
    deep_in_the_cavern_room = Map("Deep in the Cavern")
    cavern_lower_path_room = Map("Cavern Lower Path")


    rooms = [      [None                  , cavern_room     ,  None,],
                   [below_the_water        ,lower_cavern_room, cavern_side_path_room],
                   [deep_in_the_cavern_room,     None        , cavern_lower_path_room]


    ]
    idx_x = 1
    idx_y = 1
    current_room = rooms[idx_x][idx_y]
    current_room.set_map(user.get_user_location_X(),user.get_user_location_Y(),'| X |')
    while True:
        time.sleep(2)
        os.system('clear')
        user_x = user.get_user_location_X()
        user_y = user.get_user_location_Y()
        #aligns text with map
        print('{:^18s}'.format(current_room.room))  
        current_room.print_map()
        print("\nCommands")
        print("'W' to move foward")
        print("'A' to move left")
        print("'S' to move backwards")
        print("'D' to move right")
        move = input("\nWhere would you like to move? ")

        if move.lower() == "w":
            #change maps
            if user_x == 0:
                if not idx_x-1 < 0  and rooms[idx_x-1][idx_y] != None:
                    current_room.set_map(user_x,user_y,'|   |')
                    idx_x -=1
                    current_room = rooms[idx_x][idx_y]
                    user_x = 2
                    user.set_user_location_X(user_x)
                    current_room.set_map(user_x,user_y,'| X |')
                else: print("There's a force field blocking you!")



            else:
                current_room.set_map(user_x,user_y,'|   |')
                user_x-=1
                user.set_user_location_X(user_x)
                current_room.set_map(user_x,user_y,'| X |')

        elif move.lower() == "a":
            if (user_x == 0 or user_x == 1 or user_x == 2) and user_y == 0:
                if rooms[idx_x][idx_y-1] == None:
                    print("A giant rock is standing in your way!")
                else:
                    current_room.set_map(user_x,user_y,'|   |')
                    idx_y -=1
                    current_room = rooms[idx_x][idx_y]
                    user_y = 2
                    user.set_user_location_Y(user_y)
                    current_room.set_map(user_x,user_y,'| X |')
            else:
                current_room.set_map(user_x,user_y,'|   |')
                user_y -= 1
                user.set_user_location_Y(user_y)
                current_room.set_map(user_x,user_y,'| X |')

        elif move.lower() == "s":
            if user_x == 2:

                if rooms[idx_x+1][idx_y] == None:
                    print("I wouldn't go there if I were you...")
                else:
                    current_room.set_map(user_x,user_y,'|   |')
                    idx_x +=1
                    current_room = rooms[idx_x][idx_y]
                    user_x = 0
                    user.set_user_location_X(user_x)
                    current_room.set_map(user_x,user_y,'| X |')
            else:

                current_room.set_map(user_x,user_y,'|   |')
                user_x+=1
                user.set_user_location_X(user_x)
                current_room.set_map(user_x,user_y,'| X |')

        elif move.lower() == "d":
            current_room.set_map(user_x,user_y,'|   |')
            user_y+=1
            user.set_user_location_Y(user_y)
            current_room.set_map(user_x,user_y,'| X |')



def main():
    #print_Title()
    start_game = input("\nWould you like to continue? (Y)es or (N)o: ")
    if start_game == 'y':
        print("Starting game")
        #bar_loop()
    elif start_game == 'n':
        exit()
    time.sleep(2)
    game()
    
if  __name__ == '__main__':
    main()

