import pygame

from noname import constants


class SlotContainerFull(Exception):
    pass


class InvalidSlotNumber(Exception):
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

    def free_slots(self):
        return [slot for slot in self.slots.itervalues() if slot.free()]

    def has_space(self):
        return len(self.free_slots()) > 0

    def get_first_free_slot(self):
        return get_first_free_slot(self.slots)

    def add(self, item):
        slot = self.get_first_free_slot()
        slot.add(item)

    def get(self, slot_number):
        slot_range = range(1, self.num_slots + 1)
        if slot_number not in slot_range:
            msg = "Invalid slot number %s for container size %s"
            raise InvalidSlotNumber(msg % slot_number, self.num_slots)
        return self.slots[slot_number]


class Bag(SlotContainer):
    pass


class Inventory(SlotContainer):
    pass


class PlayerInventory(Inventory):
    def __init__(self, owner, num_slots):
        Inventory.__init__(self, owner, num_slots)
        initial_bag = Bag(self, constants.STARTING_BAG_SIZE)
        self.add(initial_bag)


class MonsterInventory(object):
    def __init__(self, owner, items):
        self.owner = owner
        self.items = items

    def get_item(self):
        raise NotImplemented
