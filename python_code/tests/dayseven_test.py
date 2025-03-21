import pytest 
import numpy as np

from python_code.src.day7.main import DaySevenClass


class TestDaySixClass:
    def test_check_connections(self):
        checker = DaySevenClass()
        calibration_input = "190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20 165"
        assert checker.find_sum_of_all_legitimate_operators(calibration_input) == 3749