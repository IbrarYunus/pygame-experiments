import pygame
import os

_image_library = {'stomba': '..\/resources\stomba.png'}


def get_image(path):
    global _image_library
    image = pygame.image.load(_image_library.get(path))

    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


def start():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('[!] EXITING')
                done = True
        screen.fill((0, 0, 0))

        screen.blit(get_image('stomba'), (20, 20))
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    start()
