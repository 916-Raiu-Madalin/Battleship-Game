import random


class Battleship:
    def __init__(self, grid_player, grid_computer):
        self.grid = grid_player
        self.grid_computer = grid_computer

    def addShipsPlayer(self,x, y, z, length):
        return self.grid.addShips(x,y,z,length)

    def addShipsComputer(self,x,y,z,length):
        return self.grid_computer.addShips(x, y, z, length)

    def playerTurn(self,x,y):
        a, b = self.grid_computer.playershoot(x, y)
        return a, b

    def computershoot(self, x, y):
        a, b = self.grid.computershoot(x, y)
        return a, b

    def isDefeated(self, side):
        if side == 0:
            return self.grid.isDefeated()
        elif side == 1:
            return self.grid_computer.isDefeated()

    def get_grid(self):
        a = self.grid.get_grid()
        return a

    def getComputerGrid(self):
        a =self.grid_computer.get_grid()
        return a