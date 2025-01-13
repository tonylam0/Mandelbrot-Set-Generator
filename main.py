import pygame
from calc import Bounds

pygame.init()

WINDOW = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Mandelbrot Set")

def main():
    running = True
    clock = pygame.time.Clock()
    points = []
    iterations = 200
    z = 0

    while running:
        clock.tick(20)
        WINDOW.fill((0,0,0))

        points, z, iterations = Bounds.calc(points, z, 0.8j, iterations)
        Bounds.draw(WINDOW, points)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()