#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module can be used to solve a sudoku puzzle."""

# Sudoku Solver
# Solution in Python

# Example sudoku board
# ┌-----------------------┐
# | . . . | . 9 . | . . 4 |
# | 4 1 . | . . 3 | . . . |
# | 8 . 7 | 6 . 4 | 2 1 . |
# |-------|-------|-------|
# | . . 1 | . . 7 | . . 2 |
# | . 6 . | . 4 . | . 9 . |
# | 2 . . | 5 . . | 7 . . |
# |-------|-------|-------|
# | . 4 8 | 3 . 6 | 9 . 7 |
# | . . . | 4 . . | . 2 1 |
# | 6 . . | . 1 . | . . . |
# └-----------------------┘

TEST_BOARD = [[0, 0, 0, 0, 9, 0, 0, 0, 4],
              [4, 1, 0, 0, 0, 3, 0, 0, 0],
              [8, 0, 7, 6, 0, 4, 2, 1, 0],
              [0, 0, 1, 0, 0, 7, 0, 0, 2],
              [0, 6, 0, 0, 4, 0, 0, 9, 0],
              [2, 0, 0, 5, 0, 0, 7, 0, 0],
              [0, 4, 8, 3, 0, 6, 9, 0, 7],
              [0, 0, 0, 4, 0, 0, 0, 2, 1],
              [6, 0, 0, 0, 1, 0, 0, 0, 0]]

def display_puzzle(board):
    """Prints the sudoku puzzle in a user-friendly way."""
    print '┌-----------------------┐'
    for i, row in enumerate(board):
        if i != 0 and i % 3 == 0:
            print '|-------|-------|-------|'
        for j, cell in enumerate(row):
            if j % 3 == 0:
                print '|',
            print cell,
        print '|'
    print '└-----------------------┘'

display_puzzle(TEST_BOARD)
