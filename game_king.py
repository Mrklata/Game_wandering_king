import random

import pygame


pygame.init()


class Rules:
    """General information about the game."""
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen_wight = 1500
        self.screen_height = 900
        self.window = pygame.display.set_mode((self.screen_wight, self.screen_height))
        self.enemies = []
        self.projectiles = []
        self.count_projectiles = 5
        self.mistake = 32


class Images:
    """All images."""
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
        self.bg = pygame.image.load("static_files/bg_pro.png")
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
        self.ammo = pygame.image.load("static_files/ammo.png")
        self.a1 = pygame.image.load("static_files/a1.png")
        self.a2 = pygame.image.load("static_files/a2.png")
        self.a3 = pygame.image.load("static_files/a3.png")
        self.a4 = pygame.image.load("static_files/a4.png")
        self.a5 = pygame.image.load("static_files/a5.png")
        self.ammo_kit = pygame.transform.scale(
            pygame.image.load("static_files/ammokit.png"), (40, 40)
        )
        self.enemy = pygame.transform.scale(
            pygame.image.load("static_files/enemy.png"), (64, 64)
        )


# Adding game title and creating images and rules
pygame.display.set_caption("Wandering King")
images = Images()
rules = Rules()


class Player(object):
    """Player and all his information."""
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
        """Draw player on window."""
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
    """Projectile and all its information."""
    def __init__(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height
        self.speed = 20

    def redraw(self, window, direction):
        """Draw projectile."""
        if 0 < self.x < rules.screen_wight and 0 < self.y < rules.screen_height:
            if direction == "left":
                self.x -= self.speed
                window.blit(images.arrow_left, (self.x, self.y))
            if direction == "right":
                self.x += self.speed
                window.blit(images.arrow_right, (self.x, self.y))
            if direction == "up":
                self.y -= self.speed
                window.blit(images.arrow_up, (self.x, self.y))
            if direction == "down":
                self.y += self.speed
                window.blit(images.arrow_down, (self.x, self.y))


class Ammo(object):
    """Ammo and all its information."""
    def __init__(self):
        self.x = rules.screen_wight - 200
        self.y = rules.screen_height - 200

    def redraw(self, window):
        """Draw ammo."""
        window.blit(images.ammo, (self.x, self.y))
        if rules.count_projectiles == 1:
            window.blit(images.a1, (self.x, self.y))
        if rules.count_projectiles == 2:
            window.blit(images.a2, (self.x, self.y))
        if rules.count_projectiles == 3:
            window.blit(images.a3, (self.x, self.y))
        if rules.count_projectiles == 4:
            window.blit(images.a4, (self.x, self.y))
        if rules.count_projectiles == 5:
            window.blit(images.a5, (self.x, self.y))


class AmmoKit(object):
    """Ammo kit and all its information."""
    def __init__(self):
        self.x = rules.screen_wight // 2
        self.y = rules.screen_height // 2

    def redraw(self, window):
        """Draw ammo kit"""
        window.blit(images.ammo_kit, (self.x, self.y))


class Enemy(object):
    """Enemy and all its information."""
    def __init__(self, x, y, wight, height, speed):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height
        self.speed = speed

    def redraw(self, window):
        """Draw enemy"""
        window.blit(images.enemy, (self.x, self.y))


# Creating player, ammo and ammo kit
player = Player(200, 200, 64, 64)
ammo = Ammo()
ammo_kit = AmmoKit()


def full_redraw(projectiles):
    """Redraw all objects, projectiles etc."""
    # Draw background
    rules.window.blit(images.bg, (0, 0))

    # Draw player
    player.redraw(rules.window)

    # Loop for drawing projectiles
    for p in projectiles:
        p["arrow"].redraw(rules.window, p["direction"])
        if (
            0 >= p["arrow"].x >= rules.screen_wight
            or 0 >= p["arrow"].y >= rules.screen_height
        ):
            projectiles.remove(p)

    # Loop for changing enemies positions
    for e in rules.enemies:
        if e.x > player.x and e.y > player.y:
            e.x -= e.speed
            e.y -= e.speed
        if e.x > player.x and e.y < player.y:
            e.x -= e.speed
            e.y += e.speed
        if e.x < player.x and e.y < player.y:
            e.x += e.speed
            e.y += e.speed
        if e.x < player.x and e.y > player.y:
            e.x += e.speed
            e.y -= e.speed
        if e.x == player.x and e.y < player.y:
            e.y += e.speed
        if e.x == player.x and e.y > player.y:
            e.y -= e.speed
        if e.x > player.x and e.y == player.y:
            e.x -= e.speed
        if e.x < player.x and e.y == player.y:
            e.x += e.speed

        # Draw enemies
        e.redraw(rules.window)

        # Check if projectile hit enemy, remove both when hit
        for p in projectiles:
            if (e.x + rules.mistake) > p["arrow"].x > (e.x - rules.mistake) and (
                e.y + rules.mistake
            ) > p["arrow"].y > (e.y - rules.mistake):
                projectiles.remove(p)
                # Sometimes if two projectiles hit one enemy it tried to remove same enemy twice
                try:
                    rules.enemies.remove(e)
                except ValueError:
                    print("Same enemy hit by two arrows")

    # Draw ammo and ammo kit
    ammo_kit.redraw(rules.window)
    ammo.redraw(rules.window)

    # Update window
    pygame.display.update()


def start_game():
    """Start game"""
    ticker = 0
    run = True

    # Main loop
    while run:
        rules.clock.tick(27)
        if ticker > 0:
            ticker -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Collecting ammo kit
        if (ammo_kit.x + rules.mistake // 2) >= player.x >= (
            ammo_kit.x - rules.mistake * 2
        ) and (ammo_kit.y + rules.mistake // 2) >= player.y >= (
            ammo_kit.y - rules.mistake * 2
        ):
            rules.count_projectiles = 5

        keys = pygame.key.get_pressed()

        # Move right
        if keys[pygame.K_RIGHT] and player.x < rules.screen_wight - player.wight:
            player.x += player.speed
            player.right = True
            player.left = False
            player.up = False
            player.down = False
            player.standing = False

        # Move left
        elif keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player.speed
            player.right = False
            player.left = True
            player.up = False
            player.down = False
            player.standing = False

        # Move up
        elif keys[pygame.K_UP] and player.y > 0:
            player.y -= player.speed
            player.right = False
            player.left = False
            player.up = True
            player.down = False
            player.standing = False

        # Move down
        elif keys[pygame.K_DOWN] and player.y < rules.screen_height - player.height:
            player.y += player.speed
            player.right = False
            player.left = False
            player.up = False
            player.down = True
            player.standing = False

        # Reset walk count when standing
        else:
            player.walk_count = 0

        # Fire ammo
        if keys[pygame.K_SPACE] and not player.standing and ticker == 0:
            ticker = 10
            direction = None
            if player.right:
                direction = "right"
            if player.left:
                direction = "left"
            if player.up:
                direction = "up"
            if player.down:
                direction = "down"
            if rules.count_projectiles > 0:
                rules.count_projectiles -= 1
                print(rules.count_projectiles)
                rules.projectiles.append(
                    {
                        "arrow": Projectile(player.x, player.y, 20, 20),
                        "direction": direction,
                    }
                )

        # Spawn enemy
        if keys[pygame.K_w]:
            rules.enemies.append(
                Enemy(
                    random.randint(rules.mistake, rules.screen_wight - rules.mistake),
                    random.randint(rules.mistake, rules.screen_height - rules.mistake),
                    64,
                    64,
                    random.uniform(1, 2),
                )
            )

        full_redraw(rules.projectiles)
