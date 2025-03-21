from pydantic import BaseModel
import numpy as np

class DaySevenClass(BaseModel):
    calibration_input: str = None
    calibrated_list: list = None

    def __post_init__(self, calibration_input: str = None, calibrated_list: list = None):
        self.calibration_input = calibration_input
        self.calibrated_list = calibrated_list

    def turn_input_to_list(self, calibration_input: str = None):
        self.calibration_input = calibration_input
        self.calibrated_list = [tuple(x.split(":")) for x in self.calibration_input.split("\n")]
        return self.calibrated_list
    
    def preprocess_inputs(self):
        if self.calibrated_list is None:
            raise ValueError("No input to perform on.")
        else:
            outcomes = [x[0] for x in self.calibrated_list]
            data = [[int(y) for y in x[1]] for x in self.calibrated_list]
            return outcomes, data

    def get_all_permutations_of_operators(self, data):
        pass


    
if __name__ == "__main__":
    checker = DaySevenClass()
