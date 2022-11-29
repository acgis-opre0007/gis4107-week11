import pytest 
import shapes


def test_area_circle():
    expected = 12.566
    circle = shapes.Circle() 
    circle.radius = 2 
    actual = circle.area 

    assert expected == pytest.approx(actual, 0.001)

    expected = 'Circle area with a radius of 2 is 12.566'
    actual = str(circle)
    assert expected == actual


def test_area_square():
    expected = 9
    square = shapes.Square() 
    square.side = 3 
    actual = square.area_sq

    assert expected == actual

    expected = 'Square area with a side of 3 is 9'
    actual = str(square)
    assert expected == actual

def test_area_rectangle():
    expected = 8
    rectangle = shapes.Rectangle()
    rectangle.length = 4
    rectangle.width = 2
    actual = rectangle.area_rec

    assert expected == actual

    expected = 'Rectangle area with a length of 4 and a width of 2 is 8'
    actual = str(rectangle)
    assert expected == actual