import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    def test_maze_create_cells2(self):
        num_cols = 23
        num_rows = 15
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._Maze__cells[0]),
            num_rows,
        )
    def test_maze_create_cells3(self):
        num_cols = 50
        num_rows = 50
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m3._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m3._Maze__cells[0]),
            num_rows,
        )
    def test__break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit()
        c1 = m1._Maze__cells[0][0]
        c2 = m1._Maze__cells[num_cols-1][num_rows-1]
        self.assertFalse(
            c1.has_top_wall
        )
        self.assertFalse(
            c2.has_bottom_wall
        )

    def test__reset_visited(self):
        num_cols = 12
        num_rows = 10
        seed = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10,None,seed)
        m1._Maze__break_entrance_and_exit()
        m1._Maze__break_walls_r(0,0)
        m1._Maze__reset_visited()
        c1 = m1._Maze__cells[0][0]
        c2 = m1._Maze__cells[num_cols-1][num_rows-1]
        self.assertFalse(
            c1.visited
        )
        self.assertFalse(
            c2.visited
        )




if __name__ == "__main__":
    unittest.main()