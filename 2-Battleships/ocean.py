from os import system, name
from console import clearConsole
import random

class Ocean:

    def __init__(self):
        """
        Summary:
        Initializing class field.

        Parameters:
        __matrix (array): private array 2-dimension used to represent board
        __output (list): private list to contains all string to render board
        __ships (array): array 1-dimension array represent lenght of all available ships
        healt (int): number of health point at start of game
        """

        self.__matrix = [["" for colm in range(0,10)] for row in range(0,10)]
        self.__output = ["" for x in range(35)]
        self.__ships = [6, 4, 4, 3, 3, 2, 2]
        self.health = 24

    def PlaceshipsOnOceanForAI(self):
        """
        Summary:
        AI CUI for placing ships on his ocean (board)
        """

        for ship in self.__ships:
            while(True):
                row = random.randint(0, 9)
                col = random.randint(0, 9)

                optionList = ["UP", "DOWN", "LEFT", "RIGHT"]
                direction = random.choice(optionList)
                
                if self.__IsOutOfRange(row, col, direction, ship) or self.__checkAllDirection(row, col, direction, ship):
                    continue
                else:
                    self.__placeShip(row, col, direction, ship)
                    break

    def PlaceShipsOnOceanForPlayer(self):
        """
        Summary:
        Player CUI for placing ships on his own ocean (board)
        """

        for ship in self.__ships:
            while(True):
                clearConsole()
                self.RenderOcean(True)
                print("Place ship leng: " + str(ship))
                row = int(input("Row "))
                col = int(input("Column "))
                direction = input("Choose direction write: UP, DOWN, LEFT or RIGHT ")

                if self.__IsOutOfRange(row, col, direction, ship) or self.__checkAllDirection(row, col, direction, ship):
                    print("Ship place out of range of ocean or is next to other ship")
                    input("Enter anything to continue")
                else:
                    self.__placeShip(row, col, direction, ship)
                    break
        
        self.RenderOcean(True)

    def RenderOcean(self, renderShips: bool):
        """
        Summary:
        Render in console Ocean board.

        Parameters:
        renderShips (bool): Checking if can render ships or require to hide them all
        """


        if self.__output is not None:
            self.__output = ["" for x in range(35)]

        colIdx = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for index in range(0,11):
            if index == 0:
                self.__addCellToString(0, True, "")

                for col in colIdx:
                    self.__addCellToString(0, True, col)
            else:
                outputIdx = index * 3

                for col in colIdx:
                    if col == "0":
                        self.__addCellToString(outputIdx, False, colIdx[index - 1])
                        self.__addCellToString(outputIdx, False, self.__renderShip(index - 1, colIdx.index(col), renderShips))
                    else:
                        self.__addCellToString(outputIdx, False, self.__renderShip(index - 1, colIdx.index(col), renderShips))

        for index in range(0, len(self.__output)):
            print(self.__output[index])

    def Shoot(self, row:int, col: int):
        """
        Summary:
        Shoot to enemy ship! Method replace on board cell text to "X" if hit part of ship ("S") or "O" if hit empty cell.

        Parameters:
        row (int): Index of row in matrix
        col (int): Index of column in matrix

        Returns:
        bool: True if hit enemy ship or hit already selected cell or False if hit empty cell.
        """

        if self.__matrix[row][col] == "S":
            self.__matrix[row][col] = "X"
            self.health -= 1
            print("Bullet hit enemy ship. Giving extra shot.")
            return True
        elif self.__matrix[row][col] == "":
            self.__matrix[row][col] = "O"
            return False
        elif (self.__matrix[row][col] == "X" or self.__matrix[row][col] == "O"):
            print("This cell was already selected. Repeating turn")
            return True

    def __renderShip(self, row: int, col: int, renderShips: bool):
        """
        Summary:
        Checking if can render part of ship on board

        Parameters:
        row (int): Index of row in matrix
        col (int): Index of column in matrix
        renderShips (bool): If False then checking is cell contains part of Ship

        Returns:
        string: self.__matrix[row][col] value if renderShip is True else checking if self.__matrix[row][col] does not contains part of ship and return empty string.
        """
        
        if not renderShips:
                if self.__matrix[row][col] == "S":
                    return ""
        
        return self.__matrix[row][col]

    def __IsOutOfRange(self, row: int, col: int, direction: str, shipLenght: int):
        """
        Summary:
        Verifying if ship to place is out of range

        Parameters:
        row (int): Index of row in matrix
        col (int): Index of column in matrix
        direction (str): Direction string
        shipLenght (int): Lenght of current ship
        """

        if direction == "UP":
            return row - shipLenght < 0
        elif direction == "DOWN":
            return row + shipLenght > 9
        elif direction == "LEFT":
            return col - shipLenght < 0
        else: 
            return col + shipLenght > 9

    def __addCellToString(self, index: int, isFirstRow: bool, msg: str):
        """
        Summary:
        Private method to add to output string another cell.

        Parameters:
        index (int): Index of output lane to modify
        isFirstRow (bool): If True then adding additional line with indexes of columns
        msg (str): Cell text
        """

        if msg == "":
            msg = " "

        if isFirstRow:
            self.__output[0] += "-----"
            self.__output[1] += " " + msg + "  *"
            self.__output[2] += "    *"
            self.__output[3] += "-----"
        else:
            self.__output[index + 1] += " "+ msg +"  *"
            self.__output[index + 2] += "    *"
            self.__output[index + 3] += "-----"

    def __placeShip(self, row: int, col: int, direction: str, shipLenght: int):
        """
        Summary:
        Placing ship on board that start in cell[row][cell] to shipLenght position in expected direction

        Parameters:
        row (int): Selected index of row from ocean
        col (int): Selected index of column from ocean
        direction (str): Direction string
        shipLength (int): Lenght of current ship
        """

        for i in range(0, shipLenght):
            if direction == "UP":
                self.__matrix[row - i][col] = "S"
            elif direction == "DOWN":
                self.__matrix[row + i][col] = "S"
            elif direction == "LEFT":
                self.__matrix[row][col - i] = "S"
            else: 
                self.__matrix[row][col + i] = "S"

    def __checkAllDirection(self, row: int, col: int, direction: str, shipLenght: int):
        """
        Summary:
        Verifying if is possible to place ship in starts from cell[row][col] in [direction] with [shipLenght] lenght.

        Parameters:
        row (int): Selected index of row from ocean
        col (int): Selected index of column from ocean
        direction (str): direction string
        shipLength (int): lenght of current ship

        Returns:
        bool: Returning True if all cells around expected ship position is clear. False if any cell around is part of other ship ("S")
        """
        
        result = True

        for i in range(0, shipLenght):
            if direction == "UP":
                result = self.__checkIsCellsAroundEmpty(row - i, col)
            elif direction == "DOWN":
                result = self.__checkIsCellsAroundEmpty(row + i, col)
            elif direction == "LEFT":
                result = self.__checkIsCellsAroundEmpty(row, col - i)
            elif direction == "RIGHT":
                result = self.__checkIsCellsAroundEmpty(row, col + i)
            
            if result == False:
                return True

        return False

    def __checkIsCellsAroundEmpty(self, row: int, col: int):
        """
        Summary:
        Checking if all cells around and center is empty.

        Parameters:
        row (int): Selected index of row from ocean
        col (int): Selected index of column from ocean

        Returns:
        bool: Returning True or False
        """

        return (self.__checkCell(row - 1, col - 1) and
                self.__checkCell(row - 1, col) and
                self.__checkCell(row - 1, col + 1) and
                self.__checkCell(row, col - 1) and
                self.__checkCell(row, col) and
                self.__checkCell(row, col + 1) and
                self.__checkCell(row + 1, col - 1) and
                self.__checkCell(row + 1, col) and
                self.__checkCell(row + 1, col + 1))

    def __checkCell(self, row: int ,col: int):
        """
        Summary:
        Checking if cell[row][col] is in matrix range and currently empty

        Parameters:
        row (int): Selected index of row from ocean
        col (int): Selected index of column from ocean

        Returns:
        bool: Returning True if cell is out of range or empty. False if cell contains already Ship part ("S")
        """

        if (self.IsInMatrixRange(row,col)):
            return self.__matrix[row][col] != "S"
        else:
            return True

    def IsInMatrixRange(self, row: int, col: int):
        """
        Summary:
        Checking if cell[row][col] is in matrix range

        Parameters:
        row (int): Selected index of row from ocean
        col (int): Selected index of column from ocean

        Returns:
        bool: Returning True cell is in matrix range. False is is out of range.
        """

        return ((row >= 0 and row <= 9) and ( col >= 0 and col <= 9))
