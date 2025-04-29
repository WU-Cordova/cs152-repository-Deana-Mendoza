#project_2_gameoflife_cell.py

class Cell:
    def __init__(self, alive: bool = False):
        self.alive = alive
    
    def __str__(self):
        return "🦠" if self.alive else "X"
    
    def __repr__(self):
        return self.__str__()


