from pydantic import BaseModel
import numpy as np
import pandas as pd 

class DayTwoClass(BaseModel):
    reports: list

    def __post_init__(self, reports: list = None):
        self.reports = reports

    def assert_matrix_style(self):
        report_matrix = np.array(self.reports)
        if not np.issubdtype(report_matrix.dtype, np.number):
            raise TypeError("Wrong Data Types")
        if np.isnan(report_matrix).any():
            raise ValueError("NaNs given")
        return True
    
    def assert_matrix_rows_equal_sign(self, matrix: np.ndarray = None):
        signed_mat = np.sign(matrix)
        vector = np.abs(signed_mat @ np.ones(signed_mat.shape[1])) == signed_mat.shape[1] * np.ones(signed_mat.shape[0])
        return vector
    
    def compare_adjacent_entries(self):
        if self.assert_matrix_style():
            left_side = np.array(self.reports)[:,:-1]
            right_side = np.array(self.reports)[:,1:]
            distance_matrix = left_side - right_side
            vector = self.assert_matrix_rows_equal_sign(distance_matrix)
            abs_distance_matrix = np.abs(distance_matrix)
            leq_mat = abs_distance_matrix <= 3
            geq_mat = abs_distance_matrix >= 1
            comp_mat = leq_mat * geq_mat 
            comp_mat_dist = comp_mat @ np.ones(comp_mat.shape[1]) == comp_mat.shape[1] * np.ones(comp_mat.shape[0])
            false_rows = comp_mat_dist * vector 
            return false_rows
        return False
    
if __name__ == "__main__":
    reports = [[7,6,4,2,1],[1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]
    checker = DayTwoClass(reports = reports)
    false_rows = checker.compare_adjacent_entries()
    print(false_rows)


        
        