from pydantic import BaseModel
import numpy as np
from typing import Union

class DayFiveClass(BaseModel):
    tuple_list: Union[list, str]

    def __post_init__(self, tuple_list: Union[list, str]):
        self.tuple_list = tuple_list

    def turn_tuple_string_to_list(self):
        if type(self.tuple_list) == str:
            try:
                self.tuple_list = [tuple(map(int, line.split('|'))) for line in self.tuple_list.strip().split('\n') if "." not in line]
            except Exception as e:
                raise ValueError("Input is not in desired input form! One entry of X|Y per line, please!")
        return None
    
    def validate_tuples_in_list(self):
        return all([((type(x) == tuple) & (len(x) == 2) & (type(x[0])==int) & (type(x[1])==int)) for x in self.tuple_list])
    
    def turn_update_string_to_list(self, update):
        if type(update)==str:
            try:
                update_list = [int(x) for x in update.split(",") if not "." in x]
                return update_list
            except Exception as e:
                raise ValueError("Update String is not in correct form! Enter a string that has the form X,Y,Z where X, Y and Z are integers.")
        return update
    
    def validate_input_list(self, update_list):
        return all([type(x)==int for x in update_list])
            
    def determine_if_right_order(self, update):
        self.turn_tuple_string_to_list()
        update_list = self.turn_update_string_to_list(update)
        if (self.validate_tuples_in_list() & self.validate_input_list(update_list)):
            prev_nodes = np.array([x[0] for x in self.tuple_list])
            foll_nodes = np.array([x[1] for x in self.tuple_list])
            for i, elem in enumerate(update_list):
                if len(set(prev_nodes[np.where(foll_nodes == elem)]) & set(update_list[i:])) != 0:
                    return False, None, "Update cannot be printed according to rules"
            if len(update_list) % 2 == 1:
                return True, update_list[int(len(update_list)/2)], "Update may be printed"
            elif len(update_list) % 2 == 0:
                return True, update_list[int(len(update_list)/2)-1], f"Update may be printed, middle page number\nIs the lower one as number of pages is equal."
        else:
            raise ValueError("Either Tuple or Update-List has wrong format.")

    
if __name__ == "__main__":
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
    checker = DayFiveClass(tuple_list = tuple_list)
    good_string = "75,47,61,53,29"
    bad_string = "97,13,75,29,47"
    for input_string in [good_string, bad_string]:
        val, middle, outcome = checker.determine_if_right_order(input_string)
        if val:
            print(f"{outcome}. Middle element is {middle}.")
        else:
            print(f"{outcome}")