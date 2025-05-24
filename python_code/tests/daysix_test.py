import pytest 
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.day6.main import DaySixClass


class TestDaySixClass:
    def test_check_connections(self):
        checker = DaySixClass()
        input_maze = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."
        maze_visited, visited, length = checker.run_through_maze(input_maze = input_maze)
        assert length == 41

    def test_check_raise_Value_Error_Wrong_Input_Letter(self):
        checker = DaySixClass()
        input_maze = "....#.....\n.........A\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."
        with pytest.raises(ValueError):
            maze_visited, visited, length = checker.run_through_maze(input_maze = input_maze)
        
    def test_check_raise_Value_Error_Wrong_Input_Dimensions(self):
        checker = DaySixClass()
        input_maze = "....#.....\n.........\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."
        with pytest.raises(ValueError):
            maze_visited, visited, length = checker.run_through_maze(input_maze = input_maze)

    def test_check_raise_Value_Error_Wrong_No_Player(self):
        checker = DaySixClass()
        input_maze = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#........\n........#.\n#.........\n......#..."
        with pytest.raises(ValueError):
            maze_visited, visited, length = checker.run_through_maze(input_maze = input_maze)

    def test_check_raise_Value_Error_Infinite_Loop(self):
        checker = DaySixClass()
        input_maze = "....#.....\n.........#\n..........\n..#.......\n.......#..\n....#.....\n.#.#^#....\n....#...#.\n#.........\n......#..."
        with pytest.raises(ValueError):
            maze_visited, visited, length = checker.run_through_maze(input_maze = input_maze)