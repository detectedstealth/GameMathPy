import pygame

pygame.init()
screen_width = 1080
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

white = pygame.Color(255, 255, 255)

def to_pygame_coordinates(display, x, y):
    """Changes the origin to the bottom left instead of top left (default)"""
    return x, display.get_height() - y


def draw_pisces_stars():
    # Horizontal path
    position = to_pygame_coordinates(screen, 100, 100)
    pygame.draw.rect(screen, white, (position[0], position[1], 20, 20))
    position = to_pygame_coordinates(screen, 160, 85)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 200, 110)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 320, 115)
    pygame.draw.rect(screen, white, (position[0], position[1], 15, 15))
    position = to_pygame_coordinates(screen, 400, 110)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 480, 90)
    pygame.draw.rect(screen, white, (position[0], position[1], 18, 18))
    # Vertical path
    position = to_pygame_coordinates(screen, 440, 140)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 360, 240)
    pygame.draw.rect(screen, white, (position[0], position[1], 15, 15))
    position = to_pygame_coordinates(screen, 348, 280)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 280, 440)
    pygame.draw.rect(screen, white, (position[0], position[1], 15, 15))
    # Final circle path
    position = to_pygame_coordinates(screen, 260, 500)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 230, 530)
    pygame.draw.rect(screen, white, (position[0], position[1], 15, 15))
    position = to_pygame_coordinates(screen, 250, 560)
    pygame.draw.rect(screen, white, (position[0], position[1], 8, 8))
    position = to_pygame_coordinates(screen, 280, 580)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 320, 560)
    pygame.draw.rect(screen, white, (position[0], position[1], 15, 15))
    position = to_pygame_coordinates(screen, 320, 520)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 300, 490)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))

def draw_virgo_stars():
    position = to_pygame_coordinates(screen, 530, 200)
    pygame.draw.rect(screen, white, (position[0], position[1], 20, 20))
    position = to_pygame_coordinates(screen, 650, 260)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 720, 258)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 820, 320)
    pygame.draw.rect(screen, white, (position[0], position[1], 15, 15))
    position = to_pygame_coordinates(screen, 780, 420)
    pygame.draw.rect(screen, white, (position[0], position[1], 15, 15))
    
    position = to_pygame_coordinates(screen, 600, 100)
    pygame.draw.rect(screen, white, (position[0], position[1], 18, 18))
    position = to_pygame_coordinates(screen, 658, 120)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 690, 90)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 780, 115)
    pygame.draw.rect(screen, white, (position[0], position[1], 15, 15))
    position = to_pygame_coordinates(screen, 800, 180)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 880, 260)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 940, 280)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    position = to_pygame_coordinates(screen, 1010, 380)
    pygame.draw.rect(screen, white, (position[0], position[1], 10, 10))
    

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw_pisces_stars()
    draw_virgo_stars()
    

    pygame.display.update()

pygame.quit()
