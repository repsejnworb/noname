class Item(object):
    def __init__(self, name, stats=None, itype=None, level=None):
        self.name = name
        self.stats = stats
        self.type = itype
        self.level = level
