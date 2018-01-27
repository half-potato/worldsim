import random, string
from Item import Item

casting_dict = {
    "Item": Item,
}

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def roll(dice:str)->int:
    dice_tokens = dice.split("d")
    out = 0
    for i in range(0, int(dice_tokens[0])):
        out += random.randint(0,int(dice_tokens[1])+1)

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename
