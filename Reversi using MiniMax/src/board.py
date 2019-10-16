import numpy as np
import abminimax
import sys


# arxikopoihsh tamploy
def starterBoard():
    board = np.ones((8, 8))*(-1)
    board[3][3] = 1
    board[3][4] = 0
    board[4][3] = 0
    board[4][4] = 1
    return board


# ektypwsh tamploy
def printBoard(board):
    print("   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    print("---|---|---|---|---|---|---|---|---|")
    i = 0
    for row in board:
        printed_row = ""
        for column in row:
            if (column == int(0)):
                printed_row += "| Χ "
            elif (column == int(1)):
                printed_row += "| Ο "
            elif (column == int(2)):
                printed_row += "| * "
            else:
                printed_row += "|   "
        print(" " + str(i) + " " + printed_row + "|")
        i += 1
        print("---|---|---|---|---|---|---|---|---|")


# klonopoihsh tamplou
def copyBoards(originalBoard):
    tempBoard = np.ones((8, 8))
    for row in range(8):
        for column in range(8):
            tempBoard[row][column] = originalBoard[row][column]
    return tempBoard


# eyresh egkyron kinhsewn kai ektypwsh vohthtikoy pinaka me tis dynates kinhseis
def getBoardWithValidMoves(validBoard, tile):
    tempBoard = copyBoards(validBoard)
    validMoves = getValidMoves(tempBoard, tile)
    for x, y in validMoves:
        tempBoard[x][y] = 2
    printBoard(tempBoard)
    return validMoves


# diavasma kinhshs paixth
def getPlayerMove(board, tile, validMoves):
    while True:
        try:
            print(validMoves)
            xMove, yMove = input('Choose from valid moves [x, y]').split(" ")
            pmove = [int(xMove), int(yMove)]
            if pmove in validMoves:
                break
            else:
                print("Wrong choise")
                print(validMoves)
        except ValueError:
            print("Oops!")
            exitValue = input("Want to exit ? [Y/N]")
            if exitValue == "Y":
                sys.exit()
            else:
                continue
    return makeMove(board, tile, pmove[0], pmove[1])


# eyresh kinhshs AI1
# def getPlayerMoveAI(board, playerTile, computerTile):
    # compMove = abminimax.execute(board, computerTile, playerTile)
    # print("AI choise was: " + str(compMove))
    # return makeMove(board, playerTile, compMove[0], compMove[1])

# eyresh kinhshs AI2
def getComputerMove(board, playerTile, computerTile):
    compMove = abminimax.execute(board, playerTile, computerTile)
    print("AI choise was: " + str(compMove))
    return makeMove(board, computerTile, compMove[0], compMove[1])


# ektelesh kinhshs
def makeMove(board, tile, xstart, ystart):
    newBoard = copyBoards(board)
    tilesToFlip = isValidMove(newBoard, tile, xstart, ystart)
    if tilesToFlip is False:
        return False
    newBoard[xstart][ystart] = tile
    for x, y in tilesToFlip:
        newBoard[x][y] = tile
    return newBoard


# eyresh skor
def getScoreOfBoard(board):
    Bscore = 0
    Wscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == int(0):
                Bscore += 1
            if board[x][y] == int(1):
                Wscore += 1
    return {"0": Bscore, "1": Wscore}


# epivevaiosh egkirhs kinhshs kai lista tile gia allagh
def isValidMove(originalBoard, tile, xstart, ystart):
    board = copyBoards(originalBoard)
    # an oxi adeia kai einai sto tamplo synexise
    if board[xstart][ystart] != int(-1) or not isOnBoard(xstart, ystart):
        return False
    # arxikh thesh = tile toy paixth poy paizei
    board[xstart][ystart] = tile
    # anathesh antipaloy tile
    if tile == int(1):
        otherTile = int(0)
    else:
        otherTile = int(1)
    tilesToFlip = []
    # koitame pros oles tis kateythhnseis
    for xdir, ydir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdir
        y += ydir
        # elegxos gis entos oriwn
        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdir
            y += ydir
            if not isOnBoard(x, y):
                continue
            # oso vriskoyme antipalo tile synexizome
            while board[x][y] == otherTile:
                x += xdir
                y += ydir
                # an vgoume ektos break
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            # an ola mia xara kai vroyme dikos mas tile gyrname pros ta piso
            if board[x][y] == tile:
                # mexri na epistrepsoyme sthn arxikh thesh prosthetoyme ta tile gia allagh
                while True:
                    x -= xdir
                    y -= ydir
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    # epanaferoyme thn thesh poy valame to tile mas se kenh
    board[xstart][ystart] = int(-1)
    # an epistrafei kenh lista me tile gia allagh shmainei adynath kinhsh
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


# elegxos oti vriskomaste entos tamploy
def isOnBoard(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <= 7


# evresh listas egkyron kinhsewn
def getValidMoves(validBoard, tile):
    # Returns a list of [x,y] lists of valid moves for the given player on the given board.
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(validBoard, tile, x, y) is not False:
                validMoves.append([x, y])
    return validMoves
