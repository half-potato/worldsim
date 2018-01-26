import random

def roll(dice:str)->int:
    dice_tokens = dice.split("d")
    out = 0
    for i in range(0, int(dice_tokens[0])):
        out += random.randint(0,int(dice_tokens[1])+1)
