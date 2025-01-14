import numpy as np
import pygame


class Bounds:
    SCALE = 350

    # Creates a range for real and imaginary numbers
    real_range = np.linspace(-2, 1, 1000)
    imag_range = np.linspace(-1.5, 1.5, 1000)

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
                        print(f"Point {c.round(2)} escaped at iteration {i}")
                        break
    
    def draw(win):
        for real in range(Bounds.c_values.shape[0]):
            for imag in range(Bounds.c_values.shape[1]):
                c = Bounds.c_values[real, imag] 
                if Bounds.iterations[real, imag] > 75: 
                    color = (255, 165, 0)
                elif 50 < Bounds.iterations[real, imag] <= 75: 
                    color = (255, 0, 0)
                elif 20 < Bounds.iterations[real, imag] <= 50: 
                    color = (255, 255, 0)
                # elif 15 < Bounds.iterations[real, imag] <= 25: 
                #     color = (0, 122, 204)
                elif 12 < Bounds.iterations[real, imag] <= 20: 
                    color = (204,51,0)
                elif 0 < Bounds.iterations[real, imag] <= 12: 
                    color = (51, 0, 102)
                elif Bounds.iterations[real, imag] == 0:
                    color = (25, 0, 51)

                pygame.draw.circle(
                    win, 
                    color, 
                    (c.real * Bounds.SCALE + 1400 / 2, c.imag * Bounds.SCALE + 800 / 2),
                    5
                )
