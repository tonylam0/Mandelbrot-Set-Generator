import numpy as np
import pygame


class Bounds:
    SCALE = 350

    # Creates a range for real and imaginary numbers
    # Increasing the amount of points increases the accuracy
    points = 1000
    real_range = np.linspace(-2, 1, points)
    imag_range = np.linspace(-1.5, 1.5, points)

    # Creates a 2D grid for the complex plane
    real, imag = np.meshgrid(real_range, imag_range)

    # Outputs a list of lists containing real array + imaginary array * j
    c_values = real + imag * 1j
    iterations = np.zeros(c_values.shape)

    escape_radius = 2
    
    # Iterative formula
    # c represents a complex number 
    def calc():
        # Will return 500 for each due to range 
        for real in range(Bounds.c_values.shape[0]):
            print(f"Computing: {int(real/Bounds.points*100+1)}% done")
            for imag in range(Bounds.c_values.shape[1]):
                z = 0
                c = Bounds.c_values[real, imag]  # Treated as coordinate in the 2D plane
                max_iterations = 100

                for i in range(max_iterations):
                    z = z**2 + c
                    
                    # Tracks when z unbounds
                    # i > 0 prevents escaped c's to be colored the same as bounded
                    if abs(z) > Bounds.escape_radius and i > 0:
                        Bounds.iterations[real, imag] = i
                        # print(f"Point {c.round(2)} escaped at iteration {i}")
                        break
    
    def draw(win):
        for real in range(Bounds.c_values.shape[0]):
            for imag in range(Bounds.c_values.shape[1]):
                c = Bounds.c_values[real, imag] 
                color = (
                    Bounds.iterations[real, imag] * 5 % 255, 
                    Bounds.iterations[real, imag] * 10 % 255, 
                    Bounds.iterations[real, imag] * 15 % 255
                )

                pygame.draw.circle(
                    win, 
                    color, 
                    (c.real * Bounds.SCALE + 1400 / 2, c.imag * Bounds.SCALE + 800 / 2),
                    1
                )
