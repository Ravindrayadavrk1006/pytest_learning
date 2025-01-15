import pytest
import source.shapes as shapes

#pytest fixtures

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, width=20)
@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(length= 5, width= 10)
#pass the fixtures
def test_area(my_rectangle):
    # rectangle = shapes.Rectangle(length= 10, width= 20)
    # assert rectangle.area() == 10*20
    

    #testing with fixtures
    assert my_rectangle.area() == 10*20

def test_rectangle(my_rectangle):
    # rectangle = shapes.Rectangle(length= 10, width= 20)
    # assert rectangle.parameter() == 2*(10 + 20)

    assert my_rectangle.parameter() == 2*(10+20)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle