import pytest
import source.shapes as shapes


#parameterized testing, in it we can pass numbr of inputs and the test cases will run for all the test cases
@pytest.mark.parametrize("side_length, expected_area" , [(5,25), (4,16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area ):
    assert shapes.Square(side= side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_area" , [(5,20), (4,16), (9, 36)])
def test_multiple_square_areas(side_length, expected_area ):
    assert shapes.Square(side= side_length).parameter() == expected_area

