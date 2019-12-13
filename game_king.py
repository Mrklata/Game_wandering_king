import pygame

pygame.init()

clock = pygame.time.Clock()
screen_wight = 600
screen_height = 600
window = pygame.display.set_mode((screen_wight, screen_height))
pygame.display.set_caption("Wandering King")

walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png')]
walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png')]
walk_up = [pygame.image.load('U1.png'), pygame.image.load('U2.png'), pygame.image.load('U3.png')]
walk_down = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png')]
standing = pygame.image.load('D1.png')
bg = pygame.image.load('bg.png')


class Player(object):
    def __init__(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height
        self.speed = 7
        self.walk_count = 0
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.standing = False

    def redraw(self, window):
        if self.walk_count + 1 >= 9:
            self.walk_count = 0
        if self.right:
            window.blit(walk_right[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1

        if self.left:
            window.blit(walk_left[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1

        if self.up:
            window.blit(walk_up[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1

        if self.down:
            window.blit(walk_down[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1

        if self.standing:
            window.blit(standing, (self.x, self.y))


def full_redraw():
    window.blit(bg, (0, 0))

    player.redraw(window)
    pygame.display.update()


player = Player(200, 200, 64, 64)

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player.x < screen_wight - player.wight:
        player.x += player.speed
        player.right = True
        player.left = False
        player.up = False
        player.down = False
        player.standing = False

    elif keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player.speed
        player.right = False
        player.left = True
        player.up = False
        player.down = False
        player.standing = False

    elif keys[pygame.K_UP] and player.y > 0:
        player.y -= player.speed
        player.right = False
        player.left = False
        player.up = True
        player.down = False
        player.standing = False

    elif keys[pygame.K_DOWN] and player.y < screen_height - player.height:
        player.y += player.speed
        player.right = False
        player.left = False
        player.up = False
        player.down = True
        player.standing = False

    else:
        player.right = False
        player.left = False
        player.up = False
        player.down = False
        player.standing = True
        player.walk_count = 0

    full_redraw()
