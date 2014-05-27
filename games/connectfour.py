#!/usr/bin/env python2

# Overhaul, still missing the logic though


from random import randint

class Board(object):

    def __init__(self, width, height, player_char, npc_char, first_turn):
        self.width = width
        self.height = height
        self.data = ["_" for x in range(width) for y in range(height)]
        self.player_char = player_char
        self.npc_char = npc_char

        # validate the first_turn arg
        if first_turn not in ("player", "npc"):
            raise ValueError("first_turn must be either 'player' or 'npc'")

        self.whose_turn = first_turn

    def __repr__(self):
        s = ""
        for i, c in enumerate(self.data):
            if i % self.width == 0:
                s += "\n"
            s += c
        return s

    def _2d_to_1d(self, x, y):
        return x * self.width + y

    def __getitem__(self, coords):
        return self.data[self._2d_to_1d(*coords)]

    def __setitem__(self, coords, value):
        self.data[self._2d_to_1d(*coords)] = value

    def drop_coin(self, column):
        """print self
        if self[(0, column)] != "_":
            return False
        else:
            for i in range(1,-1,-1):
                if self[(i, column)] == "_":
                    if self.whose_turn == "npc":
                        self[(i, column)] = self.npc_char
                        print "through"
                        self.whose_turn == "player"
                        return True
                    else:
                        self[(i, column)] = self.player_char
                        self.whose_turn == "npc"
                        return True"""

    def is_game_over(self):
        # return True if somebody won
        return False

    def reset_board(self):
        # clear the board back to the default character
        pass


class NPC(object):

    def __init__(self, name):
        self.name = name

    def take_turn(self, board):
        column = randint(0,6)
        board.drop_coin(column)


if __name__ == "__main__":
    npc = NPC("Fred")
    board = Board(7, 6, "X", "O", "npc")
    while not board.is_game_over():
        if board.whose_turn == "npc":
            print("It's %s's turn" % npc.name)
            npc.take_turn(board)
        else:
            coin_dropped = False
            while not coin_dropped:
                column = int(raw_input("Enter a column number (0-6)."))
                board.drop_coin(column)

    print("Game over. The winner is %s!" % board.whose_turn)
