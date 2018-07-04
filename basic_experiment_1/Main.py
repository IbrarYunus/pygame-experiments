import pygame


def start():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((400,300))
    done = False
    is_blue = True

    x = 30
    y = 30

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3

        pygame.display.flip()
        # drawing stuff
        if is_blue:
            colour = (0, 128, 255)
        else:
            colour = (255,100,0)

        clock.tick(60)
        screen.fill((0,0,0))
        # arguments are (surface instance, colour, shape(x-y coords and width and height
        pygame.draw.rect(screen, colour, pygame.Rect(x, y, 10, 10))

        # to get key depression statuses:
        # pygame.key.get_pressed()

if __name__ == "__main__":
    start()