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

    def save(self, filepath):
        with open(filepath, "w+") as f:
            for i in self.getAttrList():
                f.write("%s : %s\n" % (i, str(self.getAttr(i))))

    @staticmethod
    def load(filepath):
        attrs = {}
        with open(filepath, "r") as f:
            for line in f:
                s = [i.strip() for i in line.split(":")]
                attrs[s[0]] = s[1]
        return Dict(**attrs)

    def __str__(self):
        s = ""
        for i in self.getAttrList():
            s += "%s : %s\n" % (i, str(self.getAttr(i)))
        return s
