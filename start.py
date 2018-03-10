import random
import numpy


def read_field(myFile):
    """
    (str) -> data
    :return:
    """
    matrix = numpy.array([[0 for x in range(10)] for y in range(10)])
    maximalValue = 10
    stripList = []
    myFile = open(myFile, "r")
    for i in myFile:
        stripList.append(list(i.strip("\n")))
    for i in range(len(stripList)):
        for j in range(len(stripList[i][:maximalValue])):
            if stripList[i][j] == "*":
                matrix[i][j] = 1
            else:
                continue

    return matrix


#print(read_field("field.txt"))


def has_ship(data, tuple):
    """
    (list, tuple) -> bool
    Checks if the ship is a part of a cell
    """
    if data[ord(tuple[0])-65][tuple[1]-1] == 1:
        return True
    else:
        return False


# print(has_ship(read_field("field.txt"), ("A", 10)))


def ship_size(data, tuple):
    """
    (list, tuple) -> int
    Counts the size of the ship, which is situated in this cell
    """
    x = tuple[1]-1
    y = ord(tuple[0])-65
    checkingCell = has_ship(data, tuple)
    if checkingCell:
        sum = 1
        count = 1
        while (y + count) < 10 and data[y+count][x]:
            count += 1
            sum += 1
        count = 1
        while (y - count) > 0 and data[y-count][x]:
            count += 1
            sum += 1
        count = 1
        while (x - count) < 10 and data[y][x-count]:
            count += 1
            sum += 1
        count = 1
        while (x + count) < 10 and data[y][x+count]:
            count += 1
            sum += 1

        return sum
    return "The cell is empty"

# print(ship_size(read_field("field.txt"), ("G", 5)))


def is_valid(data):
    """
    (list) -> bool
    Takes a battle field as a parameter
    Returns is the field could be  playing one or not
    """
    lengthOfShip = []
    countOverall = []
    listWithPoints = []
    matrix = data
    maximalValue = 10
    for i in matrix:
        for j in i:
            if j == 1:
                countOverall.append(j)

    if len(countOverall) == 20:
        for i in range(len(matrix)):
            for j in range(len(matrix[i][:maximalValue])):
                if matrix[i][:maximalValue][j] == 1:
                    x_j = chr(i+65)
                    y_j = j+1
                    listWithPoints.append((x_j, y_j))

    for i in listWithPoints:
        lengthOfShip.append(ship_size(read_field("field.txt"), i))

    lOfSh = sorted(lengthOfShip)
    if (lOfSh.count(1) == 4) and (lOfSh.count(2) == 6) \
            and (lOfSh.count(3) == 6) and (lOfSh.count(4) == 4):
        return True
    else:
        return False

# print(is_valid(read_field("field.txt")))


def field_to_str(data):
    """
    (list) -> str
    Change the format to the string, which could be written into the file
    or printed out on screen
    """
    maximalValue = 10
    myStr = ""
    matrix = data
    # myStr += " |" + "1 2 3 4 5 6 7 8 9 10\n"
    myStr += " |" + "- - - - - - - - - - -\n"
    for i in range(len(matrix)):
        for j in range(len(matrix[i][:maximalValue])):
            if j == 0:
                myStr += chr(65+i) + "| " + \
                         str(matrix[i][:maximalValue][j]) + " "
            else:
                myStr += str(matrix[i][:maximalValue][j]) + " "
        myStr += "\n"
    return myStr.replace("0", " ").replace("1", "*")


# print(field_to_str(read_field("field.txt")))
def checkAround(data, tuple):
    """
    Checks free cells around the given cell
    """
    matrix = data
    if tuple[0] > 0 and tuple[1] > 0:
        if has_ship(data, (chr(tuple[0]-1 + 65), tuple[1])) == False and \
                has_ship(data, (chr(tuple[0] + 1 + 65), tuple[1])) == False and \
                has_ship(data, (chr(tuple[0] + 65), tuple[1] + 1)) == False and \
                has_ship(data, (chr(tuple[0] + 65), tuple[1] - 1)) == False:
            return True
        else:
            return False
    elif tuple[0] == 0 and tuple[1] >= 0:
        if has_ship(data, (chr(tuple[0] + 1 + 65), tuple[1])) == False and \
                has_ship(data, (chr(tuple[0] + 65), tuple[1] + 1)) == False \
                and \
                has_ship(data, (chr(tuple[0] + 65), tuple[1] - 1)) == False:
            return True
        else:
            return False


def generate_field():
    """
    () -> data
    Generates a random field, where the ships are situated
    """
    matrix = numpy.array([[0 for x in range(10)] for y in range(10)])

    x = random.randint(0, 9)
    y = random.randint(0, 6)
    for i in range(4):
        matrix[x][y] = 1
        y += 1

    for i in range(3):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        while (has_ship(matrix,(chr(x+65), y)) == True) and \
                (has_ship(matrix,(chr(x+65), y+1)) == True) and \
                (has_ship(matrix, (chr(x + 65), y-1)) == True) and \
                ((checkAround(matrix, (x, y))) == False):
            x = random.randint(0, 7)
            y = random.randint(0, 7)
        for i in range(2):
            matrix[x][y] = 1
            y += 1

    for i in range(2):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        while (has_ship(matrix,(chr(x+65), y)) == True) and \
                (has_ship(matrix,(chr(x+65), y+1)) == True) and \
                (has_ship(matrix, (chr(x + 65), y-1)) == True) and \
                ((checkAround(matrix, (x, y))) == False):
            x = random.randint(0, 8)
            y = random.randint(0, 8)
        for i in range(3):
            matrix[x][y] = 1
            y += 1

    for i in range(4):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while (has_ship(matrix,(chr(x+65), y)) == True) and \
                (has_ship(matrix,(chr(x+65), y+1)) == True) and \
                (has_ship(matrix, (chr(x + 65), y-1)) == True) and \
                ((checkAround(matrix, (x, y))) == False):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        for i in range(1):
            matrix[x][y] = 1
            y += 1

    return matrix

print(generate_field())









