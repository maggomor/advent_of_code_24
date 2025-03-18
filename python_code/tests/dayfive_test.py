import pytest 
import numpy as np

from python_code.src.day5.main import DayFiveClass

data = """
            47|53
            97|13
            97|61
            97|47
            75|29
            61|13
            75|53
            29|13
            97|29
            53|29
            61|53
            97|53
            61|29
            47|13
            75|47
            97|75
            47|61
            75|61
            47|29
            75|13
            53|13
            """
tuple_list = [tuple(map(int, line.split('|'))) for line in data.strip().split('\n')]

class TestDayFiveClass:
    def test_check_right_order_string_tuples(self):
        checker = DayFiveClass(tuple_list=data)
        updates = [[75,47,61,53,29],
                   [97,61,53,29,13],
                   [75,29,13],
                   [75,97,47,61,53],
                   [61,13,29],
                   [97,13,75,29,47]]
        for i, update in enumerate(updates):
            if i in [0,1,2]:
                val, middle, _ = checker.determine_if_right_order(update)
                assert val
                assert middle == update[int(len(update)/2)]
            elif i in [3,4,5]:
                val, middle, _ = checker.determine_if_right_order(update)
                assert middle is None

    def test_check_right_order_list_tuples(self):
        checker = DayFiveClass(tuple_list=tuple_list)
        updates = [[75,47,61,53,29],
                   [97,61,53,29,13],
                   [75,29,13],
                   [75,97,47,61,53],
                   [61,13,29],
                   [97,13,75,29,47]]
        for i, update in enumerate(updates):
            if i in [0,1,2]:
                val, middle, _ = checker.determine_if_right_order(update)
                assert val
                assert middle == update[int(len(update)/2)]
            elif i in [3,4,5]:
                val, middle, _ = checker.determine_if_right_order(update)
                assert middle is None

    def test_check_wrong_input_tuple_string(self):
        tuple_list = [tuple([35,17]), tuple([19,"a"])]
        update = [35,17]
        checker = DayFiveClass(tuple_list=tuple_list)
        with pytest.raises(ValueError):
            checker.determine_if_right_order(update)

    def test_check_wrong_input_tuple_float(self):
        tuple_list = [tuple([35,17]), tuple([19,27.5])]
        update = [35,17]
        checker = DayFiveClass(tuple_list=tuple_list)
        with pytest.raises(ValueError):
            checker.determine_if_right_order(update)

    def test_check_wrong_input_update_string(self):
        update = [35,"a"]
        checker = DayFiveClass(tuple_list=tuple_list)
        with pytest.raises(ValueError):
            checker.determine_if_right_order(update)

    def test_check_wrong_input_update_float(self):
        tuple_list = [tuple([35,17]), tuple([19,27.5])]
        update = [35,17.9]
        checker = DayFiveClass(tuple_list=tuple_list)
        with pytest.raises(ValueError):
            checker.determine_if_right_order(update)