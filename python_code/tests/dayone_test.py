import pytest 
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.day1.main import DayOneClass

class TestDayOneClass:
    def test_check_list_correctness(self):
        list_one = [1,5,6,4]
        list_two = [2,3,4,9]
        checker = DayOneClass(list_one=list_one, list_two=list_two)
        assert checker.check_list_correctness() == True

    def test_check_list_correctness_error(self):
        list_one = [1,5,6,4]
        list_two = [2,3,4,9, 10]
        checker = DayOneClass(list_one=list_one, list_two=list_two)
        with pytest.raises(ValueError):
            checker.check_list_correctness()

    def test_check_list_correctness_error_type(self):
        list_one = [1,5,6,4]
        list_two = [2,3,4,"a"]
        checker = DayOneClass(list_one=list_one, list_two=list_two)
        with pytest.raises(ValueError):
            checker.check_list_correctness()
        
    def test_compare_lists(self):
        list_one = [1,5,6,4]
        list_two = [2,3,4,9]
        checker = DayOneClass(list_one=list_one, list_two=list_two)
        assert checker.compare_lists() == 10