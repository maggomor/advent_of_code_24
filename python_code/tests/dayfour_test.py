import pytest 
import numpy as np

from python_code.src.day4.main import DayFourClass


class TestDayFourClass:
    def test_check_connections(self):
        checker = DayFourClass()
        matrix = [list("MMMSXXMASM"),list("MSAMXMSMSA"),list("AMXSXMAAMM"),list("MSAMASMSMX"),list("XMASAMXAMM"),list("XXAMMXXAMA"),list("SMSMSASXSS"),list("SAXAMASAAA"),list("MAMMMXMMMM"),list("MXMXAXMASX")]
        test_string = "XMAS"
        length, connections = checker.get_connections(matrix, test_string)
        assert length == 18
        assert type(connections) == np.ndarray
        assert connections.shape == np.array(matrix).shape

    def test_check_raise_Value_Error_Wrong_Dimensions(self):
        matrix = [list("MMMSXXMA"),list("MSAMXMSMSA"),list("AMXSXMAAMM"),list("MSAMASMSMX"),list("XMASAMXAMM"),list("XXAMMXXAMA"),list("SMSMSASXSS"),list("SAXAMASAAA"),list("MAMMMXMMMM"),list("MXMXAXMASX")]
        test_string = "XMAS"
        checker = checker = DayFourClass()
        with pytest.raises(ValueError):
            checker.get_connections(matrix, test_string)
        
    def test_check_raise_Type_Error_Wrong_Input(self):
        matrix = "this-should-raise-a-value-error"
        test_string = "XMAS"
        checker = checker = DayFourClass()
        with pytest.raises(TypeError):
            checker.get_connections(matrix, test_string)

    def test_check_raise_Type_Error_Non_Alpha_Entries(self):
        matrix = [list("MMMS") + [5] + list("XMASM"),list("MSAMXMSMSA"),list("AMXSXMAAMM"),list("MSAMASMSMX"),list("XMASAMXAMM"),list("XXAMMXXAMA"),list("SMSMSASXSS"),list("SAXAMASAAA"),list("MAMMMXMMMM"),list("MXMXAXMASX")]
        test_string = "XMAS"
        checker = checker = DayFourClass()
        with pytest.raises(TypeError):
            checker.get_connections(matrix, test_string)