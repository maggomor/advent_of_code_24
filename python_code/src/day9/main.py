from pydantic import BaseModel
import numpy as np
from typing import Union

class DayNineClass(BaseModel):
    input_str: str = None

    def __post_init__(self, input_str: str = None):
        self.input_str = input_str

    def validate_input_str(self, input_str: str = None):
        return all([type(int(input_str[i]))==int for i in range(len(input_str))])

    def create_full_string(self, input_str: str = None):
        if self.validate_input_str(input_str=input_str):
            block_numbers = [int(input_str[i]) for i in range(len(input_str)) if i % 2 == 0]
            space_numbers = [int(input_str[i]) for i in range(len(input_str)) if i % 2 == 1]
            if len(input_str) % 2 == 1:
                space_numbers.append(0)
            full_space_string = ""
            counter = 0
            for block, space in zip(block_numbers, space_numbers):
                full_space_string += block*str(counter)+space*"."
                counter += 1
        return full_space_string
    
    def sort_full_string(self, input_str: str = None):
        for i in range(len(input_str))[::-1]:
            if ((input_str[i] != ".") & (input_str.find(".") < i)):
                input_str = input_str[:input_str.find(".")] + input_str[i] + input_str[input_str.find(".")+1:i] + "." + input_str[i+1:]
        return input_str
    
    def compute_checksum(self, input_str: str = None):
        checksum = 0
        for idx, num in enumerate(input_str):
            if num != ".":
                checksum += idx * int(num)
        return checksum
    
    def run_program(self, input_str: str = None):
        return self.compute_checksum(self.sort_full_string(self.create_full_string(input_str=input_str)))

    
if __name__ == "__main__":
    data = "2333133121414131402"
    checker = DayNineClass()
    checksum = checker.run_program(data)
    print(f"Checksum of String {data} is {checksum}.")