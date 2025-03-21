from pydantic import BaseModel
import numpy as np
from itertools import product

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
    
    def generate_combinations(self, input_str: str = None):
        parts = input_str.split()
        operators = list(product(['+', '*'], repeat=len(parts)-1))
        combinations = []
        for op_set in operators:
            combined = "".join(p + o for p, o in zip(parts, op_set)) + parts[-1]
            combinations.append(combined)
        return combinations

    def generate_tuples(self, inputs: list = None):
        outputs = [tuple([x[0], self.generate_combinations(input_str = x[1].lstrip())]) for x in inputs]
        return outputs
    
    def evaluate_true_values(self, inputs: list = None):
        true_vals_sum = 0
        for tuples in inputs:
            true_result = tuples[0]
            for test_result in tuples[1]:
                sum_val = 0
                for elem in test_result.split("+"):
                    if "*" not in elem:
                        sum_val += int(elem)
                    elif "*" in elem:
                        temp = elem.split("*")
                        val = 1
                        for num in temp:
                            val *= int(num)
                        sum_val += val
                if int(sum_val) == int(true_result):
                    true_vals_sum += sum_val
        return true_vals_sum
    
    def find_sum_of_all_legitimate_operators(self, input_str: str = None):
        self.calibrated_list = self.turn_input_to_list(input_str)
        outputs = self.generate_tuples(inputs = self.calibrated_list)
        final_sum = self.evaluate_true_values(inputs = outputs)
        return final_sum

if __name__ == "__main__":
    calibration_input = "190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20 165"
    checker = DaySevenClass()
    final_sum = checker.find_sum_of_all_legitimate_operators(calibration_input)
    print(f"Final Sum is {final_sum}")
