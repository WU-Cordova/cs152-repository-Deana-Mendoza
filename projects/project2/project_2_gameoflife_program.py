#project_2_gameoflife_program.py


from project_2_gameoflife_gamecontroller import GameController


if __name__ == "__main__":                  #runs the main program
    game = GameController(15, 15)
    game.run_game()