import pytest
import source.shapes as shapes
import math

class TestCircle:
    #this method runs before every test method
    def setup_method(self, method):
        print(f"setting up {method}")
        #here we can setup some values which remain relevant for the test case

        self.circle = shapes.Circle(10)

    #this method run after every test method
    def teardown_method(self, method):
        print(f"teardown {method}")
        #delete the circle object
        del self.circle

    def test_area(self):
        print("-------testing method 1-------")
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        
    def test_parameter(self):
        print("-------testing method 2--------")
        result = self.circle.parameter()
        expected = 2* math.pi* self.circle.radius
        assert result == expected




