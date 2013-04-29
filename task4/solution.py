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
        self.board = [[' ' for i in range(3)] for i in range(3)]
        self.last_played = None
        self.state = None

    def __setitem__(self, square, value):
        if not (isinstance(square, str) and re.match('^[A-C][1-3]$', square)):
            raise InvalidKey
        if not value in {'X', 'O'}:
            raise InvalidValue
        if self.board[int(square[1]) - 1][ord(square[0]) - ord('A')] != ' ':
            raise InvalidMove
        if self.last_played == value:
            raise NotYourTurn
        self.board[int(square[1]) - 1][ord(square[0]) - ord('A')] = value
        self.last_played = value

    def __getitem__(self, square):
        if not (isinstance(square, str) and re.match('^[A-C][1-3]$', square)):
            raise InvalidKey
        return self.board[3 - int(square[1])][ord(square[0]) - ord('A')]

    def __str__(self):
        representation = '\n  -------------\n3 | ' +\
            ' | '.join(self.board[2]) +\
            ' |\n  -------------\n2 | ' +\
            ' | '.join(self.board[1]) +\
            ' |\n  -------------\n1 | ' +\
            ' | '.join(self.board[0]) +\
            ' |\n  -------------\n    ' +\
            'A   B   C  \n'
        return representation

    def check_if_win(self, player):
        major_diagonal = [[self.board[i][i] for i in range(3)]]
        minor_diagonal = [[self.board[i][2 - i] for i in range(3)]]
        columns = [[self.board[i][j] for i in range(3)] for j in range(3)]
        lines = self.board + columns + major_diagonal + minor_diagonal
        for line in lines:
            if set(line) == {player}:
                return True

    def is_full(self):
        for row in self.board:
            if ' ' in row:
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
