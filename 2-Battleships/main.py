# Rules: https://pl.wikipedia.org/wiki/Okr%C4%99ty
#
# tl;dr:
# On board: S - Ship, X - Hitted ship with shot, O - Missed shot
# Row - Indexes on the left of board; Col - Indexes on the top of board
# Do not place ship next another one (min 1 square of free space)
# Find and hit all parts of enemy ships
#
# Authors:
# Magdalena Czubek
# Julian Chodorowski
#
# Prepare environment:
# - Required installed Python probably in 3.0 version or newer
# - Open cmd, move to folder with game files and open game with command main.py 

from ocean import *
from battle import *

def main():
    """
        Summary:
        Main method to launch game menu.
        """

    while True:
        option = input('''
        Choose option:
        (1) Start game
        (2) Exit game
        ''')

        if option == '1':
            playerOcean = Ocean()
            playerOcean.PlaceShipsOnOceanForPlayer()
            aiOcean = Ocean()
            aiOcean.PlaceshipsOnOceanForAI()
            battle.StartGame(playerOcean, aiOcean)

        elif option == '2':
            exit("Thanks for playing")

main()