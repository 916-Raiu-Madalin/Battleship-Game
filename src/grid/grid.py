class Grid:
    def __init__(self):
        self.grid = []
        for y in range(0, 10):
            row = []
            for x in range(0, 10):
                row.append("")
            self.grid.append(row)

    def get_grid(self):
        return self.grid

    def is_empty(self, x, y):
        # returns if a grid is empty or not
        if self.grid[x][y] == "":
            return True
        else:
            return False

    def addShips(self, x, y, orientation, length):
        # test that the coords are not filled, if they are empty add the ship

        if orientation == 1:
            for i in range(y, y + length):
                if self.is_empty(x, i) == False:
                    return False
            for i in range(y, y + length):
                self.grid[x][i] = int(length)

        if orientation == 2:
            for i in range(x, x + length):
                if self.is_empty(i, y) == False:
                    return False
            for i in range(x, x + length):
                self.grid[i][y] = int(length)

        return True

    def  isDefeated(self):
        for y in range(len(self.grid)):
            for x in self.grid[y]:
                if x != "" and x != "miss" and x != "hit":
                    if x >= 0 and x <= 9:
                        return False
        return True

    def playershoot(self, x, y):
        if self.grid[x][y] == "hit":
            return 'You already shot here and it was a hit', False
        if self.grid[x][y] == "miss":
            return 'You already shot here and it was a miss', False

        if self.grid[x][y] == "":
            self.grid[x][y] = "miss"
            return 'miss', False

        if self.grid[x][y] >= 0 and self.grid[x][y] <= 9:
            cop = self.grid[x][y]
            self.grid[x][y] = "hit"
            return 'hit', self.shipSunk(cop)

    def computershoot(self, x, y):
        if self.grid[x][y] == "":
            self.grid[x][y] = 'miss'
            return 'miss', False
        if self.grid[x][y] >= 0 and self.grid[x][y] <= 9:
            cop = self.grid[x][y]
            self.grid[x][y] = "hit"
            return 'hit', self.shipSunk(cop)

    def shipSunk(self, number):
        for y in range(len(self.grid)):
            for x in self.grid[y]:
                if x == number:
                    return False
        return number
