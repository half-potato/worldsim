from Types import STAT_NAMES
from typing import Union, List
import random
from utils import roll

class Entity:
    """The base class for all entities

        
    """
    def __init__(self, name, stats:Stats, hp:Union[int, str], speed:Union[int, List[int]], alignment=None, skills:List[Skill]=None, bonuses:List[Bonus]=None):
        self.name = name
        self.stats = stats
        if type(hp) is str:
            self.hp = roll(hp)
        else:
            self.hp = hp
        self.speed = {"land":0, "flying":0}
        if type(speed) is int:
            self.speed["land"] = speed
        else:
            self.speed["land"] = speed[0]
            self.speed["flying"] = speed[1]
        self.alignment = alignment
        self.skills = skills
        self.bonuses = bonuses

    def add_bonus(self, bonus:Bonus):
        self.bonuses.append(bonus)

    def get_bonuses(self, stat):
        bonuses = list(filter(lambda bonus: stat in bonus.stat_bonus.keys(), self.bonuses))
        stat_bonus = 0
        for bonus in bonuses:
            stat_bonus+=bonus.stat_bonus[stat]
        return stat_bonus

    def roll_check(self, check_name, advantage=False, disadvantage=False):
        is_stat = check_name in STAT_NAMES
        is_skill = check_name in [skill.name for skill in self.skills]
        modifier = 0
        stat = None
        if not is_stat and not is_skill:
            return LookupError("%s is not a valid skill or stat")
        elif is_stat:
            modifier+=self.stat.modifier(check_name)
            stat = check_name
        elif is_skill:
            skill = list(filter(lambda skill: skill['name'] == check_name, self.skills))[0]
            modifier+=self.stat.modifier(skill.stat)
            stat = skill.stat
            if skill.trained and self.proficiency:
                modifier+= self.proficiency

        modifier+=get_bonuses(stat)

        if advantage or disadvantage:
            rolls = [roll("1d20")+modifier, roll("1d20")+modifier]
            if advantage:
                return max(rolls)
            else:
                return min(rolls)
        return roll("1d20")+modifier

class NonPlayerCharacter(Entity):
    def __init__(self, name, stats:Stats, hp:Union[int, str], speed:Union[int, List[int]], cr:float, loottable:LootTable, alignment=None, skills:List[Skill]=None, bonuses:List[Bonus]=None):
        super().__init__(name, stats, hp, speed, alignment, skills, bonuses)
        self.cr = cr
        self.loottable = loottable

class Stats:
    """Maintains skills and makes sure everything is in range
    """

    def __init__(self, range_max=30, **kwargs):
        self.max = range_max

        for stat in kwargs:
            self.setAttr(stat, kwargs[stat])

    def setAttr(self, name, value):
        if type(value) is not int:
            return TypeError("%s value must be an int" % name)
        if name not in STAT_NAMES:
            return LookupError("%s is not in stat table" % name)
        if value not in range(0, self.max):
            return ValueError("%s must be between 0 and %s" % (name, value))
        setattr(self, name, value)

    def getAttr(self, name)->int:
        return getattr(self, name)

    def modifier(self, name)->int:
        return (getattr(self, name)-10)/2


class Skill:
    """For skills that need to be checked (i.e Acrobatics, stealth)
    """
    def __init__(self, name, stat:str, trained:bool=False):
        self.name = name

        if stat not in STAT_NAMES:
            raise LookupError("%s not in stat list" % stat)
        self.stat = stat
        self.trained = trained

class Bonus:
    """For flat bonuses from feats and traits and stuff
    """
    def __init__(self, name, desc=None, **kwargs):
        self.name = name
        if not desc:
            self.desc = "Lazy DM"
        else:
            self.desc = desc
        self.stat_bonus = {}
        for stat in kwargs:
            if stat in STAT_NAMES:
                self.stat_bonus[stat] = kwargs[stat]
            else:
                raise LookupError("%s not found in stat table" % stat)

    def getAttr(self, name):
        return getattr(self.stat_bonus, stat)
