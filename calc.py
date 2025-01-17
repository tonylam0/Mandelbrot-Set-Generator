import numpy as np
import pygame


class Bounds:
    SCALE = 350
    power = 2
    z = 0

    # Creates a range for real and imaginary numbers
    # Increasing the amount of points increases the accuracy
    points = 1000
    real_range = np.linspace(-2, 1, int(points))
    imag_range = np.linspace(-1.5, 1.5, int(points))

    # Creates a 2D grid for the complex plane
    real, imag = np.meshgrid(real_range, imag_range)

    # Outputs a list of lists containing real array + imaginary array * j
    c_values = real + imag * 1j
    coordinates = {}
    escape_radius = 2

    # Used to update values when power is set
    # Cap point multiplier by 50
    def update():
        Bounds.points = 1000 + abs(Bounds.power) * abs(50 - Bounds.power) % 50
        real_range = np.linspace(-2, 1, int(Bounds.points))
        imag_range = np.linspace(-1.5, 1.5, int(Bounds.points))

        real, imag = np.meshgrid(real_range, imag_range)

        Bounds.c_values = real + imag * 1j
        Bounds.coordinates = {}
    
    # Mandelbrot's recursive formula
    # c represents a complex number 
    def calc():
        # Will return numbers of points in ranges
        for real in range(Bounds.c_values.shape[0]):
            print(f"Computing: {int(real/Bounds.points*100+1)}% done")
            for imag in range(Bounds.c_values.shape[1]):
                z = Bounds.z
                c = Bounds.c_values[real, imag]  # Treated as coordinate in the 2D plane
                max_iterations = 100
                Bounds.coordinates[(real, imag)] = 0

                for i in range(max_iterations):
                    z = z**Bounds.power + c  # Formula can be changed to illustrate other fractals
                    
                    # Tracks when z unbounds
                    # i > 0 prevents escaped c's to be colored the same as bounded
                    if abs(z) > Bounds.escape_radius and i > 0:
                        Bounds.coordinates[real, imag] = i  # - np.log2(np.log2(abs(z) + 1e-10))
                        break
    
    
    def draw(win):
        for coordinate, i in Bounds.coordinates.items():
            c = Bounds.c_values[coordinate[0], coordinate[1]] 
            color = (
                i * 5 % 255, 
                i * 10 % 255, 
                i * 15 % 255
            )

            pygame.draw.circle(
                win, 
                color, 
                (c.real * Bounds.SCALE + 1400 / 2, c.imag * Bounds.SCALE + 800 / 2),
                1
            )