import numpy
import matplotlib
import pygame

class Bounds:
    SCALE = 100

    def __init__(self, initial, complex_num, iterations) -> None:
        self.initial = initial
        self.complex_num = complex_num
        self.iterations = iterations
    
    # Iterative formula
    # c represents a complex number 
    def calc(z, complex_num, iterations):
        points = []

        while iterations > 0:
           iterations -= 1
           z_sum = z**2 + complex_num
           points.append((z, z_sum))
           z = z_sum
        return points
    
    def draw(win, points: list):
        # Draws a circle on the points created by the iterative formula
        for point in points:
            pygame.draw.circle(
                win, 
                (173, 216, 230), 
                (point[0] * Bounds.SCALE, point[1] * Bounds.SCALE),
                5
            )
