class State(object):

    def __init__(self, positions, x, y, width, height):

        active_cells = []

        for y, row in enumerate(positions.splitlines()):
            for x, cell in enumerate(row.strip()):
                if cell == 'o':
                    active_cells.append((x,y))

        board = [[False] * width for row in range(height)]

        for cell in active_cells:
            board[cell[1] + y][cell[0] + x] = True

        self.board = board
        self.width = width
        self.height = height

    def display(self):

        output = ''

        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if self.board[y][x]:
                    output += ' o'
                else:
                    output += ' .'
            output += '\n'

        return output
