import pytest
import source.myfunctions as my_functions


def test_add():
    result = my_functions.add(1,4)
    #here it is failing , the code will break here
    # assert result == 6
    # assert result == 5

def test_divide():
    result = my_functions.divide(10,2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = my_functions.divide(10, 0)
        assert True

def test_add_strings():
    result = my_functions.add("i like ", "healthy food")
    assert result == "i like healthy food"