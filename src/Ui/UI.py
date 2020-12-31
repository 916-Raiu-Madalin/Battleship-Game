import time
import random


class Ui:
    def __init__(self, battleship):
        self.battleship = battleship

    def addShips(self):
        ships = [6, 5, 4, 3, 2]
        for i in range(0, 5):
            print("You are curently plancing a ship with the length of " + str(ships[i]))
            self.battleship.addShips(ships[i])

    def addComputerShips(self):
        ships = [6, 5, 4, 3, 2]
        for i in range(0, 5):
            self.battleship.addComputerShips(ships[i])

    def PVE(self):

        print("Now we are going to add your ships")

        # add ships for player 1
        print("Player 1 add ships.")
        print("You input the root coordinate of the ship which is extended up or right")

        # add ships

        self.addShips()
        input("Press enter to continue...")
        self.clearScreen()

        # add ships for computer
        print("The computer is placing his ships, please wait")
        time.sleep(2)
        self.clearScreen()
        self.addComputerShips()
        print("The computer has added the ships, may the battle begin!")
        input("Press enter to continue...")
        self.clearScreen()
        # list of coords the computer should shoot
        computerWaitList = []
        computerShotList = []

        while self.battleship.isDefeated(0) == False and self.battleship.isDefeated(1) == False:
            turn = 1
            # If player 1 turn
            if turn == 1:
                print("Player 1's turn to shoot.")
                x = 1
                y=False
                while x != 'miss' and x != 'hit':
                    x,y = self.battleship.playerTurn()

                print("You " + str(x))
                if y != False:
                    print("The ship with length "+str(y)+" has sank! ")

                input("Press enter to continue...")
                self.clearScreen()

            # check if game is won or not
            if self.battleship.isDefeated(1) == True:
                self.clearScreen()
                print("Player 1 wins!!")
                input("Press enter to continue...")
                self.clearScreen()
                return
            # if game is not won,computers turn

            turn = 2
            if turn == 2:
                print("Computer's turn to shoot")

                valid = False
                while valid == False:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    # if there are coords on the waiting list it takes them from there

                    if computerWaitList:
                        x = computerWaitList[0][0]
                        y = computerWaitList[0][1]
                        computerWaitList.pop(0)
                    alreadyshot = False
                    # if proposed x and y coordinate are already used then repeat loop
                    for coord in computerShotList:
                        if coord == [x, y]:
                            alreadyshot = True
                    if alreadyshot == False:
                        valid = True

                print("Computer is deciding...")
                time.sleep(1)
                # shoot with coords and also add them to used coords
                sunkRez = False
                computerShotList.append([x, y])
                shootResult, sunkRez = self.battleship.computershoot(x,y)
                print("Computer shot at " +str(x)+" "+str(y))

                #if the computer hit try adding smart coords to wait list
                if shootResult == "hit":
                    print("The computer hit!")
                    if sunkRez != False:
                        print("The ship with length " + str(sunkRez) + " has sank! ")
                    self.battleship.show_player_grid()
                    if sunkRez != False:
                        while len(computerWaitList) % 4 !=0:
                            computerWaitList.pop(0)
                    if x+1 <=9:
                        computerWaitList.append([x+1,y])
                    if y+1 <=9:
                        computerWaitList.append([x,y+1])
                    if x-1 >=0:
                        computerWaitList.append([x-1,y])
                    if y-1 >=0:
                        computerWaitList.append([x,y-1])
                else:
                    print("The computer missed!")
                    self.battleship.show_player_grid()
                input("Press enter to continue...")

                #check game is won or not
                if self.battleship.isDefeated(0) == True:
                    self.clearScreen()
                    print("Computer wins!!")
                    input("press enter to continue...")
                    self.clearScreen()
                    return



    def clearScreen(self):
        print("\n" * 30)
