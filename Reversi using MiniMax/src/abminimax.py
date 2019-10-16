import board
import random
import stateNode


def execute(game_board, playerTile, computerTile):
    # dimioyrgoyme arxikh katastash stateNode
    # den exei gonea, kamia kinhsh, o paixths mexri ekei einai o player
    # kai skor 0
    initialState = stateNode.stateNode(game_board, None, playerTile, 0, None)
    # orizoyme vathos alpha beta
    depth = 4
    alpha = -8888
    beta = 8888
    # vriskoyme to veltisto skor kai kinhsh
    # kai ton kaloyme me mizing = compyter tile
    eval = minimax(initialState, depth, alpha, beta, computerTile)
    return eval.move


def minimax(state, depth, alpha, beta, mizing):
    # an bathos 0 epistrefoyme thn axiologhsh toy state
    if(depth == 0):
        state = stateScore(state, mizing)
        return state

    # an mizing = 0 tote minimize
    # an mizing = 1 tote maximize
    if mizing:
        # arxikopoish maxvalue kai evresh egkyrwn kinhsewn
        # gia dhmioyrgia paidiwn
        maxEval = -8888
        validMoves = board.getValidMoves(state.curBoard, not state.player)
        validMoves = random.sample(validMoves, len(validMoves))
        # gia kathe validMove dhmioyrgoyme neo stateNode
        # to prosthetoyme sto parent ws paidi
        # kai kanoyme minimax gia ayto se vathos -1
        for validMove in validMoves:
            newState = board.makeMove(state.curBoard, not state.player, validMove[0], validMove[1])
            newStateNode = stateNode.stateNode(newState, validMove, not state.player, 0, state.curBoard)
            state.addChild(newStateNode)
            eval = minimax(newStateNode, depth-1, alpha, beta, 0)
            # an to paidi eixe megalhtero skor
            # apo to maxEval tote to state
            # pairnei to neoskor kai thn kinhsh
            if(eval.value > maxEval):
                state.value = eval.value
                state.move = validMove
            # an to alpha einai mikrotero
            # apo thn timh toy paidioy tote
            # ananeonoyme thn timh toy
            if(alpha < eval.value):
                alpha = eval.value
            # an to beta mikrotero toy alpha tote den xreiazetai na koitaxoyme
            # parapano
            if(beta <= alpha):
                break
            # epistrefoyme to state
        return state
        # antistoixa gia to mini
    else:
        minEval = 8888
        validMoves = board.getValidMoves(state.curBoard, not state.player)
        validMoves = random.sample(validMoves, len(validMoves))
        for validMove in validMoves:
            newState = board.makeMove(state.curBoard, not state.player, validMove[0], validMove[1])
            newStateNode = stateNode.stateNode(newState, validMove, not state.player, 0, state.curBoard)
            state.addChild(newStateNode)
            eval = minimax(newStateNode, depth-1, alpha, beta, 1)
            if(eval.value < minEval):
                state.value = eval.value
                state.move = validMove
            if(beta > eval.value):
                beta = eval.value
            if(beta <= alpha):
                break
        return state


# axiologish state
def stateScore(state, mizing):
    # koitame gia gonies
    # koitame gia diafora se tile
    # koitame gia an plhsiazoyme pleyres
    cornerMoveScore = isCornerMove(state.move)
    tileScore = getTileDifference(state, mizing)
    edgeScore = isNearEdge(state.move)
    stateScore = cornerMoveScore + tileScore + edgeScore
    # an kanoyme maximize epistrefoyme
    # thetiko thetiko scor
    # an minimize arnhtiko skor
    if mizing:
        state.value = stateScore
        return state
    else:
        state.value = -stateScore
        return state


# evresh diaforas se tile
def getTileDifference(state, mizing):
    score = board.getScoreOfBoard(state.curBoard)
    dif = 0
    # an maximize aspra - mavra
    # an minimize mavra - aspra
    if mizing:
        dif = score["1"] - score["0"]
    else:
        dif = score["0"] - score["1"]
    return dif


# an vrisketa se gonia
# an oxi 0 skor
def isCornerMove(move):
    if (isOnCorner(move[0], move[1])):
        return 20
    else:
        return 0


# an plhsiazoyme pleyres
def isNearEdge(move):
    points = 0
    if(move[0] - 0 < 3 or 7-move[0] < 1 or move[1] - 0 < 1 or 7 - move[1] < 1):
        points += 6
        if(move[0] - 0 < 1 or 7-move[0] < 1 or move[1] - 0 < 1 or 7 - move[1] < 1):
            points += 4
    return points


def isOnCorner(x, y):
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)
