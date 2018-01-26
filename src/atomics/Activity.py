class Activity(Dict):
    def __init__(self, name, desc, res_gained, res_consumed, duration=0, optimal_env, **kargs):
        self.name = name
        self.desc = desc
        self.res_gained = res_gained
        self.res_consumed = res_consumed
        self.optimal_env = optimal_env
        self.duration = duration
        for i in kargs:
            self.setAttr(i, kargs[i])

    def finish(self):
        return res_gained, res_consumed
