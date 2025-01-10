import pygame
from calc import Bounds

pygame.init()

WINDOW = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Mandelbrot Set")

def main():
    running = True
    clock = pygame.time.Clock()
    points = Bounds.calc(0.15j, 20)

    while running:
        clock.tick(60)
        WINDOW.fill((0,0,0))

        Bounds.draw(WINDOW, points)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()