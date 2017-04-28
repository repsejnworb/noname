from noname import hud


def test_create_element():
    element = hud.Element((100, 50), (100, 100))
    assert element is not None


def test_create_element_collection():
    element_collection = hud.ElementCollection((100, 50), (100, 100))
    assert element_collection is not None
