from cell import Cell


class Board():
    def __init__(self, width, height, scale):
        self.width = int(width / scale)
        self.height = int(height / scale)
        self.scale = scale

        self.grid = [[Cell(r, c, self.scale) for c in range(self.width)]
                     for r in range(self.height)]

    def display_board(self, window):
        for i in range(0, self.width):
            for j in range(0, self.height):
                self.grid[i][j].display(window)
