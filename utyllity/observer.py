from enums.enentNames import EventName


class Observer:
    def __init__(self):
        self.observer_events = {}

    def register_event(self, event_name, func_to_call):
        if event_name in self.observer_events:
            self.observer_events[event_name].append(func_to_call)
        else:
            self.observer_events[event_name] = [func_to_call]

    def call_event(self, event_name: EventName):
        if not (event_name in self.observer_events):
            self.observer_events[event_name] = []
        for func in self.observer_events[event_name]:
            func()

