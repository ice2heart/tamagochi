from typing import Dict


class State:
    def __init__(self):
        pass

    def tick(self):
        pass

    def spent_energy(self):
        return -6


class Event:
    def requirements(self) -> Dict:
        return {}

    def move(self) -> str:
        return 'none'

    @property
    def text(self) -> str:
        return 'Nothing'


class IdleState(State):
    type = 'idle'

    @property
    def text(self) -> str:
        return 'Idling'


class SleepState(State):
    type = 'sleep'

    def tick(self) -> Dict:
        return {
            'hp': 10,
            'stamina': 12.5,
            'hunger': 10,
        }

    def spent_energy(self):
        return 0

    @property
    def text(self) -> str:
        return 'Sleeping'


class GoToBedEvent(Event):
    def requirements(self, state, stats, skills) -> bool:
        if state is not SleepState.type:
            return True

    def move(self) -> str:
        return SleepState.type

    @property
    def text(self) -> str:
        return 'Go to bed'


class WakeUpEvent(Event):
    def requirements(self, state, stats, skills) -> bool:
        if state is SleepState.type:
            return True

    def move(self) -> str:
        return IdleState.type

    @property
    def text(self) -> str:
        return 'Wakeup'
