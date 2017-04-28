import pytest

from noname import inventory


def test_new_slot_container_has_space():
    slot_container = inventory.SlotContainer(None, 16)
    assert slot_container.has_space()


def test_big_slot_container_has_space_after_add():
    slot_container = inventory.SlotContainer(None, 16)
    slot_container.add("Item")
    assert slot_container.has_space()


def test_slot_container_full():
    slot_container = inventory.SlotContainer(None, 1)
    slot_container.add("Item")
    assert slot_container.has_space() is False


def test_get_first_free_slot():
    slot_container = inventory.SlotContainer(None, 16)
    free_slot = slot_container.get_first_free_slot()
    assert free_slot.free()


def test_get_first_free_slot_full():
    slot_container = inventory.SlotContainer(None, 1)
    slot_container.add("Item")
    with pytest.raises(inventory.SlotContainerFull):
        slot_container.get_first_free_slot()
