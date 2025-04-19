#project_2_gameoflife_grid.py


from random import randint
from datastructures.array2d import Array2D  
from datastructures.kbhit import KBHit  
from project_2_gameoflife_cell import Cell


class Grid:                                                             #includes the construction of a grid using Array 2D,
                                                                        # the rules of the Game of Life, as well as how to count
    def __init__(self, rows: int, cols: int, random_seed: bool = True): #the neigbors and in using the rules how it would affect the next generation
        self.rows = rows
        self.cols = cols                                                #initialization of variables 
        self.grid = Array2D.empty(rows, cols, Cell)
        self.kb_hit = KBHit()  
        self.history = []  
        if random_seed:
            self.random_seed()

    def random_seed(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = Cell(randint(0, 1) == 1)

    def neighbor_count(self, rows: int, cols: int) -> int:
        neighbors = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1), (1, 0), (1, 1)]
        count = 0
        for drows, dcols in neighbors:
            nrows, ncols = rows + drows, cols + dcols                       #A counter to see how many of the possible 8 cell around it are filled 
            if 0 <= nrows < self.rows and 0 <= ncols < self.cols:
                if self.grid[nrows][ncols].alive:
                    count += 1
        return count

    def next_generation(self):
        new_grid = Array2D.empty(self.rows, self.cols, Cell)
        
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.neighbor_count(row, col)
                cell = self.grid[row][col]
                
                if cell.alive:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[row][col] = Cell(False)  #Cell dies from isolation or overcrowding
                    else:
                        new_grid[row][col] = Cell(True)  #Cell lives to next generation
                else:
                    if neighbors == 3:
                        new_grid[row][col] = Cell(True)  #Cell becomes alive by the condition where it needs three neighbors
                    else:
                        new_grid[row][col] = Cell(False)  #Empty cells
        
        self.grid = new_grid

    def grid_display(self):
        print("\n".join("".join(str(cell) for cell in row) for row in self.grid))

    def print_border(self):
        print("\n" + "-" * (self.cols * 2))  #Makes a border so that it can separate generations 

        
    
    def is_grid_clear(self): #makes a check to see if the grid is clear, if so the game is over
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col].alive:
                    return False  
        return True  
    
    def add_to_history(self):           #adds grid to histry but only keeps at most 5, duplicates dont seem to work too well
        self.history.append(self.grid)    
        if len(self.history) > 5:
            self.history.pop(0)

    def is_repeating(self):
        for i in range(len(self.history) - 1):
            if self.grid == self.history[i]:
                return True
        return False