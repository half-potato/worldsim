STAT_NAMES = ["str", "con", "dex", "int", "cha", "wis", "per", "will", "luck"]

statTypes = {
}

# Add a bunch of different variabilities

def addFlatDistribution(name, high, low):
    statTypes[name] = {}
    for i in STAT_NAMES:
        statTypes[name][i] = [low, high]

def addFlatDistribution("var2", 9, 11) # Armies
def addFlatDistribution("var4", 8, 12) # Similar people
def addFlatDistribution("var6", 7, 13) # Humans

def addFlatDistribution("smallAnimal", 3, 6)
statTypes["smallAnimal"]["dex"] = [14, 16]

def addFlatDistribution("animal", 4, 7)
statTypes["animal"]["dex"] = [10, 12]
statTypes["animal"]["int"] = [2, 4]

def addFlatDistribution("largeAnimal", 4, 7)
statTypes["largeAnimal"]["dex"] = [8, 10]
statTypes["largeAnimal"]["con"] = [8, 10]
statTypes["largeAnimal"]["str"] = [8, 10]

bonusTypes = {
    "Bloodlust": {
        "stats": {
            "str": 2,
        },
        "desc": "Loves hurting people",
    },
    "Kind": {
        "stats": {
            "cha": 2,
            "str": -2,
        },
        "desc": "Kind to others, would never hurt a soul",
    },
    "I am very smart": {
        "stats": {
            "int": 1,
            "cha": -2,
        },
        "desc": "Makes sure you know about every mistake you made"
    },
    "Careful": {
        "stats": {
            "per": 1,
            "wis": 1,
        },
        "desc": "Takes the time to check everything is in order",
    },
    "Greedy": {
        "stats": {
            "cha": -1,
            "luck": 1,
        },
        "desc": "The glimmer in their eye when they see your items makes you nervous.",
    },
}
