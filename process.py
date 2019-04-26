#!/usr/bin/python3
class Process(object):
    def __init__(self):
        self.name = ""
        self.size = 0
        self.arrivalTimes = []
        self.endTimes = []
        self.completed = 0
        self.done = False
        self.running = False