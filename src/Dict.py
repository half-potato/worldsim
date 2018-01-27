import os, utils

# It's like a dictionary class hybrid
class Dict:
    def __init__(self, *args, **kargs):
        for i in kargs:
            self.setAttr(i, kargs[i])

    def setAttr(self, name, value):
        setattr(self, name, value)

    def getAttr(self, name):
        return getattr(self, name)

    def getAttrList(self):
        return [attr for attr in vars(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    @staticmethod
    def fromTemplate(name):
        return

    def save(self, path):
        with open(os.path.join(path, self.name), "w+") as f:
            for i in self.getAttrList():
                f.write("%s : %s\n" % (i, str(self.getAttr(i))))

    @staticmethod
    def load(filepath):
        attrs = {}
        with open(filepath, "r") as f:
            for line in f:
                s = [i.strip() for i in line.split(":")]
                if s[1] == "None":
                    attrs[s[0]] = None
                elif utils.isfloat(s[1]):
                    attrs[s[0]] = float(s[1])
                elif s[1].isdigit():
                    attrs[s[0]] = int(s[1])
                else:
                    attrs[s[0]] = s[1]
        return Dict(**attrs)

    def cast(d):
        if not hasattr(d, "type"):
            return d
        t = utils.casting_dict[d.type]
        return t(d)

    def __str__(self):
        s = ""
        for i in self.getAttrList():
            s += "%s : %s\n" % (i, str(self.getAttr(i)))
        return s
