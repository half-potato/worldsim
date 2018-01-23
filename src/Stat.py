import random
from statTypes import types, STAT_NAMES

class Stat:
    """
    Usage:
    Looking up a stat:
    s = Stat(...)
    s.str or s.stats["str"]
    """
    def __init__(self, *args, **kwargs):
        """
        3 ways to init Stats: from args, from type of stats and bonus, and from ranges
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

        Type, Bonus:
        Parameters
        ----------
        type : str
            name of a type defined in types in statTypes.py
        bonus : int
            constant added to every stat

        Ranges:
        Parameters
        ----------
        ranges : Dict : str -> int[2 or 3]
            Must contain a value for every stat defined in STAT_NAMES in statTypes.py
            The int array is of the format [lowerBound, Upperbound, step] and is fed directly to random.randrange
        """

        self.stats = {}
        if len(args) == 9:
            # Init stats from args
            for i, v in enumerate(STAT_NAMES):
                self.stats[v] = args[i]
        elif len(args) == 2:
            # Init stats from type and bonus
            if not args[0] in types:
                raise LookupError("Type %s not found in types" % args[0])
            ranges = types[args[0]]
            # Add bonus
            for k in ranges:
                ranges[k] = [i+args[1] for i in ranges[k]]
            # Init using ranges
            self.__init__(ranges)
        elif len(args) == 1:
            # Init stats from ranges. Can have extra stats.
            # Check that all stats are in range
            ranges = args[0]
            keys = ranges.keys()
            for k in STAT_NAMES:
                if not k in keys:
                    raise LookupError("Attribute %s not found in initialization range for Stat" % k)
            for k, v in ranges.items():
                self.stats[k] = random.randrange(*v)

    def __getattr__(self, name):
        if name == "stats":
            return super(Stat, self).__getattr__(name)
        elif name in self.stats:
            return self.stats[name]
        else:
            return super(Stat, self).__getattr(name)

    def __setattr__(self, name, value):
        if name == "stats":
            super(Stat, self).__setattr__(name, value)
        elif name in self.stats:
            self.stats[name] = value
        else:
            super(Stat, self).__setattr__(name, value)

    def __str__(self):
        s = ""
        for k in self.stats:
            s += "%s: %i\n" % (k, self.stats[k])
        return s

s = Stat("even", 1)
s.str = 10
print(s)
print(s.str)
print(s.stats)
