import pygame

from board import Board
from player import Player


def main():
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        redraw_gameWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


def redraw_gameWindow():
    pass


if __name__ == "__main__":
    main()
