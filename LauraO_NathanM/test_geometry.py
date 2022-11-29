import Geometry


def test_point():
    point = Geometry.Point(1,2)
    expected = (1,2)
    actual = (point.x,point.y)
    assert expected == actual 

def test_line():
    from_point = Geometry.Point(1,2)
    to_point = Geometry.Point(0,0)
    line = Geometry.Line(from_point,to_point)
    line.to_point = Geometry.Point(1,2)
    line.from_point = Geometry.Point(0,0)
    expected = ((1)**2 + (2)**2)**0.5
    actual = line.length
    assert expected == actual 

def test_polyline():
    from_point = Geometry.Point(4,1)
    to_point = Geometry.Point(9,6)
    line = Geometry.Line(from_point,to_point)
    from_point2 = Geometry.Point(6,7)
    to_point2 = Geometry.Point(10,5)
    line2 = Geometry.Line(from_point2,to_point2)
    polyline = Geometry.Polyline()
    polyline.add_segment(line)
    polyline.add_segment(line2)
    expected = 11.54
    actual = round(polyline.length, 2)
    assert expected == actual 
