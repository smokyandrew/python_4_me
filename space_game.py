import pygame, controls
from gun import Gun


def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Garou loves beating up")
    bg_color = (12, 3, 45)
    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()


run()