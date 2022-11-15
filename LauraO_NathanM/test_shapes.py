import shapes
import pytest 



def test_area_circle(circle):
    expected = 12.566
    circle = shapes.Circle() 
    circle.radius = 2 
    actual = circle.area 

    assert expected == pytest.approx(actual, 0.001)


def test_area_square(square):
    expected = 9
    square = shapes.Square() 
    square.side = 3 
    actual = square.area_square 

    assert expected == pytest.approx(actual, 0.001)