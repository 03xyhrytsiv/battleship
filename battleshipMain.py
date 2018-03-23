import start
import sys
import copy
import numpy


class Field:
    """
    Class Field creates playing field with randomly situated ships,
    counts number of ship pieces and creates an empty field
    """
    def generatingFields(self):
        """
        :return: generated field with randomly situated ships
        """
        playerField = start.generate_field()
        return playerField

    def numberOf(self, generating):
        """
        :param generating: the field itself
        :return: number of pieces of ships on the field
        """
        numberOf1 = 0
        for i in generating:
            for j in i:
                if j == 1:
                    numberOf1 += 1
        return numberOf1

    def emptyField(self):
        """
        :return: empty list fo lists
        """
        emptyField1 = []
        for i in range(10):
            l1 = []
            emptyField1.append(l1)
        for i in emptyField1:
            for j in range(10):
                i.append("0")
        return numpy.array(emptyField1)


class Game(Field):
    """
    Takes Field as a superclass to inherit field options from there
    Represents the game itself
    Takes two parameters: two names of the players
    """
    def __init__(self, name1, name2):
        """
        Initializing names of players
        """
        self.name1 = name1
        self.name2 = name2

    def theGame(self):
        """
        The main game, where the players play their games
        """
        playerField1 = Field.generatingFields(self)
        playerField2 = Field.generatingFields(self)
        numberOf1 = Field.numberOf(self, playerField1)
        numberOf2 = Field.numberOf(self, playerField2)
        emptyField1 = Field.emptyField(self)
        emptyField2 = copy.copy(emptyField1)
        while True:
            trackingLst = []
            while len(trackingLst) % 2 == 0:
                # print(emptyField2)
                myStr = ""
                print("   1 2 3 4 5 6 7 8 9 10")
                maximalValue = 10
                myStr += " |" + "- - - - - - - - - - -\n"
                for i in range(len(emptyField2)):
                    for j in range(len(emptyField2[i][:maximalValue])):
                        if j == 0:
                            myStr += chr(65 + i) + "| " + \
                                     str(emptyField2[i][:maximalValue][j]) + " "
                        elif j == 9:
                            myStr += str(emptyField2[i][:maximalValue][j]) + " "
                            myStr += "\n"
                        else:
                            myStr += str(emptyField2[i][:maximalValue][j]) + " "
                print(myStr)
                position = input(self.name1 + ", enter the position of the ship: ")
                position = list(position)
                try:
                    if len(position) == 2:
                        firstCoord = ord(position[0]) - 65
                        secondCoord = int(position[1]) - 1
                    elif len(position) == 3:
                        second = position[1] + position[2]
                        firstCoord = ord(position[0]) - 65
                        secondCoord = int(second) - 1
                except Exception:
                    print("Wrong input(enter like this:'A2')")
                    sys.exit()
                firstCoord = int(firstCoord)
                secondCoord = int(secondCoord)
                emptyCounter = 0
                for i in emptyField2:
                    for j in i:
                        if j == 1:
                            emptyCounter += 1
                try:
                    if playerField2[firstCoord][secondCoord] == 1:
                        emptyField2[firstCoord][secondCoord] = "✔"
                    elif emptyCounter == numberOf2:
                        print("Player" + self.name1 + "won! Congratulations!")
                        sys.exit()
                    elif playerField2[firstCoord][secondCoord] != 1 \
                            and playerField2[firstCoord][secondCoord] != "✔":
                        emptyField2[firstCoord][secondCoord] = "⚫"
                        trackingLst.append("elem")
                except Exception:
                    print("Wrong input(enter like this:'A2')")
                    sys.exit()


            while len(trackingLst) % 2 != 0:
                myStr = ""
                print("  1 2 3 4 5 6 7 8 9  10")
                maximalValue = 10
                myStr += " |" + "- - - - - - - - - - -\n"
                for i in range(len(emptyField1)):
                    for j in range(len(emptyField1[i][:maximalValue])):
                        if j == 0:
                            myStr += chr(65 + i) + "| " + \
                                     str(emptyField1[i][:maximalValue][j]) + " "
                        elif j == 9:
                            myStr += str(emptyField1[i][:maximalValue][j]) + " "
                            myStr += "\n"
                        else:
                            myStr += str(emptyField1[i][:maximalValue][j]) + " "
                print(myStr)
                position = input(self.name2 + ", enter the position of the ship: ")
                position = list(position)
                try:
                    if len(position) == 2:
                        firstCoord = ord(position[0]) - 65
                        secondCoord = int(position[1]) - 1
                    elif len(position) == 3:
                        second = position[1] + position[2]
                        firstCoord = ord(position[0]) - 65
                        secondCoord = int(second) - 1
                except Exception:
                    print("Wrong input(enter like this:'A2')")
                    sys.exit()
                firstCoord = int(firstCoord)
                secondCoord = int(secondCoord)
                emptyCounter = 0
                for i in emptyField1:
                    for j in i:
                        if j == 1:
                            emptyCounter += 1
                try:
                    if emptyCounter == numberOf1:
                        print("Player" + self.name2 + "won! Congratulations!")
                        sys.exit()
                    elif playerField1[firstCoord][secondCoord] == 1:
                        emptyField1[firstCoord][secondCoord] = "✔"
                    elif playerField1[firstCoord][secondCoord] != 1 \
                            and playerField1[firstCoord][secondCoord] != "✔":
                        emptyField1[firstCoord][secondCoord] = "⚫"
                        trackingLst.append("elem")
                except Exception:
                    print("Wrong input(enter like this:'A2')")
                    sys.exit()


name1 = input("Name1: ")
name2 = input("Name2: ")
# running the game
gamer = Game(name1, name2)
print(gamer.theGame())













