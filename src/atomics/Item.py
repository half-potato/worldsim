import random, math, game

class Item(Dict):
    def __init__(self, name, rarity, quality=None, dob=game.time(), max_age=None, durability=100, stacksize=1, **kargs):
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
        self.dob = dob
        self.max_age = max_age
        self.durability = durability
        self.stacksize = stacksize
        for i in kargs:
            self.setAttr(i, kargs[i])

    def getQuality(self):
        return self.quality * (self.durability/100.)

    def getAge(self):
        """ yyyyyyyymmddhhmmss """
        return game.time() - self.dob

    def use(self):
        """ probablistically damage the item """
        probDamage = 1 - self.getQuality()/100. + (self.getAge() - self.max_age/2.)/self.max_age # temp
