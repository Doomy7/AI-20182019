class stateNode:
    # arxikopoishs arxikoy node katastashs
    def __init__(self, curBoard, move, player, value=0, parentBoard=None, children=[]):
        self.__curBoard = curBoard
        self.__parentBoard = parentBoard
        self.__move = move
        self.__player = player
        self.__value = value
        self.__children = []

    # torino board
    @property
    def curBoard(self):
        return self.__curBoard

    # parent board
    @property
    def parentBoard(self):
        return self.__parentBoard

    # kinhsh apo to parent sto current
    @property
    def move(self):
        return self.__move

    # axiologhsh current
    @property
    def value(self):
        return self.__value

    # tile paixth
    @property
    def player(self):
        return self.__player

    # paidia toy current tile
    @property
    def children(self):
        return self.__children

    @curBoard.setter
    def curBoard(self, curBoard):
        self.__curBoard = curBoard

    @parentBoard.setter
    def parentBoard(self, parentBoard):
        self.__parentBoard = parentBoard

    @move.setter
    def move(self, move):
        self.__move = move

    @value.setter
    def value(self, value):
        self.__value = value

    @player.setter
    def player(self, player):
        self.__player = player

    @children.setter
    def children(self, children):
        self.__children = children

    def addChild(self, childNode):
        self.__children.append(childNode)

    # ektypvsh node
    def print(self):
        print(self.__curBoard, self.__parentBoard, self.__move, self.__value, self.__player, self.__children)
        print("\n")

    # ektyposh paidiwn
    def printChildren(self):
        for children in self.__children:
            children.print()

    # clonopoihsh state
    def copyState(self, state):
        self.__curBoard = state.curBoard
        self.__parentBoard = state.parentBoard
        self.__move = state.move
        self.__player = state.player
        self.__value = state.value
        self.__children = state.children
