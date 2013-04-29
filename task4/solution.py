class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    COLUMNS = ['A', 'B', 'C']
    ROWS = ['3', '2', '1']
    VALUES = ['X', 'O']
    SQUARES = [j+i for i in ['3', '2', '1'] for j in ['A', 'B', 'C']]

    def __init__(self):
        self.board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
                      'B1': ' ', 'B2': ' ', 'B3': ' ',
                      'C1': ' ', 'C2': ' ', 'C3': ' '}
        self.last_played = None
        self.state = None

    def __setitem__(self, square, value):
        if square not in self.board.keys():
            raise InvalidKey('{} is not a valid key'.format(square))
        if not value in self.VALUES:
            raise InvalidValue('You can put only X and O')
        if self.board[square] != ' ':
            raise InvalidMove('This square is already filled')
        if self.last_played == value:
            raise NotYourTurn("It's not your turn!")
        self.board[square] = value
        self.last_played = value

    def __getitem__(self, square):
        if square not in self.board.keys():
            raise InvalidKey('{} is not a valid key'.format(square))
        return self.board[square]

    def __str__(self):
        return ('\n' +
                '  -------------\n' +
                '3 | {} | {} | {} |\n' +
                '  -------------\n' +
                '2 | {} | {} | {} |\n' +
                '  -------------\n' +
                '1 | {} | {} | {} |\n' +
                '  -------------\n' +
                '    A   B   C  \n').format(*[self.board[square]
                                              for square in self.SQUARES])

    def check_if_win(self, player):
        major_diagonal = [self.board['A3'], self.board['B2'], self.board['C1']]
        minor_diagonal = [self.board['A1'], self.board['B2'], self.board['C3']]

        columns = [[self.board[j+i] for i in self.ROWS] for j in self.COLUMNS]
        rows = [[self.board[j+i] for j in self.COLUMNS] for i in self.ROWS]
        lines = [major_diagonal] + [minor_diagonal] + rows + columns

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
