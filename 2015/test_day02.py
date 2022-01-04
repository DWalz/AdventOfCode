from day02 import get_present_area, get_present_ribbon, get_total


def test_present_area2x3x4():
    assert get_present_area('2x3x4') == 58


def test_present_area1x1x10():
    assert get_present_area('1x1x10') == 43


def test_presents_area():
    assert get_total(get_present_area, '2x3x4\n1x1x10') == 101


def test_present_ribbon2x3x4():
    assert get_present_ribbon('2x3x4') == 34


def test_present_ribbon1x1x10():
    assert get_present_ribbon('1x1x10') == 14


def test_presents_ribbon():
    assert get_total(get_present_ribbon, '2x3x4\n1x1x10') == 48
