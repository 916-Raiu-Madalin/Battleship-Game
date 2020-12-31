class Grid:
    def __init__(self):
        self.grid = []
        for y in range(0, 10):
            row = []
            for x in range(0, 10):
                row.append("")
            self.grid.append(row)

    def show_grid(self):
        # add the top coordinates for the grid
        print("-" * 45)
        line = ""
        for i in range(10):
            line += "| " + str(i) + " "
        print(line + "||   |")
        print("-" * 45)

        # add the cells
        for y in range(len(self.grid)):
            line = ""
            for x in self.grid[y]:
                if x == "":
                    line += "| - "
                elif x == "miss":
                    line += "| " + '\033[91m'+"X "+'\033[0m'
                elif x == "hit":
                    line += "| "+ '\033[32m'+"O "+'\033[0m'
                else:
                    line += "| - "

            # add the side coordinates
            line += "|| " + str(y) + " |\n"

            for x in self.grid[y]:
                line += "____"
            line += "_____"
            print(line)

    def show_player_grid(self):
        # add the top coordinates for the grid
        print("-" * 45)
        line = ""
        for i in range(10):
            line += "| " + str(i) + " "
        print(line + "||   |")
        print("-" * 45)

        # add the cells
        for y in range(len(self.grid)):
            line = ""
            for x in self.grid[y]:
                if x == "":
                    line += "| - "
                else:
                    line += "| " + str(x) + " "

            # add the side coordinates
            line += "|| " + str(y) + " |\n"

            for x in self.grid[y]:
                line += "____"
            line += "_____"
            print(line)

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

    def isDefeated(self, side):
        if side == 0:
            for y in range(len(self.grid)):
                for x in self.grid[y]:
                    if x!="" and x!="miss" and x!="hit":
                        if x >= 0 and x <= 9:
                            return False
            return True
        if side == 1:
            for y in range(len(self.grid)):
                for x in self.grid[y]:
                    if x!="" and x!="miss" and x!="hit":
                        if x >= 0 and x <= 9:
                            return False
            return True

    def playershoot(self, x, y):
        if self.grid[x][y] == "hit":
            return 'You already shot here and it was a hit',False
        if self.grid[x][y] == "miss":
            return 'You already shot here and it was a miss',False

        if self.grid[x][y] == "":
            self.grid[x][y] = "miss"
            return 'miss',False

        if self.grid[x][y] >= 0 and self.grid[x][y] <= 9:
            cop = self.grid[x][y]
            self.grid[x][y] = "hit"
            return 'hit',self.shipSunk(cop)

    def computershoot(self, x, y):
        if self.grid[x][y] == "":
            self.grid[x][y] = 'miss'
            return 'miss',False
        if self.grid[x][y] >= 0 and self.grid[x][y] <= 9:
            cop= self.grid[x][y]
            self.grid[x][y] = "hit"
            return 'hit',self.shipSunk(cop)

    def shipSunk(self,number):
        for y in range(len(self.grid)):
            for x in self.grid[y]:
                if x == number:
                    return False
        return number