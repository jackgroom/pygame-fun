import pygame

from board import Board


def main():
    board = Board(3, 3)
    board.print_grid()


if __name__ == "__main__":
    main()
