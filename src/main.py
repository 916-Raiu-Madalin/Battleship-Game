
from Ui.UI import Ui
from battleship.battleship import Battleship
from grid.grid import Grid

if __name__ == '__main__':
    player_grid = Grid()
    computer_grid = Grid()
    battleship = Battleship(player_grid, computer_grid)
    ui = Ui(battleship)
    play = "yes"
    ui.PVE()
    while play == "yes":
        print("Do you want to play again?")
        play = input("yes or no: ")
        if play == "yes":
            player_grid = Grid()
            computer_grid = Grid()
            battleship = Battleship(player_grid, computer_grid)
            ui = Ui(battleship)
            ui.PVE()
