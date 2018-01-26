import os

class Container:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def save(self, path):
        # Need to delete the stuff that doesn't match

    @staticmethod
    def load(path):

    def append(self, child):
        self.items.append(child)

    def remove(self, name, amount=1):
        for i in range(amount):
            self.items.remove(name)

