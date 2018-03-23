import start
import sys
import copy
import numpy

name1 = input("Name1: ")
name2 = input("Name2: ")

playerField1 = start.generate_field()
playerField2 = start.generate_field()
# print(playerField1)
# print(playerField2)
numberOf1 = 0
for i in playerField1:
    for j in i:
        if j == 1:
            numberOf1 += 1
numberOf2 = 0
for i in playerField2:
    for j in i:
        if j == 1:
            numberOf2 += 1

emptyField1 = []
for i in range(10):
    l1 = []
    emptyField1.append(l1)
for i in emptyField1:
    for j in range(10):
        i.append("0")
emptyField1 = numpy.array(emptyField1)
emptyField2 = copy.copy(emptyField1)

while True:
    trackingLst = []
    while len(trackingLst) % 2 == 0:
        print(emptyField2)
        position = input(name1 + ", enter the position of the ship: ")
        position = list(position)
        try:
            if len(position) == 2:
                firstCoord = ord(position[0]) - 65
                secondCoord = int(position[1]) - 1
                print(firstCoord, secondCoord)
            elif len(position) == 3:
                second = position[1] + position[2]
                firstCoord = ord(position[0]) - 65
                secondCoord = int(second) - 1
        except Exception:
            print("Wrong input(enter like this:'A2'")
            sys.exit()
        firstCoord = int(firstCoord)
        secondCoord = int(secondCoord)
        emptyCounter = 0
        for i in emptyField2:
            for j in i:
                if j == 1:
                    emptyCounter += 1
        if playerField2[firstCoord][secondCoord] == 1:
            emptyField2[firstCoord][secondCoord] = "X"
            print(emptyField2)
        elif emptyCounter == numberOf2:
            print("Player" + name1 + "won! Congratulations!")
            sys.exit()
        else:
            trackingLst.append("elem")

    while len(trackingLst) % 2 != 0:
        print(emptyField1)
        position = input(name2 + ", enter the position of the ship: ")
        position = list(position)
        try:
            if len(position) == 2:
                firstCoord = ord(position[0]) - 65
                secondCoord = int(position[1]) - 1
                print(firstCoord, secondCoord)
            elif len(position) == 3:
                second = position[1] + position[2]
                firstCoord = ord(position[0]) - 65
                secondCoord = int(second) - 1
        except Exception:
            print("Wrong input(enter like this:'A2'")
            sys.exit()
        firstCoord = int(firstCoord)
        secondCoord = int(secondCoord)
        emptyCounter = 0
        for i in emptyField1:
            for j in i:
                if j == 1:
                    emptyCounter += 1
        if playerField1[firstCoord][secondCoord] == 1:
            emptyField1[firstCoord][secondCoord] = "X"
            print(emptyField1)
        elif emptyCounter == numberOf2:
            print("Player" + name2 + "won! Congratulations!")
            sys.exit()
        else:
            trackingLst.append("elem")



