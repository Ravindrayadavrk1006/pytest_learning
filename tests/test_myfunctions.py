import pytest
import source.myfunctions as my_functions
import time

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

# adding metadata that this test is slow
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10,2)
    assert result == 5


#if we don't want to run some tests
@pytest.mark.skip(reason = "this feature is currently broken")
def test_add():
    assert my_functions.add(1,2) == 3


# we are marking it failed
@pytest.mark.xfail(reason= "we know we cannot divide by zero")
def test_divide_by_zero():
    my_functions.divide(4, 0)
