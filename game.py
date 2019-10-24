from gui import *
from map import *
from player import *
import copy


class Game:
    def __init__(self):
        self.map = OriginalMap(220, 140, 200, 200, 4, 4)
        self.player1 = RandomPlayer(1)
        self.player2 = RandomPlayer(2)
        self.t = 0

        self.player1_pieces = [i for i in range(12)]
        for i in self.player1_pieces:
            self.map.assign_point(i, PointStatus.player_1)

        self.player2_pieces = [i for i in range(13, 25)]
        for i in self.player2_pieces:
            self.map.assign_point(i, PointStatus.player_2)

    def tick(self):
        self.t += 1
        game_copy = copy.deepcopy(self)
        player = self.player1 if self.t % 2 == 1 else self.player2
        move = player.next_move(game_copy)
        self.apply(move)

    def get_possible_moves(self):
        possible_moves = []
        pieces_available = self.player1_pieces if self.t % 2 == 1 else self.player2_pieces
        for piece_id in pieces_available:
            piece = self.map.id_to_point(piece_id)

            for i in range(-2, 3):
                for j in range(-2, 3):
                    dest_row = piece[0] + i
                    dest_column = piece[1] + j
                    if self.map.is_point_valid(dest_row, dest_column):
                        dest_id = self.map.point_to_id(dest_row, dest_column)
                        if self.map.can_move(piece_id, dest_id):
                            possible_moves.append((piece_id, dest_id))

        return possible_moves

    def apply(self, move):
        # print(move)
        if move is not None:
            outcomes = self.map.apply_move(move)

            moving_player_pieces = self.player1_pieces if self.t % 2 == 1 else self.player2_pieces
            waiting_player_pieces = self.player2_pieces if self.t % 2 == 1 else self.player1_pieces

            for outcome in outcomes:
                # Some piece died
                if outcome[1] == -1:
                    assert outcome[0] in waiting_player_pieces
                    waiting_player_pieces.remove(outcome[0])
                # A piece moved
                else:
                    assert outcome[0] in moving_player_pieces
                    moving_player_pieces.remove(outcome[0])
                    moving_player_pieces.append(outcome[1])

    def get_player_pieces(self, number):
        if number == 1:
            return self.player1_pieces
        else:
            return self.player2_pieces

    def get_player_score(self, number):
        return len(self.get_player_pieces(number)) + (12 - len(self.get_player_pieces(3 - number))) * 5

    def render(self, surface):
        self.map.render(surface)

    def copy(self, copy):
        self.map.copy(copy.map)
        copy.t = self.t
        copy.player1_pieces = self.player1_pieces.copy()
        copy.player2_pieces = self.player2_pieces.copy()
