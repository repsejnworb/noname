class SlotContainerFull(Exception):
    pass


class Slot(object):
    def __init__(self, slot_number):
        self.number = slot_number
        self.item = None

    def free(self):
        return self.item is None

    def add(self, item):
        self.item = item

    def contains(self, item):
        if item == self.item:
            return True
        else:
            return False


def create_slots(num_slots):
    slots = {}
    for i in range(1, num_slots + 1):
        slots[i] = Slot(i)
    return slots


def get_first_free_slot(slots):
    for slot_number, slot in slots.iteritems():
        if slot.free():
            return slot
    raise SlotContainerFull()


class SlotContainer(object):
    def __init__(self, owner, num_slots):
        self.owner = owner
        self.num_slots = num_slots
        self.slots = create_slots(num_slots)

    def has_space(self):
        free_slots = [slot for slot in self.slots.itervalues() if slot.free()]
        return len(free_slots) > 0

    def get_first_free_slot(self):
        return get_first_free_slot(self.slots)

    def add(self, item):
        slot = self.get_first_free_slot()
        slot.add(item)


class Bag(SlotContainer):
    pass


class Inventory(SlotContainer):
    pass


class PlayerInventory(Inventory):
    def __init__(self, owner, num_slots):
        Inventory.__init__(self, owner, num_slots)


class MonsterInventory(object):
    def __init__(self, owner, items):
        self.owner = owner
        self.items = items

    def get_item(self):
        raise NotImplemented
