import pytest 
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.day3.main import DayThreeClass

class TestDayThreeClass:
    def test_check_base_functionality(self):
        test_string = "mul(12,5)"
        checker = DayThreeClass()
        outcome = checker.get_multiplication_result(test_string)
        assert outcome == 60

    def test_check_not_multiply_incomplete(self):
        test_string = "mul(12,5"
        checker = DayThreeClass()
        outcome = checker.get_multiplication_result(test_string)
        assert outcome == 0
        
    def test_check_raise_Value_Error_wrong_multiplcation(self):
        test_list = ["12", "ab"]
        checker = DayThreeClass()
        with pytest.raises(ValueError):
            checker.return_product_of_list(test_list)