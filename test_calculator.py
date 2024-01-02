import calculator

class TestCalculator :
    def test_addition(self):
        assert 4==calculator.add(2,2)
    
    def test_substract(self):
        assert 7==calculator.substract(19,12)