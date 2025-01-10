import numpy
import matplotlib
import pygame

class Bounds:
    SCALE = 10000

    def __init__(self, complex_num, iterations) -> None:
        self.complex_num = complex_num
        self.iterations = iterations
    
    # Iterative formula
    # c represents a complex number 
    def calc(complex_num, iterations):
        points = []
        z = 0

        while iterations > 0:
           iterations -= 1
           z = z**2 + complex_num
           points.append((z.real, z.imag))
        return points
    
    def draw(win, points: list):
        # Draws a circle on the points created by the iterative formula
        for point in points:
            pygame.draw.circle(
                win, 
                (173, 216, 230), 
                (point[0] * Bounds.SCALE + 1000 / 2, point[1] * Bounds.SCALE + 800 / 2),
                5
            )
