import numpy
import matplotlib
import pygame

class Bounds:
    SCALE = 50

    def __init__(self, complex_num, iterations) -> None:
        self.complex_num = complex_num
        self.iterations = iterations
    
    # Iterative formula
    # c represents a complex number 
    def calc(points, z, complex_num, iterations):
        if iterations > 0:
           iterations -= 1
           z = z**2 + complex_num
           points.append((z.real, z.imag))
        return points, z, iterations
    
    def draw(win, points: list):
        # Draws a circle on the points created by the iterative formula
        print(points)
        if len(points) > 1:
            pygame.draw.lines(win, (230, 230, 250), False, points)

        for idx, point in enumerate(points):
            pygame.draw.circle(
                win, 
                (173, 216, 230), 
                (point[0] * Bounds.SCALE + 1000 / 2, point[1] * Bounds.SCALE + 800 / 2),
                2.5
            )

            print(points[idx][0] * Bounds.SCALE + 1000 / 2, points[idx][1] * Bounds.SCALE + 800 / 2)

            if len(points) > 1:
                pygame.draw.line(
                    win, 
                    (230, 230, 250), 
                    (points[idx][0] * Bounds.SCALE + 1000 / 2, points[idx][1] * Bounds.SCALE + 800 / 2),
                    (points[idx-1][0] * Bounds.SCALE + 1000 / 2, points[idx-1][1] * Bounds.SCALE + 800 / 2)
                )

