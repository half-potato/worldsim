import os, shutil, re, utils
from Dict import Dict
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
            items = [i.name for i in self.items]
            diff = list(set(items) ^ (set(ls)))
            todelete = set(ls).intersection(set(diff))
            for i in todelete:
                p = os.path.join(path, i)
                #print(os.path.join(path, i))
                if os.path.isdir(p):
                    shutil.rmtree(p)
                else:
                    os.remove(p)
        else:
            os.mkdir(path)

        for i in self.items:
            i.save(path)

    @staticmethod
    def load(path):
        items = []
        #path = utils.format_filename(path)
        name = os.path.basename(path)
        if os.path.isdir(path):
            for i in os.listdir(path):
                p = os.path.join(path, i)
                if os.path.isdir(os.path.join(path, i)):
                    items.append(Container.load(p))
                else:
                    items.append(Dict.load(p))
            return Container(name, items)
        else:
            return None

    def append(self, child):
        self.items.append(child)

    def remove(self, name, amount=1):
        amt_rm = 0
        for i in self.items:
            if i.name == name:
                self.items.remove(i)
                amt_rm += 1
            if amt_rm == amount:
                break
        return amt_rm

    def __str__(self):
        s = "name: %s {\n" % self.name
        for i in self.items:
            s += "%s\n" % i
        s = s[:-1] + "}\n"
        return s
