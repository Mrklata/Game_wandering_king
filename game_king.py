import pygame


pygame.init()


class Rules:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen_wight = 1200
        self.screen_height = 1200
        self.window = pygame.display.set_mode((self.screen_wight, self.screen_height))


class Images:
    def __init__(self):
        self.walk_left = [
            pygame.image.load("static_files/L1.png"),
            pygame.image.load("static_files/L2.png"),
            pygame.image.load("static_files/L3.png"),
        ]
        self.walk_right = [
            pygame.image.load("static_files/R1.png"),
            pygame.image.load("static_files/R2.png"),
            pygame.image.load("static_files/R3.png"),
        ]
        self.walk_up = [
            pygame.image.load("static_files/U1.png"),
            pygame.image.load("static_files/U2.png"),
            pygame.image.load("static_files/U3.png"),
        ]
        self.walk_down = [
            pygame.image.load("static_files/D1.png"),
            pygame.image.load("static_files/D2.png"),
            pygame.image.load("static_files/D3.png"),
        ]
        self.standing = pygame.image.load("static_files/D1.png")
        self.bg = pygame.image.load("static_files/bg.jpg")
        self.arrow_left = pygame.transform.scale(
            pygame.image.load("static_files/AL.png"), (50, 50)
        )
        self.arrow_right = pygame.transform.scale(
            pygame.image.load("static_files/AR.png"), (50, 50)
        )
        self.arrow_up = pygame.transform.scale(
            pygame.image.load("static_files/AU.png"), (50, 50)
        )
        self.arrow_down = pygame.transform.scale(
            pygame.image.load("static_files/AD.png"), (50, 50)
        )


pygame.display.set_caption("Wandering King")
images = Images()


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
        self.standing = True

    def redraw(self, window):
        if self.walk_count + 1 >= 9:
            self.walk_count = 0

        if self.right:
            window.blit(images.walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        if self.left:
            window.blit(images.walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        if self.up:
            window.blit(images.walk_up[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        if self.down:
            window.blit(images.walk_down[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        if self.standing:
            window.blit(images.standing, (self.x, self.y))


class Projectile(object):
    def __init__(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height
        self.speed = 20

    def redraw(self, window, direction):
        if 0 < self.x < 1200 and 0 < self.y < 1200:
            if direction == "left":
                self.x -= 10
                window.blit(images.arrow_left, (self.x, self.y))
            if direction == "right":
                self.x += 10
                window.blit(images.arrow_right, (self.x, self.y))
            if direction == "up":
                self.y -= 10
                window.blit(images.arrow_up, (self.x, self.y))
            if direction == "down":
                self.y += 10
                window.blit(images.arrow_down, (self.x, self.y))


class Enemy(object):
    def __init__(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height

    def redraw(self, window):
        window.blit(images.standing, (self.x, self.y))

enemies = []
projectiles = []
rules = Rules()
player = Player(200, 200, 64, 64)
enemy = Enemy(700, 700, 64, 64)
enemies.append(enemy)

def full_redraw(projectiles):
    rules.window.blit(images.bg, (0, 0))

    player.redraw(rules.window)
    for p in projectiles:
        p["arrow"].redraw(rules.window, p["direction"])
        if 0 >= p["arrow"].x >= 1999 or 0 >= p["arrow"].y >= 1999:
            projectiles.remove(p)
    for e in enemies:
        e.redraw(rules.window)
        for p in projectiles:
            if (e.x + 32) > p["arrow"].x > (e.x - 32) and (e.y + 32) > p["arrow"].y > (e.y - 32):
                enemies.remove(e)
                projectiles.remove(p)

    pygame.display.update()


def start_game():
    run = True
    while run:
        rules.clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player.x < rules.screen_wight - player.wight:
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

        elif keys[pygame.K_DOWN] and player.y < rules.screen_height - player.height:
            player.y += player.speed
            player.right = False
            player.left = False
            player.up = False
            player.down = True
            player.standing = False

        else:
            player.walk_count = 0
        if keys[pygame.K_SPACE]:
            direction = None
            if player.right:
                direction = "right"
            if player.left:
                direction = "left"
            if player.up:
                direction = "up"
            if player.down:
                direction = "down"
            projectiles.append(
                {
                    "arrow": Projectile(player.x, player.y, 20, 20),
                    "direction": direction,
                }
            )

        full_redraw(projectiles)
