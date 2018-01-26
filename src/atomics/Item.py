import random, math, game

class Item(Dict):
    def __init__(self, name, rarity, quality=None, dob=game.time(), max_age=None, durability=1, stacksize=1, **kargs):
        """
        Parameters:
        -----------
        name : str
            Name of the item
        rarity : float
            Chance of finding this item in it's respective loot table. Affects quality
        quality : float
            Multiplier for task it's used with
        dob : int
            dob is the date of birth of the item 
        """
        self.name = name
        self.rarity = rarity
        if not quality:
            self.quality = math.log(rarity) + random.gauss(.5, math.log(rarity))
        else:
            self.quality = quality
        self.age = age
        self.max_age = max_age
        self.durability = durability
        self.stacksize = stacksize
        for i in kargs:
            self.setAttr(i, kargs[i])
