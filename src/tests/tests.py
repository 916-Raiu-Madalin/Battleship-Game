import unittest
from battleship.battleship import Battleship
from grid.grid import Grid


class TestBattleship(unittest.TestCase):
    def setUp(self):
        self._player_grid = Grid()
        self._computer_grid = Grid()
        self._battleship = Battleship(self._player_grid, self._computer_grid)

    def test_AddShipsPlayer(self):
        self._battleship.addShipsPlayer(1, 2, 1, 5)
        a = self._battleship.get_grid()
        self.assertEqual(a[1][2], 5)

    def test_AddShipsComputer(self):
        self._battleship.addShipsComputer(1, 2, 1, 5)
        a = self._battleship.getComputerGrid()
        self.assertEqual(a[1][2], 5)

    def test_PlayerTurn(self):
        a, b = self._battleship.playerTurn(1, 2)
        self.assertEqual(a, 'miss')
        self.assertEqual(b, False)

    def test_Computershoot(self):
        a, b = self._battleship.computershoot(1, 2)
        self.assertEqual(a, 'miss')
        self.assertEqual(b, False)

    def test_isDefeated(self):
        a = self._battleship.isDefeated(0)
        b = self._battleship.isDefeated(1)
        self.assertEqual(a, True)
        self.assertEqual(b, True)

    def test_getgrid(self):
        a = self._battleship.get_grid()
        self.assertNotEqual(len(a), 0)

    def test_getComputerGrid(self):
        a = self._battleship.getComputerGrid()
        self.assertNotEqual(len(a), 0)


class TestGrid(unittest.TestCase):
    def setUp(self):
        self._player_grid = Grid()
        self._computer_grid = Grid()
        self._battleship = Battleship(self._player_grid, self._computer_grid)

    def test_AddShips(self):
        self._player_grid.addShips(1, 2, 1, 5)
        b = self._player_grid.addShips(1, 2, 1, 5)
        self._player_grid.addShips(1, 2, 2, 5)
        a = self._player_grid.addShips(1, 2, 2, 5)

        self.assertEqual(b, False)
        self.assertEqual(a, False)

    def test_isDefeated(self):
        self._player_grid.addShips(5, 5, 2, 3)
        self._player_grid.isDefeated()

    def test_isEmpty(self):
        self.assertEqual(self._player_grid.is_empty(1,1),True)
        self._player_grid.addShips(1,1,1,5)
        self.assertEqual(self._player_grid.is_empty(1,1),False)

    def test_playerShot(self):
        self._player_grid.addShips(1,2,2,5)
        a,b=self._player_grid.playershoot(1,2)
        self.assertEqual(a,'hit')
        self.assertEqual(b,False)
        a,b = self._player_grid.playershoot(1,2)
        self.assertEqual(a,'You already shot here and it was a hit')
        self.assertEqual(b,False)
        self._player_grid.playershoot(1,1)
        a,b =self._player_grid.playershoot(1,1)
        self.assertEqual(a,'You already shot here and it was a miss')
        self.assertEqual(b,False)

    def test_computerShot(self):
        self._computer_grid.addShips(1,1,1,5)
        a,b =self._computer_grid.computershoot(1,1)
        self.assertEqual(a,'hit')
        self.assertEqual(b,False)

    def test_shipSunk(self):
        self._player_grid.addShips(1,1,1,2)
        self.assertEqual(self._player_grid.shipSunk(2),False)

        self._player_grid.playershoot(1,1)
        self._player_grid.playershoot(1,2)

        self.assertEqual(self._player_grid.shipSunk(2), 2)

