import pygame
from calc import Bounds


pygame.init()

WINDOW = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Mandelbrot Set Generator")

def main():
    running = True
    clock = pygame.time.Clock()
    Bounds.calc()

    while running:
        clock.tick(20)
        WINDOW.fill((255,255,255))

        Bounds.draw(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()