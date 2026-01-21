from cell import Cell
from graphics import Window
import time,random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            random.seed(seed)
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)

    def __create_cells(self):
        for col in range(self.num_cols):
            colum_cells =[]
            for row in range(self.num_rows):
                c = Cell(self.win)
                colum_cells.append(c)
            self.__cells.append(colum_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i,j)

    def __draw_cell(self,i,j):
        if self.win == None:
            return
        c = self.__cells[i][j]
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        c.draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.05)
    
    def __break_entrance_and_exit(self):
        top_left_cell = self.__cells[0][0]
        top_left_cell.has_top_wall = False
        self.__draw_cell(0,0)
        bottom_right_cell = self.__cells[self.num_cols-1][self.num_rows-1]
        bottom_right_cell.has_bottom_wall = False
        self.__draw_cell(self.num_cols-1,self.num_rows-1)

    def __break_walls_r(self,i,j):
        curr_cell = self.__cells[i][j]
        curr_cell.visited = True
        while True:
            to_visit = []
            if j > 0 and not self.__cells[i][j-1].visited:
                to_visit.append((i,j-1))
            if j < self.num_rows-1 and not self.__cells[i][j+1].visited:
                to_visit.append((i,j+1))
            if i > 0 and not self.__cells[i-1][j].visited:
                to_visit.append((i-1,j))
            if i < self.num_cols-1 and not self.__cells[i+1][j].visited:
                to_visit.append((i+1,j))
            if len(to_visit) == 0:
                self.__draw_cell(i,j)
                return
            next_i,next_j = random.choice(to_visit)
            next_cell = self.__cells[next_i][next_j]
            if next_j == j+1:
                curr_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            if next_j == j-1:
                curr_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            if next_i == i-1:
                curr_cell.has_left_wall = False
                next_cell.has_right_wall = False
            if next_i == i+1:
                curr_cell.has_right_wall = False
                next_cell.has_left_wall = False
            self.__break_walls_r(next_i,next_j)