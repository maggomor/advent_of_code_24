from pydantic import BaseModel
import numpy as np
from typing import Union

class DaySixClass(BaseModel):
    input_maze: str = None
    maze_array: list = None

    def __post_init__(self, input_maze:str = None, maze_array:list = None):
        self.input_maze = input_maze
        self.maze_array = maze_array

    def validate_maze(self, legitimate_symbols:str = ["\n", "#", ".", "^", ">", "v", "<"], input_maze: str = None):
        self.input_maze = input_maze
        val = False
        if 1 == len(set([len(x) for x in input_maze.split('\n')])):
            if np.sum(np.array([input_maze.count(symbol) for symbol in ["^", ">", "v", "<"]])) == 1:
                if all([x in legitimate_symbols for x in list(set(input_maze))]):
                    val = True
        if val:
            return True
        else:
            raise ValueError("Input Maze has the wrong format")
        
    def save_maze_array(self):
        try:
            self.maze_array = np.array([[x] for x in self.input_maze.split("\n")])
            return self.maze_array
        except Exception as e:
            raise ValueError(f"No Maze found: {e}")

    def locate_player_and_direction(self):
        for i in range(len(self.maze_array)):
            if self.maze_array[i][0].find("^") != -1:
                return np.array([i, self.maze_array[i][0].find("^")]), np.array([-1,0])
            elif self.maze_array[i][0].find(">") != -1:
                return np.array([i, self.maze_array[i][0].find(">")]), np.array([0,1])
            elif self.maze_array[i][0].find("v") != -1:
                return np.array([i, self.maze_array[i][0].find("v")]), np.array([1,0])
            elif self.maze_array[i][0].find("<") != -1:
                return np.array([i, self.maze_array[i][0].find("<")]), np.array([0,-1])
    
    def locate_next_obstacle(self, maze_array:np.ndarray = None, location: np.ndarray = None, direction: np.ndarray = None, visited_locations: list = []):
        current_location = location
        visited_locations.append(current_location)
        exit_found = False
        right_wing_turn = {str(np.array([-1,0])): np.array([0,1]), str(np.array([0,1])): np.array([1,0]), str(np.array([1,0])): np.array([0, -1]), str(np.array([0,-1])): np.array([-1,0])}
        while True:
            new_location = current_location + direction
            if ((new_location[0] < 0) | (new_location[1] < 0) | (new_location[0] > maze_array.shape[0] -1) | (new_location[1] > (len(maze_array[0][0]) -1))):
                exit_found = True
                break
            if maze_array[new_location[0]][0][new_location[1]] == "#":
                direction = right_wing_turn[str(direction)]
                break
            elif any([all((new_location in loc) & (new_location != location)) for loc in (visited_locations)]):
                raise ValueError("Endless Loop encountered, there is no exit.")
                break
            else: 
                current_location = new_location
                visited_locations.append(current_location)
        return exit_found, current_location, direction, visited_locations
    
    def mark_locations(self, maze_array, visited):
        for visited_location in visited:
            new_string = maze_array[visited_location[0]][0][:visited_location[1]] + "X" + maze_array[visited_location[0]][0][visited_location[1]+1:]
            maze_array[visited_location[0]] = [new_string]
        return maze_array
    
    def turn_maze_array_into_string(self, maze_array):
        return "\n".join(x[0] for x in maze_array)
    
    def run_through_maze(self, input_maze:str = None):
        if self.validate_maze(input_maze=input_maze):
            self.maze_array = self.save_maze_array()
            location, direction = self.locate_player_and_direction()
            val, new_loc, new_direc, visited = False, location, direction, []
            while not val:
                val, new_loc, new_direc, visited = self.locate_next_obstacle(maze_array=self.maze_array, location = new_loc, direction = new_direc, visited_locations=visited)
            new_maze = self.maze_array.copy()
            maze_visited = self.mark_locations(new_maze, visited)
            maze_visited_string = self.turn_maze_array_into_string(maze_visited)
            return maze_visited_string, f"{len(list(set([str(x.tolist()) for x in visited])))} different unique points have been visited by the guard."
        else:
            raise ValueError("Maze that was entered is not as required.")
    
if __name__ == "__main__":
    input_maze = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."
    checker = DaySixClass()
    maze_visited, visited = checker.run_through_maze(input_maze = input_maze)
    print("Path of the guard is as follows:")
    print(maze_visited)
    print(visited)