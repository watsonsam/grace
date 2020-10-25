import unittest
import cell
import maze


class MyTestCase(unittest.TestCase):
    def test_new_cell_has_four_borders(self):
        the_cell = cell.Cell()
        self.assertEqual(the_cell.north, True)
        self.assertEqual(the_cell.south, True)
        self.assertEqual(the_cell.east, True)
        self.assertEqual(the_cell.west, True)

    def test_new_cell_is_not_visited(self):
        the_cell = cell.Cell()
        self.assertNotEqual(the_cell.visited, True)

    def test_new_maze_has_correct_number_of_cells(self):
        the_maze = maze.Maze(2, 3)
        self.assertEqual(the_maze.width, 2)
        self.assertEqual(the_maze.height, 3)
        self.assertEqual(len(the_maze.grid), 6)

    def test_correct_neighbours_returned(self):
        the_maze = maze.Maze(3, 3)
        neighbours = the_maze.get_neighbours(1, 1)
        self.assertEqual(len(neighbours), 4)
        self.assertIn((1, 0), neighbours)
        self.assertIn((1, 2), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((0, 1), neighbours)

        neighbours = the_maze.get_neighbours(0, 0)
        self.assertEqual(len(neighbours), 2)
        self.assertIn((1, 0), neighbours)
        self.assertIn((0, 1), neighbours)

        neighbours = the_maze.get_neighbours(2, 2)
        self.assertEqual(len(neighbours), 2)
        self.assertIn((2, 1), neighbours)
        self.assertIn((1, 2), neighbours)

    def test_joined_cells_have_correct_borders(self):
        the_maze = maze.Maze(3, 3)
        the_maze.join_cells((0, 0), (1, 0))
        self.assertEqual(the_maze.grid[(0, 0)].east, False)
        self.assertEqual(the_maze.grid[(1, 0)].west, False)

        the_maze = maze.Maze(3, 3)
        the_maze.join_cells((1, 0), (0, 0))
        self.assertEqual(the_maze.grid[(0, 0)].east, False)
        self.assertEqual(the_maze.grid[(1, 0)].west, False)

        the_maze = maze.Maze(3, 3)
        the_maze.join_cells((0, 0), (0, 1))
        self.assertEqual(the_maze.grid[(0, 0)].south, False)
        self.assertEqual(the_maze.grid[(0, 1)].north, False)

        the_maze = maze.Maze(3, 3)
        the_maze.join_cells((1, 2), (1, 1))
        self.assertEqual(the_maze.grid[(1, 2)].north, False)
        self.assertEqual(the_maze.grid[(1, 1)].south, False)


    #def test_cannot_join_non_contiguous_cells(self):


if __name__ == '__main__':
    unittest.main()
