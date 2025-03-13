#project_2_gameoflife_controller.py

import time
from project_2_gameoflife_grid import Grid

class GameController:                                                     #controls how to run game, initiates running manual 
                                                                          #and automatic and it also inlcudes kbhit commands
    def __init__(self, rows: int, cols: int, random_seed: bool = True):
        self.controller = Grid(rows, cols, random_seed)                   #initializes game and makes a grid 
    
    def run_game(self):                                                    
        print("Choose your mode:")
        print("Press 'M' for Manual Mode")                                #kbhit commands for the different modes
        print("Press 'A' for Automatic Mode")
        print("Press 'Q' to Quit")
        
        while True:
            if self.controller.kb_hit.kbhit():
                key = self.controller.kb_hit.getch()
                if key == "Q":
                    print("You quit the game!")
                    break
                elif key == "A":
                    print("Switching to Automatic Mode")
                    self.automatic()
                    break
                elif key == "M":
                    print("Switching to Manual Mode")
                    self.manual()
                    break

    def automatic(self):                   #This is the method accessed when user chooses manual mode
        while True:
            self.controller.print_border()  
            self.controller.grid_display()
            self.controller.add_to_history()
            
            if self.controller.is_repeating():                      #checks to see any repreating grids. If so, breaks code and stops
                print("This will continue to repeat. Game Over!")
                break
            
            if self.controller.is_grid_clear():                         
                print("There are no alive cells. Game Over!")       #checks to see if grid is clear. If so, breaks code and stops
                break
            
            self.controller.next_generation()
            time.sleep(1)               #works to check that the next generation updates after 1 second "sleep"

    def manual(self):                   #This is the method accessed when user chooses manual mode 
        while True:                         
            self.controller.print_border()  
            self.controller.grid_display()
            
            self.controller.add_to_history()
            
            if self.controller.is_repeating():                          #checks to see any repreating grids. If so, breaks code and stops
                print("This will continue to repeat. Game Over!")
                break
            

            if self.controller.is_grid_clear():                         #checks to see if grid is clear. If so, breaks code and stops
                print("There are no alive cells. Game Over!")
                break
            
            if self.controller.kb_hit.kbhit():
                key = self.controller.kb_hit.getch()
                if key == "Q":
                    print("You quit the game!")
                    break
                elif key == "A":
                    print("Switching to Automatic Mode")
                    self.run_automatic()
                    break
                elif key == "M":
                    self.controller.next_generation()  
            time.sleep(0.1)  
