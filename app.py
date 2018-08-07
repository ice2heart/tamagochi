#!/usr/bin/env python3

# UI, RANDOM EVENTS

import os

# ugly hack
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

from enum import Enum, auto

class Events(Enum):
    GO_TO_WORK = auto()
    GO_TO_BED = auto()
    GO_TO_KITCHEN = auto()
    GO_TO_GAMES = auto()
    GO_TO_PRODUCTION = auto()
    RENT_DAY = auto()

class States(Enum):
    NONE = auto()
    WORK = auto()
    SLEEP = auto()
    GAME = auto()
    DO_WIDEOS = auto()
    EAT = auto()

HUNGRY_SPEED = 6
FOOD_SIZE = 50
FOOD_PRICE = 3

WORK_STAMINA_REQ = 8
SLEEP_STAMINA = 10

class Avatar:
    
    def __init__(self):
        self.hp = 100
        self.stamina = 100
        self.fill = 100
        self.money = 10
        self.state = States.NONE
        self.subscribers = 0
    

    def event(self, event_type):
        if event_type == Events.GO_TO_BED:
            self.state = States.SLEEP
        elif event_type == Events.GO_TO_WORK:
            self.state = States.WORK
        elif event_type == Events.GO_TO_KITCHEN:
            self.state = States.EAT
        else:
            pass
        print(self.state)
    
    def _hungry(self):
        hungry = self.fill - HUNGRY_SPEED
        if hungry < 0:
            self.hp = self.hp + hungry
            self.fill = 0
        else:
            self.fill -= HUNGRY_SPEED
        if self.fill > 0 and self.hp < 100:
            self.hp += 1 
        if self.hp <= 0:
            print("You are dead!")
            exit()
        
    def _feed(self):
        self.fill += FOOD_SIZE
        self.money -= FOOD_PRICE
        if self.fill > 130:
            self.fill = 50
            print("Bueeeee")
        
    
    def _work(self):
        if self.stamina <= WORK_STAMINA_REQ:
            print("You have no energy... go to bed")
            self._sleep()
        else:
            self.stamina -= WORK_STAMINA_REQ
            self.money += FOOD_PRICE

    def _sleep(self):
        if self.stamina < 100:
            self.stamina += SLEEP_STAMINA  

    def tick(self):
        self._hungry()
        if self.state == States.EAT:
            self._feed()
        elif self.state == States.WORK:
            self._work()
        elif self.state == States.SLEEP:
            self._sleep()
        else:
            self._sleep()
        cls()
        print("hp:{}\t\tfill:{}\t\t stamina:{}\t\t money:{}$\n\n".format(self.hp, self.fill, self.stamina, self.money))
        print("Subscribers: {},\t\t Status:{}\n".format(self.subscribers, self.state))



class Game:
    avatars = []
    def __init__(self):
        self.avatar = Avatar()

    def input(self):
        for state in Events:
            print('{},{}'.format(state.value, state))
        var = input("Select num of event : ")
        try:
            event = Events(int(var))
            self.avatar.event(Events(int(var)))
        except ValueError:
            pass
        
    def tick(self):
        self.avatar.tick()


game = Game()
while True:
    game.input()
    game.tick()