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
        self.score = 0.0
        self.kills = 0
        self.font = pygame.font.SysFont("Times New Roman", 18)


class Images:
    """All images."""

    def __init__(self):
        self.walk_left = [
            pygame.image.load("static_files/walk_left/1.png"),
            pygame.image.load("static_files/walk_left/2.png"),
            pygame.image.load("static_files/walk_left/3.png"),
            pygame.image.load("static_files/walk_left/4.png"),
            pygame.image.load("static_files/walk_left/5.png"),
            pygame.image.load("static_files/walk_left/6.png"),
        ]
        self.walk_left_up = [
            pygame.image.load("static_files/walk_left_up/1.png"),
            pygame.image.load("static_files/walk_left_up/2.png"),
            pygame.image.load("static_files/walk_left_up/3.png"),
            pygame.image.load("static_files/walk_left_up/4.png"),
            pygame.image.load("static_files/walk_left_up/5.png"),
            pygame.image.load("static_files/walk_left_up/6.png"),
        ]
        self.walk_left_down = [
            pygame.image.load("static_files/walk_left_down/1.png"),
            pygame.image.load("static_files/walk_left_down/2.png"),
            pygame.image.load("static_files/walk_left_down/3.png"),
            pygame.image.load("static_files/walk_left_down/4.png"),
            pygame.image.load("static_files/walk_left_down/5.png"),
            pygame.image.load("static_files/walk_left_down/6.png"),
        ]
        self.walk_right = [
            pygame.image.load("static_files/walk_right/1.png"),
            pygame.image.load("static_files/walk_right/2.png"),
            pygame.image.load("static_files/walk_right/3.png"),
            pygame.image.load("static_files/walk_right/4.png"),
            pygame.image.load("static_files/walk_right/5.png"),
            pygame.image.load("static_files/walk_right/6.png"),
        ]
        self.walk_right_up = [
            pygame.image.load("static_files/walk_right_up/1.png"),
            pygame.image.load("static_files/walk_right_up/2.png"),
            pygame.image.load("static_files/walk_right_up/3.png"),
            pygame.image.load("static_files/walk_right_up/4.png"),
            pygame.image.load("static_files/walk_right_up/5.png"),
            pygame.image.load("static_files/walk_right_up/6.png"),
        ]
        self.walk_right_down = [
            pygame.image.load("static_files/walk_right_down/1.png"),
            pygame.image.load("static_files/walk_right_down/2.png"),
            pygame.image.load("static_files/walk_right_down/3.png"),
            pygame.image.load("static_files/walk_right_down/4.png"),
            pygame.image.load("static_files/walk_right_down/5.png"),
            pygame.image.load("static_files/walk_right_down/6.png"),
        ]
        self.walk_up = [
            pygame.image.load("static_files/walk_up/1.png"),
            pygame.image.load("static_files/walk_up/2.png"),
            pygame.image.load("static_files/walk_up/3.png"),
            pygame.image.load("static_files/walk_up/4.png"),
            pygame.image.load("static_files/walk_up/5.png"),
            pygame.image.load("static_files/walk_up/6.png"),
        ]
        self.walk_down = [
            pygame.image.load("static_files/walk_down/1.png"),
            pygame.image.load("static_files/walk_down/2.png"),
            pygame.image.load("static_files/walk_down/3.png"),
            pygame.image.load("static_files/walk_down/4.png"),
            pygame.image.load("static_files/walk_down/5.png"),
            pygame.image.load("static_files/walk_down/6.png"),
        ]
        self.standing = pygame.image.load("static_files/walk_down/1.png")
        self.bg = pygame.image.load("static_files/bg_pro.png")
        self.arrow_left = pygame.transform.scale(
            pygame.image.load("static_files/AL.png"), (50, 50)
        )
        self.arrow_left_up = pygame.transform.scale(
            pygame.image.load("static_files/ALU.png"), (25, 25)
        )
        self.arrow_left_down = pygame.transform.scale(
            pygame.image.load("static_files/ALD.png"), (25, 25)
        )
        self.arrow_right = pygame.transform.scale(
            pygame.image.load("static_files/AR.png"), (50, 50)
        )
        self.arrow_right_up = pygame.transform.scale(
            pygame.image.load("static_files/ARU.png"), (25, 25)
        )
        self.arrow_right_down = pygame.transform.scale(
            pygame.image.load("static_files/ARD.png"), (25, 25)
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
        self.hearth_3 = pygame.image.load("static_files/life/3.png")
        self.hearth_2 = pygame.image.load("static_files/life/2.png")
        self.hearth_1 = pygame.image.load("static_files/life/1.png")
        self.game_over = pygame.image.load("static_files/game_over.png")


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
        self.right_up = False
        self.right_down = False
        self.left = False
        self.left_up = False
        self.left_down = False
        self.up = False
        self.down = False
        self.standing = True

    def redraw(self, window):
        """Draw player on window."""
        if self.walk_count + 1 >= 36:
            self.walk_count = 0

        if self.right:
            window.blit(images.walk_right[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 3
        if self.right_up:
            window.blit(images.walk_right_up[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 3
        if self.right_down:
            window.blit(images.walk_right_down[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 3

        if self.left:
            window.blit(images.walk_left[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 3
        if self.left_up:
            window.blit(images.walk_left_up[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 3
        if self.left_down:
            window.blit(images.walk_left_down[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 3

        if self.up:
            window.blit(images.walk_up[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 3

        if self.down:
            window.blit(images.walk_down[self.walk_count // 6], (self.x, self.y))
            self.walk_count += 3

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
            if direction == "left_up":
                self.x -= self.speed
                self.y -= self.speed
                window.blit(images.arrow_left_up, (self.x, self.y))
            if direction == "left_down":
                self.x -= self.speed
                self.y += self.speed
                window.blit(images.arrow_left_down, (self.x, self.y))
            if direction == "right":
                self.x += self.speed
                window.blit(images.arrow_right, (self.x, self.y))
            if direction == "right_up":
                self.x += self.speed
                self.y -= self.speed
                window.blit(images.arrow_right_up, (self.x, self.y))
            if direction == "right_down":
                self.x += self.speed
                self.y += self.speed
                window.blit(images.arrow_right_down, (self.x, self.y))
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

    def __init__(self, x, y):
        self.x = x
        self.y = y

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


class Life(object):
    """Lives and its information."""

    def __init__(self):
        self.x = 0
        self.y = 50
        self.count = 3

    def redraw(self, window):
        """Draw lives."""
        if self.count == 3:
            window.blit(images.hearth_3, (self.x, self.y))
        if self.count == 2:
            window.blit(images.hearth_2, (self.x, self.y))
        if self.count == 1:
            window.blit(images.hearth_1, (self.x, self.y))


class GameOver(object):
    """Game over text."""
    def __init__(self):
        self.x = rules.screen_wight // 2 - 250
        self.y = rules.screen_height // 2 - 100

    def redraw(self, window):
        """Draw game over."""
        window.blit(images.game_over, (self.x, self.y))


# Creating player, ammo and ammo kit
player = Player(200, 200, 64, 64)
ammo = Ammo()
ammo_kit = AmmoKit(rules.screen_wight // 2, rules.screen_height // 2)
hearth = Life()
game_over = GameOver()


def full_redraw(projectiles):
    """Redraw all objects, projectiles etc."""
    # Draw background
    rules.window.blit(images.bg, (0, 0))
    if hearth.count == 0:
        game_over.redraw(rules.window)
        survive = rules.font.render(
            f"You have survived {round(rules.score, 1)}", True, "black"
        )
        kills = rules.font.render(f"And killed {rules.kills} robbers", True, "black")
        score = rules.font.render(f"Final score: {rules.kills + round(rules.score, 1)}", True, "black")
        rules.window.blit(
            survive, (rules.screen_wight // 2 - 100, rules.screen_height // 2 + 100)
        )
        rules.window.blit(
            kills, (rules.screen_wight // 2 - 100, rules.screen_height // 2 + 120)
        )
        rules.window.blit(
            score, (rules.screen_wight // 2 - 100, rules.screen_height // 2 + 140)
        )

    elif hearth.count > 0:
        # Draw player
        player.redraw(rules.window)

        # Draw hearths
        hearth.redraw(rules.window)
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
            # Getting killed
            if (
                player.x + rules.mistake >= e.x >= player.x - rules.mistake
                and player.y + rules.mistake >= e.y >= player.y - rules.mistake
            ):
                hearth.count -= 1
                rules.enemies = []
                rules.count_projectiles = 5
            # Draw enemies
            e.redraw(rules.window)

            # Check if projectile hit enemy, remove both when hit
            for p in projectiles:
                if (e.x + rules.mistake) > p["arrow"].x > (e.x - rules.mistake) and (
                    e.y + rules.mistake
                ) > p["arrow"].y > (e.y - rules.mistake):
                    projectiles.remove(p)
                    rules.kills += 1
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
    spawn_ticker = 50
    game_over = False
    run = True

    # Main loop
    while run:
        rules.clock.tick(27)

        # Tick for ammo
        if ticker > 0:
            ticker -= 1

        # Tick for spawning enemies
        if spawn_ticker > 0:
            spawn_ticker -= 1

        # Score count
        if not game_over:
            rules.score += 0.1

        # Game quit
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
            ammo_kit.x = random.randint(
                rules.mistake, rules.screen_wight - rules.mistake * 2
            )
            ammo_kit.y = random.randint(
                rules.mistake, rules.screen_height - rules.mistake * 2
            )

        # No more lives
        if hearth.count == 0:
            game_over = True
        keys = pygame.key.get_pressed()
        k_up_rule = keys[pygame.K_UP] and player.y > 0
        k_down_rule = (
            keys[pygame.K_DOWN] and player.y < rules.screen_height - player.height
        )
        k_right_rule = (
            keys[pygame.K_RIGHT] and player.x < rules.screen_wight - player.wight
        )
        k_left_rule = keys[pygame.K_LEFT] and player.x > 0

        # Move right
        if k_right_rule and not (
            keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]
        ):
            player.x += player.speed
            player.right = True
            player.right_up = False
            player.right_down = False
            player.left = False
            player.left_up = False
            player.left_down = False
            player.up = False
            player.down = False
            player.standing = False
        # Move right up
        if (
            k_right_rule
            and k_up_rule
            and not (keys[pygame.K_DOWN] or keys[pygame.K_LEFT])
        ):
            player.x += player.speed
            player.y -= player.speed
            player.right = False
            player.right_up = True
            player.right_down = False
            player.left = False
            player.left_up = False
            player.left_down = False
            player.up = False
            player.down = False
            player.standing = False
        # Move right down
        if (
            k_right_rule
            and k_down_rule
            and not (keys[pygame.K_UP] or keys[pygame.K_LEFT])
        ):
            player.x += player.speed
            player.y += player.speed
            player.right = False
            player.right_up = False
            player.right_down = True
            player.left = False
            player.left_up = False
            player.left_down = False
            player.up = False
            player.down = False
            player.standing = False

        # Move left
        if k_left_rule and not (
            keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]
        ):
            player.x -= player.speed
            player.right = False
            player.right_up = False
            player.right_down = False
            player.left = True
            player.left_up = False
            player.left_down = False
            player.up = False
            player.down = False
            player.standing = False
        # Move left up
        if (
            k_left_rule
            and k_up_rule
            and not (keys[pygame.K_DOWN] or keys[pygame.K_RIGHT])
        ):
            player.x -= player.speed
            player.y -= player.speed
            player.right = False
            player.right_up = False
            player.right_down = False
            player.left = False
            player.left_up = True
            player.left_down = False
            player.up = False
            player.down = False
            player.standing = False
        # Move left down
        if (
            k_left_rule
            and k_down_rule
            and not (keys[pygame.K_UP] or keys[pygame.K_RIGHT])
        ):
            player.x -= player.speed
            player.y += player.speed
            player.right = False
            player.right_up = False
            player.right_down = False
            player.left = False
            player.left_up = False
            player.left_down = True
            player.up = False
            player.down = False
            player.standing = False

        # Move up
        if k_up_rule and not (
            keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_DOWN]
        ):
            player.y -= player.speed
            player.right = False
            player.right_up = False
            player.right_down = False
            player.left = False
            player.left_up = False
            player.left_down = False
            player.up = True
            player.down = False
            player.standing = False

        # Move down
        if k_down_rule and not (
            keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_UP]
        ):
            player.y += player.speed
            player.right = False
            player.right_up = False
            player.right_down = False
            player.left = False
            player.left_up = False
            player.left_down = False
            player.up = False
            player.down = True
            player.standing = False

        # Reset walk count when standing
        if not any(
            [
                keys[pygame.K_LEFT],
                keys[pygame.K_RIGHT],
                keys[pygame.K_UP],
                keys[pygame.K_DOWN],
            ]
        ):
            player.walk_count = 0

        # Fire ammo
        if (
            keys[pygame.K_SPACE]
            and not player.standing
            and ticker == 0
            and not game_over
        ):
            ticker = 10
            direction = None
            if player.right:
                direction = "right"
            if player.right_up:
                direction = "right_up"
            if player.right_down:
                direction = "right_down"
            if player.left:
                direction = "left"
            if player.left_up:
                direction = "left_up"
            if player.left_down:
                direction = "left_down"
            if player.up:
                direction = "up"
            if player.down:
                direction = "down"
            if rules.count_projectiles > 0:
                rules.count_projectiles -= 1
                rules.projectiles.append(
                    {
                        "arrow": Projectile(player.x, player.y, 20, 20),
                        "direction": direction,
                    }
                )

        # Spawn enemy
        if spawn_ticker == 0 and not game_over:
            # Make sure enemy won't spawn too close to player
            x = random.randint(rules.mistake, rules.screen_wight - rules.mistake)
            y = random.randint(rules.mistake, rules.screen_height - rules.mistake)
            if not (
                player.x + rules.mistake**2 >= x >= player.x + rules.mistake * 2
            ) and not (
                player.y + rules.mistake * 2 >= y >= player.y + rules.mistake * 2
            ):
                x += rules.mistake * 4
                y += rules.mistake * 4
            enemy = Enemy(
                x,
                y,
                64,
                64,
                random.uniform(1, 2),
            )
            rules.enemies.append(enemy)
            spawn_ticker = 20

        full_redraw(rules.projectiles)
