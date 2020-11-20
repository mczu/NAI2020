from ocean import *

class battle:

    def StartGame(playerOcean: Ocean, aiOcean: Ocean): 
        """
        Summary:
        Method that control whole game and players turns.

        Parameters:
        playerOcean (Ocean): representing player instance of Ocean with placed Ships
        aiOcean (Ocean): representing AI instance of Ocean with placed Ships
        """

        __playerTurn = True

        while (playerOcean.health != 0 and aiOcean.health != 0):
            if (__playerTurn):
                aiOcean.RenderOcean(False)
                print("PLAYER TURN")

                print("Select row and col to shoot")
                row = int(input("Row "))
                col = int(input("Col "))

                if (aiOcean.IsInMatrixRange(row, col)):
                    __playerTurn = aiOcean.Shoot(row, col)
                else:
                    print("Selected cell out of field. Repeating turn")
            else:
                print("AI TURN")
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                
                __playerTurn = not playerOcean.Shoot(row, col)

                print("Player ocean after AI turn")
                playerOcean.RenderOcean(True)

            print("Player HP = " + str(playerOcean.health))
            print("AI HP = " + str(aiOcean.health))
            input("Enter anything to continue")

        if playerOcean.health == 0:
            print("AI WIN")
        elif aiOcean.health == 0:
            print ("PLAYER WIN")