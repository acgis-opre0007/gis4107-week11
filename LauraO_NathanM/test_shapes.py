import pytest 
import shapes


def test_area_circle():
    expected = 12.566
    circle = shapes.Circle() 
    circle.radius = 2 
    actual = circle.area 

    assert expected == pytest.approx(actual, 0.001)


def test_area_square():
    expected = 9
    square_1 = shapes.Square() 
    square_1.side = 3 
    actual = square_1.area_sq

    assert expected == actual

def test_area_rectangle():
    expected = 8
    rectangle_1 = shapes.Rectangle()
    rectangle_1.length = 4
    rectangle_1.width = 2
    actual = rectangle_1.area_rec

    assert expected == actual