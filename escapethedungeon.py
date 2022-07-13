from threading import local
import time
import os
from tkinter import Y
from turtle import clear
from unicodedata import name
from tqdm import tqdm
#pip3 install tqdm
import sys
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

class User(Person):
    #health for user is automatically 100
    health = 100
    #position of the user
    user_location_X = 1
    user_location_Y = 1
    def __init__(self, name):
        super().__init__(name)
    def get_health(self):
        return self.health

    def set_health(self,num):
        self.health = num

    def get_initial_location_X(self):
        return self.user_location_X

    def set_initial_location_X(self, x):
        self.user_location_X = x

    def get_initial_location_Y(self):
        return self.initial_location_Y

    def set_initial_location_Y(self, y):
        self.initial_location_Y = y
    
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
    def __init__(self) -> None:
        pass
    def print_map(self):

        for i in map:
            print("----- ----- -----")
            print(" ".join(i))
            print("----- ----- -----")
    def get_map():
        return map
    def set_map(x,y, value):
        map[x][y] = value
#map will be a list of map objects 
def game():
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
    
    os.system('clear')
    time.sleep(1)

    map_class = Map()
    map = map_class.print_map()

    while True:
        print("\nMovement Instructions")
        print("'W' to move foward")
        print("'A' to move left")
        print("'S' to move backwards")
        print("'D' to move right")
        move = input("\nWhere would you like to move?")



def main():
    print_Title()
    start_game = input("\nWould you like to continue? (Y)es or (N)o: ")
    if start_game == 'y':
        print("Starting game")
        bar_loop()
    elif start_game == 'n':
        exit()
    time.sleep(2)
    game()
    
if  __name__ == '__main__':
    main()

