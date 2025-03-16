from pydantic import BaseModel
import numpy as np

class DayOneClass(BaseModel):
    list_one: list
    list_two: list
    distance: float = None

    def __post_init__(self, list_one: list, list_two: list, distance: float = None):
        self.list_one = list_one
        self.list_two = list_two
        self.distance = distance

    def check_list_correctness(self):
        if len(self.list_one) != len(self.list_two):
            raise ValueError("Lists are of different lengths")
        for x, y in zip(self.list_one, self.list_two):
            if type(x) not in [int, float] or type(y) not in [int, float]:
                raise ValueError("Wrong Type, only nums allowed!")
        return True
            
    def compare_lists(self):
        self.check_list_correctness()
        self.distance = np.sum(np.array(np.abs(np.array(self.list_one) - np.array(self.list_two))))
        return self.distance
    
if __name__ == "__main__":
    list_one = [1,5,6,4]
    list_two = [2,3,4,9]
    checker = DayOneClass(list_one=list_one, list_two=list_two)
    outcome = checker.compare_lists()
    print(f"Distance between lists {list_one} and {list_two} is: {outcome}")