import random
from Types import statTypes, bonusTypes, STAT_NAMES

class Bonus:
    def __init__(self, name, desc=None, stats=None):
        """
        Parameters
        ----------
        name : str
            Name of bonus. If stats is not defined, this is looked up in bonuses in types.py
        desc : str
            Description of bonus for flavor
        stats : Dict : str -> int
            Number to add to each stat
        """
        self.name = name
        self.desc = desc
        if stats:
            self.stats = stats
        else:
            if not name in bonusTypes:
                raise LookupError("Type %s not found in bonusTypes" % name)
            bonus = bonusTypes[name]
            self.stats = bonus["stats"]
            self.desc = bonus["desc"]
        if not self.desc:
            self.desc = "Lazy DM"

class Stat:
    """
    Usage:
    Looking up a stat:
    s = Stat(...)
    s.str
    Check basestat with:
    s.basestat["str"]
    """
    def __init__(self, *args, **kwargs):
        """
        3 ways to init Stats: from args, from type of stats and Modifier, and from ranges
        Args:
        Parameters
        ----------
        str : int
        con : int
        dex : int
        int : int
        cha : int
        wis : int
        per : int
        will : int
        luck : int

        Type, Modifier:
        Parameters
        ----------
        type : str
            name of a type defined in types in types.py
        Modifier : int
            constant added to every stat

        Ranges:
        Parameters
        ----------
        ranges : Dict : str -> int[2 or 3]
            Must contain a value for every stat defined in STAT_NAMES in types.py
            The int array is of the format [lowerBound, Upperbound, step] and is fed directly to random.randrange
        """

        self.bonuses = {}
        self.basestats = {}
        if len(args) == 9:
            # Init stats from args
            for i, v in enumerate(STAT_NAMES):
                self.basestats[v] = args[i]
        elif len(args) == 2:
            # Init basestats from type and Modifier
            if not args[0] in statTypes:
                raise LookupError("Type %s not found in statTypes" % args[0])
            ranges = statTypes[args[0]]
            # Add Modifier
            for k in ranges:
                ranges[k] = [i+args[1] for i in ranges[k]]
            # Init using ranges
            self.__init__(ranges)
        elif len(args) == 1:
            # Init basestats from ranges. Can have extra basestats.
            # Check that all basestats are in range
            ranges = args[0]
            keys = ranges.keys()
            for k in STAT_NAMES:
                if not k in keys:
                    raise LookupError("Attribute %s not found in initialization range for Stat" % k)
            for k, v in ranges.items():
                self.basestats[k] = random.randrange(*v)

    def addBonus(self, bonus):
        self.bonuses[bonus.name] = bonus

    def removeBonus(self, name):
        del self.bonuses[name]

    def __getattr__(self, name):
        """ Overriden to allow each stat to be looked up like a variable """
        if name in ["basestats", "bonuses"]:
            return super(Stat, self).__getattr__(name)
        elif name in self.basestats:
            basestat = self.basestats[name]
            for n, b in self.bonuses.items():
                if name in b.stats:
                    basestat += b.stats[name]
            return basestat
        else:
            return super(Stat, self).__getattr(name)

    def __setattr__(self, name, value):
        """ Overriden to allow each stat to be looked up like a variable """
        if name in ["basestats", "bonuses"]:
            super(Stat, self).__setattr__(name, value)
        elif name in self.basestats:
            self.basestats[name] = value
        else:
            super(Stat, self).__setattr__(name, value)

    def __str__(self):
        """ Pretty print """
        s = ""
        for k in self.basestats:
            s += "%s: %i" % (k, self.basestats[k])
            for n, b in self.bonuses.items():
                if k in b.stats:
                    s += " %+d from %s" % (b.stats[k], n)
            s += "\n"
        return s

s = Stat("even", 1)
s.str = 10
s.addBonus(Bonus("Bloodlust"))
print(s)
print(s.str)
print(s.basestats)
