import pygame

from board import Board
from player import Player

width = height = 500
board = None

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("game")


def setup():
    global board

    scale = 40
    board = Board(width, height, scale)


def draw():
    board.display_board(window)


def main():
    setup()

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


if __name__ == "__main__":
    main()
