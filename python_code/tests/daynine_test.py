import pytest 
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.day9.main import DayNineClass

class TestDayOneClass:
    def test_check_list_correctness(self):
        data = "2333133121414131402"
        checker = DayNineClass()
        assert checker.run_program(data) == 1928

    def test_check_assertion_error(self):
        data = "2A33133121414131402"
        checker = DayNineClass()
        with pytest.raises(ValueError):
            checker.run_program(data)

    def test_check_assertion_error_dot(self):
        data = "2A331.3121414131402"
        checker = DayNineClass()
        with pytest.raises(ValueError):
            checker.run_program(data)