import sys
import board
import random


def game_start(game_board, playerTile, computerTile, turn):
    while True:
        if turn == 'player':
            print(turn+"s turn")
            # gia ton paixth pairnoyme tis egkyres kinhseis
            # kai ektypwnoyme to voithitiko tamblo
            validMoves = board.getBoardWithValidMoves(game_board, playerTile)
            print(board.getScoreOfBoard(game_board))
            game_board = board.getPlayerMove(game_board, playerTile, validMoves)
            # an o antipalos den exei kinhseis stamatame kai ektypwnoyme skor
            if board.getValidMoves(game_board, computerTile) == []:
                break
            else:
                turn = 'computer'

        else:
            # typwnoyme enhmeromeno board
            board.printBoard(game_board)
            print(board.getScoreOfBoard(game_board))
            input("press Enter for AI turn")
            # ekteloyme kinhsh gia ton AI
            game_board = board.getComputerMove(game_board, playerTile, computerTile)
            board.printBoard(game_board)
            print(board.getScoreOfBoard(game_board))
            input("Press Enter to continue")
            # an o antipalos den exei kinhsh telos
            if board.getValidMoves(game_board, playerTile) == []:
                break
            else:
                turn = 'player'
    # sto telos typwnoyme skor
    return end_game(game_board, playerTile, computerTile)


def end_game(game_board, playerTile, computerTile):
    scores = board.getScoreOfBoard(game_board)
    if playerTile == 1:
        if scores["1"] > scores["0"]:
            print("Computer won\n" + str(scores["0"]) + " " + str(scores["1"]))
        elif scores["1"] < scores["0"]:
            print("Player won\n" + str(scores["0"]) + " " + str(scores["1"]))
        else:
            print('The game was a tie!')
    else:
        if scores["1"] > scores["0"]:
            print("Player won\n" + str(scores["0"]) + " " + str(scores["1"]))
        elif scores["1"] < scores["0"]:
            print("Computer won\n" + str(scores["0"]) + " " + str(scores["1"]))
        else:
            print('The game was a tie!')
    sys.exit()


if __name__ == "__main__":
    # arxiko board
    game_board = board.starterBoard()
    # tyxaia anathesh 0 = mavro, 1 = aspro
    # ta mavra panta prota paizoyn
    playerTile = random.randint(0, 1)
    if playerTile == 0:
        turn = "player"
        computerTile = 1
    else:
        computerTile = 0
        turn = "computer"
        playerTile = 1
    print('The ' + turn + ' will go first.')
    # ektelesh paixnidioy
    game_start(game_board, playerTile, computerTile, turn)
