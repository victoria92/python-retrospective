import re


class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    def __init__(self):
        self.board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
                      'B1': ' ', 'B2': ' ', 'B3': ' ',
                      'C1': ' ', 'C2': ' ', 'C3': ' '}
        self.last_played = None
        self.state = None

    def __setitem__(self, square, value):
        if square not in self.board.keys():
            raise InvalidKey
        if not value in {'X', 'O'}:
            raise InvalidValue
        if self.board[square] != ' ':
            raise InvalidMove
        if self.last_played == value:
            raise NotYourTurn
        self.board[square] = value
        self.last_played = value

    def __getitem__(self, square):
        if square not in self.board.keys():
            raise InvalidKey
        return self.board[square]

    def __str__(self):
        representation = '\n  -------------\n3 | ' +\
            '{} | {} | {}'.format(self.board['A3'], self.board['B3'], self.board['C3']) +\
            ' |\n  -------------\n2 | ' +\
            '{} | {} | {}'.format(self.board['A2'], self.board['B2'], self.board['C2']) +\
            ' |\n  -------------\n1 | ' +\
            '{} | {} | {}'.format(self.board['A1'], self.board['B1'], self.board['C1']) +\
            ' |\n  -------------\n    ' +\
            'A   B   C  \n'
        return representation

    def check_if_win(self, player):
        major_diagonal = [[self.board['A3'], self.board['B2'], self.board['C1']]]
        minor_diagonal = [[self.board['A1'], self.board['B2'], self.board['C3']]]
        columns = [[self.board[j+str(i+1)] for i in range(3)] for j in ['A', 'B', 'C']]
        rows = [[self.board[j+str(i+1)] for j in ['A', 'B', 'C']] for i in range(3)]
        lines = major_diagonal + minor_diagonal + rows + columns
        for line in lines:
            if set(line) == {player}:
                return True

    def is_full(self):
        if ' ' in self.board.values():
            return False
        return True

    def game_status(self):
        if self.state:
            return self.state
        else:
            if self.check_if_win('X'):
                self.state = 'X wins!'
                return 'X wins!'
            elif self.check_if_win('O'):
                self.state = 'O wins!'
                return 'O wins!'
            elif self.is_full():
                self.state = 'Draw!'
                return 'Draw!'
            else:
                return 'Game in progress.'

