from scripts.chp2.video2.mapmaker_start import Point
import pytest

def test_make_one_point():
    p1 = Point("Bagdad", 14.758, 18.898)
    assert p1.get_lang_long() == (14.758, 18.898)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exc:
        Point("Senegal", 99.8548, -187.44406)
    assert str(exc.value) == "Invalid latitue,longitude combination"

    with pytest.raises(ValueError) as exc:
        Point(5, 12.1152, -55.0805)
    assert str(exc.value) == "City name provided must be a string"
