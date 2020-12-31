import random


class Battleship:
    def __init__(self, grid_player, grid_computer):
        self.grid = grid_player
        self.grid_computer = grid_computer

    def addShips(self, length):
        orientation = 0
        while orientation != 1 and orientation != 2:
            try:
                orientation = int(input("Would you like the ship to be horizontal [1] or vertical [2]: "))
            except:
                orientation = 0

        # while valid ship has not been added
        while True:
            if orientation == 1:
                x, y = self.input_coords(9, 10 - length)
                check = self.grid.addShips(x, y, 1, length)
                self.grid.show_player_grid()
                if check == True:
                    break

            if orientation == 2:
                x, y = self.input_coords(10 - length, 9)
                check = self.grid.addShips(x, y, 2, length)
                self.grid.show_player_grid()
                if check == True:
                    break


    def input_coords(self, maxX, maxY):
        x = -1
        y = -1
        while x < 0 or x > maxX:
            try:
                x = int(input("Enter X coordinate between " + str(0) + " and " + str(maxX) + ": "))
            except:
                x = -1
        while y < 0 or y > maxY:
            try:
                y = int(input("Enter y coordinate between " + str(0) + " and " + str(maxY) + ": "))
            except:
                y = -1
        return x, y

    def addComputerShips(self, length):

        orientation = random.randint(1, 2)

        while True:
            if orientation == 1:
                x = random.randint(0, 9)
                y = random.randint(0, 10 - length)
                check = self.grid_computer.addShips(x, y, 1, length)
                if check == True:
                    break
            if orientation == 2:
                x = random.randint(0, 10 - length)
                y = random.randint(0, 9)
                check = self.grid_computer.addShips(x, y, 2, length)
                if check == True:
                    break

    def playerTurn(self):
        self.grid_computer.show_grid()
        x, y = self.input_coords(9, 9)
        a,b =self.grid_computer.playershoot(x, y)
        return a,b

    def computershoot(self, x, y):
        a,b = self.grid.computershoot(x, y)
        return a,b

    def isDefeated(self, side):
        if side == 0:
            return self.grid.isDefeated(side)
        elif side == 1:
            return self.grid_computer.isDefeated(side)

    def show_player_grid(self):
        self.grid.show_grid()

