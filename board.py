class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[0 for c in range(self.width)]
                     for r in range(self.height)]

    def print_grid(self):
        print(self.grid)
