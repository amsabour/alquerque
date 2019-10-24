import random
import copy


class Player:
    def __init__(self, number):
        self.number = number

    def next_move(self, game):
        raise NotImplementedError("This should be implemented")


class RandomPlayer(Player):
    def next_move(self, game):
        possible_moves = game.get_possible_moves()
        if len(possible_moves) > 0:
            move = possible_moves[random.randint(0, len(possible_moves) - 1)]
            move = possible_moves[0]
        else:
            move = None
        return move
