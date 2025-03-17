from pydantic import BaseModel
import numpy as np
import re

class DayThreeClass(BaseModel):
    input_lists: list = []

    def __post_init__(self, input_lists: list = None):
        self.input_lists = input_lists

    def return_product_of_list(self, input_list):
        if (len(input_list)==2 and all(np.strings.isnumeric(np.array(input_list)))):
                return float(input_list[0])*float(input_list[1])
        else:
            raise ValueError("Attempting to multiply non-numerical values or too many entries")
            
    def get_all_correct_multiplications(self, input_string):
        matches = [match.start() for match in re.finditer(r"mul\(", input_string)]
        store = []
        for match in matches:
            temp_string = input_string[match:]
            temp_string = temp_string[:temp_string.find(")")+1]
            if (temp_string.count(",") == 1 and len(temp_string.split("mul("))==2 and all(np.strings.isnumeric(np.array(temp_string.split("mul(")[1].split(")")[0].split(","))))):
                store.append(temp_string.split("mul(")[1].split(")")[0].split(","))
        return store 
    
    def get_multiplication_result(self, input_string):
        store = np.sum(np.array([self.return_product_of_list(x) for x in self.get_all_correct_multiplications(input_string = input_string)]))
        self.input_lists.append((input_string, store))
        return store
    
if __name__ == "__main__":
    test_string = "156mul(12,5)+asdwimul[12,4],oismul(14,9*mul(12,5!)asmul(15,4^2)miaumul(14,9**5)iwdmul(14,8)"
    test_string2 = "mul(12,5)"
    checker = DayThreeClass()
    outcome = checker.get_multiplication_result(test_string)
    outcome2 = checker.get_multiplication_result(test_string2)
    test_list = ["12", "ab"]
    print(f"Result for outcome 2 is {outcome2}")
    print(f"Result for all multiplications is {outcome}")