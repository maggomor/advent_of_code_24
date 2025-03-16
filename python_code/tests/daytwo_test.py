import pytest 
import numpy as np

from python_code.src.day2.main import DayTwoClass

class TestDayTwoClass:
    def test_check_compare_adjacent_entries(self):
        reports = [[7,6,4,2,1],[1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]
        checker = DayTwoClass(reports = reports)
        assert all(checker.compare_adjacent_entries() == [True, False, False, False, False, True])

    def test_check_assert_matrix_style_Type(self):
        reports = [[7,"a",4,2,1],[1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]
        checker = DayTwoClass(reports = reports)
        with pytest.raises(TypeError):
            checker.assert_matrix_style()
        
    def test_check_assert_matrix_style_Value(self):
        reports = [[7,6,np.nan,2,1],[1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]
        checker = DayTwoClass(reports = reports)
        with pytest.raises(ValueError):
            checker.assert_matrix_style()