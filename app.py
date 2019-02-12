#!/usr/bin/env python3

import os
from typing import Dict

from base import (
    IdleState, SleepState, WakeUpEvent, GoToBedEvent
)

# ugly hack


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Avatar:

    def __init__(self):
        self.state = IdleState.type
        self.states = {
            SleepState.type: SleepState(),
            IdleState.type: IdleState(),
        }
        self.subscribers = 0
        self.stats = {
            'hp': 100,
            'stamina': 100,
            'hunger': 0,
            'money': 10,
        }
        self.skills = {
        }

    def tick(self):
        cls()
        print(f"Status: {self.states[self.state].text}\n\n")

    def event(self, new_state):
        if new_state is not 'none':
            self.state = new_state


class Game:
    avatars = []

    def __init__(self):
        self.avatar = Avatar()
        self.events = [GoToBedEvent(), WakeUpEvent()]

    def input(self):
        for num, event in enumerate(self.events):
            if event.requirements(self.avatar.state, self.avatar.stats, self.avatar.skills):
                print(f'{num} : {event.text}')
        var = input("Select num of event : ")
        try:
            num = int(var)
            self.avatar.event(self.events[num].move())
        except ValueError:
            pass

    def tick(self):
        self.avatar.tick()


game = Game()
while True:
    game.input()
    game.tick()
