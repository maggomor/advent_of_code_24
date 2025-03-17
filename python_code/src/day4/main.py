from pydantic import BaseModel
import numpy as np

class DayFourClass(BaseModel):

    def __post_init__(self):
        pass

    def validate_matrix_type(self, matrix):
        if not np.strings.isalpha(matrix).all():
            raise TypeError("Entered Matrix that is not only strings")

    def get_locations(self, matrix, letter):
        x_matrix = matrix == letter
        coordinates = np.argwhere(x_matrix)
        return [tuple(coord) for coord in coordinates]
            
    def get_connections(self, matrix, input_string):
        if type(matrix) == list:
            try:
                matrix = np.array(matrix)
            except ValueError as e:
                raise ValueError(f"Value Error: Matrix must have equal dimensions along all sides:\n{e}")
        if type(matrix) not in [list, np.ndarray]:
            raise TypeError("Wrong Input Type: Expects List or Numppy-Array in Matrix-shape")
        self.validate_matrix_type(matrix)
        first_tuples = self.get_locations(matrix, input_string[0])
        second_tuples = self.get_locations(matrix, input_string[1])

        tuples_storage = []
        direction_storage = []
        for first_tuple in first_tuples:
            for second_tuple in second_tuples:
                if (second_tuple[1] - first_tuple[1] in [-1,0,1] and second_tuple[0] - first_tuple[0] in [-1,0,1]):
                    tuples_storage.append([first_tuple, second_tuple])
                    direction_storage.append(tuple([second_tuple[0] - first_tuple[0], second_tuple[1] - first_tuple[1]]))

        string_rest = input_string[2:]
        multiplier = 2
        while len(string_rest) > 0:
            replace_indices = []
            for location, direction in zip(tuples_storage, direction_storage):
                replace_index = tuples_storage.index(location)
                try:
                    if (matrix[location[0][0]+multiplier*direction[0], location[0][1]+ multiplier*direction[1]] == string_rest[0] and location[0][0]+multiplier*direction[0]>=0 and location[0][1]+ multiplier*direction[1]>=0):
                        location.append(tuple([location[0][0]+multiplier*direction[0], location[0][1]+ multiplier*direction[1]]))
                        tuples_storage[replace_index] = location
                    else:
                        replace_indices.append(replace_index)
                except IndexError as e:
                    replace_indices.append(replace_index)
            string_rest = string_rest[1:]
            multiplier +=1
            for replace_ind in replace_indices[::-1]:
                tuples_storage.pop(replace_ind)
                direction_storage.pop(replace_ind)

        true_matrix = np.zeros(matrix.shape)
        for entry in tuples_storage:
            for x, y in entry:
                true_matrix[x,y] = 1
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):
                if true_matrix[x,y] == 0:
                    matrix[x,y] = "."
        return len(tuples_storage), matrix 
    
if __name__ == "__main__":
    matrix = np.array([["X", "M", "A", "S"], ["M", "M", "M", "A"],["A", "X", "A", "M"], ["S", "M", "S", "X"]])
    matrix = np.array([list("MMMSXXMASM"),list("MSAMXMSMSA"),list("AMXSXMAAMM"),list("MSAMASMSMX"),list("XMASAMXAMM"),list("XXAMMXXAMA"),list("SMSMSASXSS"),list("SAXAMASAAA"),list("MAMMMXMMMM"),list("MXMXAXMASX")])
    search_string = "XMAS"
    checker = DayFourClass()
    length, outcome = checker.get_connections(matrix, search_string)
    print(f"There are {length} entries of {search_string} in the matrix:\n{outcome}")