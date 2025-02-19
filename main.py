import pygame
from calc import Bounds


pygame.init()

WINDOW = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Mandelbrot Set Generator")

def check_type(x):
    try:
        float(x)
        return float
    except ValueError:
        try:
            eval(x)
            return eval
        except (ValueError, SyntaxError):
            return str 
        
def power():
    while True:
        power = input("WHAT POWER OF THE MANDELBROT SET DO YOU WANT TO SEE: ")

        if check_type(power) == str:
            print("ERROR: PICK A NUMBER")
            continue
        elif check_type(power) == eval:
            Bounds.power = eval(power)
        elif float(power) < -77:
            print("ERROR: NUMBER MUST BE GREATER THAN OR EQUAL TO -77")
            continue
        elif check_type(power) == float and float(power) > 0:
            Bounds.power = float(power)
        else:
            Bounds.power = float(power)
            Bounds.z = 0.0001  # z as 0 for negative exponent would return an error
            Bounds.escape_radius = 5
            Bounds.real_range = [-3, 3]
            Bounds.imag_range = [-2, 3]
            Bounds.SCALE /= 1.5
            
        Bounds.update()
        Bounds.calc()
        break

def main():
    running = True
    clock = pygame.time.Clock()
    power()

    while running:
        clock.tick(5)
        WINDOW.fill((255,255,255))

        Bounds.draw(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()