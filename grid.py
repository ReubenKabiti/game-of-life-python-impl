import pygame
import numpy as np

class Grid:

    def __init__(self, nr, nc):

        self.grid = np.zeros((nr, nc))
    
    def clear(self):
        self.grid = np.zeros(self.grid.shape)

    def update(self, display_size):
        # update each cell

        grid = self.grid.copy()

        for r, row in enumerate(self.grid):
            for c, col in enumerate(row):

                is_alive = self.is_alive(r, c)
                num_alive_n = 0
                neighbours = self.get_neighbours(r, c)
                for n in neighbours:
                    if self.is_alive(*n):
                        num_alive_n += 1
                if is_alive:
                    if num_alive_n == 2 or num_alive_n == 3:
                        grid[r][c] = 1
                    else:
                        grid[r][c] = 0
                else:
                    if num_alive_n == 3:
                        grid[r][c] = 1
                    
        self.grid = grid

    def check_mouse_press(self, display_size):
        x, y = pygame.mouse.get_pos()

        r, c = self.convert_to_grid_space(display_size, x, y)

        if pygame.mouse.get_pressed()[0]:
            self.grid[r][c] = 1
        elif pygame.mouse.get_pressed()[2]:
            self.grid[r][c] = 0

    def is_alive(self, r, c):
        return self.grid[r][c] >= 1

    def get_neighbours(self, r, c):
        n = [
                [r, c - 1],
                [r - 1, c - 1],
                [r - 1, c],
                [r - 1, c + 1],
                [r, c + 1],
                [r + 1, c + 1],
                [r + 1, c],
                [r + 1, c - 1]
        ]

        nr, nc = self.grid.shape

        n = filter(lambda x: x[0] >= 0 and x[1] >= 0 and x[0] < nr and x[1] < nc, n)

        return n

    def convert_to_grid_space(self, display_size, x, y):
        u = x / display_size.width
        v = y / display_size.height

        r = self.grid.shape[0] * v
        c = self.grid.shape[1] * u

        return (int(r), int(c))

    def draw(self, display):

        dw = display.get_rect().width # display width
        dh = display.get_rect().height # display height

        rh = dh //  self.grid.shape[0] # rectangle height
        rw = dw // self.grid.shape[1] # rectangle width

        for r, row in enumerate(self.grid):

            for c, col in enumerate(row):

                u = c / self.grid.shape[1]
                v = r / self.grid.shape[0]

                x = int(u * dw)
                y = int(v * dh)
                color = pygame.Color(227, 61, 148)
                if col >= 0.4:
                    color = (0, 0, 0, 0)
                pygame.draw.rect(display, color, pygame.Rect((x, y), (rw, rh)))
                pygame.draw.rect(display, (0, 0, 0), pygame.Rect((x, y), (rw, rh)), 1)
