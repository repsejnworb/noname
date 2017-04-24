from noname.levels.base import BaseLevel


class Level(BaseLevel):
    def __init__(self):
        name = "Tutorial"
        BaseLevel.__init__(self, name)
        self.resources["sprites"] = []
