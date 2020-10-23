from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("Bagdad", 14.758, 18.898)
    assert p1.get_lang_long() == (14.758, 18.898)
