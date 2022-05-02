import pygame

pygame.joystick.init()


def goo():
    print(pygame.joystick.get_init())
    print(pygame.joystick.get_count())


joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
goo()
pygame.init()
while True:
    pygame.time.Clock().tick(27)
    for event in pygame.event.get():

        if event.type == pygame.JOYBUTTONUP:
            print(event.value)
        if event.type == pygame.JOYHATMOTION:
            print(event.value)
