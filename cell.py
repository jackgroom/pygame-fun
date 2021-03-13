import pygame


class Cell():
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scale = scale

    def display(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x *
                                                   self.scale, self.y * self.scale, self.scale, self.scale))

    def print_cell(self):
        print(self.x, ' , ', self.y)
