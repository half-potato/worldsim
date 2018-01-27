import os, shutil
from Item import Item

class Container:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def save(self, path):
        path = os.path.join(path, self.name)
        # Need to delete the stuff that doesn't match
        if os.path.isdir(path):
            ls = os.listdir(path)
            diff = list(set(self.items) - set(ls))
            todelete = set(ls).intersection(set(diff))
            for i in todelete:
                print(os.path.join(path, i))
                #shutil.rmtree(os.path.join(path, i))
        else:
            os.mkdir(path)

        for i in self.items:
            i.save(path)

    @staticmethod
    def load(path):
        pass

    def append(self, child):
        self.items.append(child)

    def remove(self, name, amount=1):
        for i in range(amount):
            self.items.remove(name)


c = Container("Finley's Asshole")
c.append(Item("Finley's Cockring", 1))
c.append(Item("Finley's Buttplug", 1))
c.save(".")
