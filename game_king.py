import random
import pygame
from pygame.locals import *
from game_data import Images, Rules, check_direction, arrow_shot

pygame.init()

# Adding joystick
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

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
        self.move = False

    def count_steps(self, window, x):
        window.blit(images.walk[f"{x}"][self.walk_count // 6], (self.x, self.y))
        if self.move or not joysticks:
            self.walk_count += 3

    def redraw(self, window):
        """Draw player on window."""
        if self.walk_count + 1 >= 36:
            self.walk_count = 0

        if self.right:
            self.count_steps(window, "right")
        if self.right_up:
            self.count_steps(window, "right_up")
        if self.right_down:
            self.count_steps(window, "right_down")

        if self.left:
            self.count_steps(window, "left")
        if self.left_up:
            self.count_steps(window, "left_up")
        if self.left_down:
            self.count_steps(window, "left_down")

        if self.up:
            self.count_steps(window, "up")

        if self.down:
            self.count_steps(window, "down")

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
        self.roll = 0

    def redraw(self, window, direction):
        """Draw projectile."""
        if rules.explosive_ammo == 0:
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
        if rules.explosive_ammo > 0:
            if 0 < self.x < rules.screen_wight and 0 < self.y < rules.screen_height:
                if self.roll + 1 >= 8:
                    self.roll = 0
                if direction == "left":
                    self.x -= self.speed / 2
                    window.blit(images.bomb[self.roll // 2], (self.x, self.y))
                    self.roll += 1
                if direction == "left_up":
                    self.x -= self.speed / 2
                    self.y -= self.speed / 2
                    window.blit(images.bomb[self.roll // 2], (self.x, self.y))
                    self.roll += 1
                if direction == "left_down":
                    self.x -= self.speed / 2
                    self.y += self.speed / 2
                    window.blit(images.bomb[self.roll // 2], (self.x, self.y))
                    self.roll += 1
                if direction == "right":
                    self.x += self.speed / 2
                    window.blit(images.bomb[self.roll // 2], (self.x, self.y))
                    self.roll += 1
                if direction == "right_up":
                    self.x += self.speed / 2
                    self.y -= self.speed / 2
                    window.blit(images.bomb[self.roll // 2], (self.x, self.y))
                    self.roll += 1
                if direction == "right_down":
                    self.x += self.speed / 2
                    self.y += self.speed / 2
                    window.blit(images.bomb[self.roll // 2], (self.x, self.y))
                    self.roll += 1
                if direction == "up":
                    self.y -= self.speed / 2
                    window.blit(images.bomb[self.roll // 2], (self.x, self.y))
                    self.roll += 1
                if direction == "down":
                    self.y += self.speed / 2
                    window.blit(images.bomb[self.roll // 2], (self.x, self.y))
                    self.roll += 1


class Tornado(object):
    """Tornado and all its information."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 20
        self.range = 400
        self.spin_count = 0

    def redraw(self, window, direction):
        """Draw tornado."""
        if self.spin_count + 1 >= 4:
            self.spin_count = 0
        if self.range > 0:
            if direction == "left":
                self.x -= self.speed
                self.range -= self.speed
                window.blit(images.tornado[self.spin_count // 2], (self.x, self.y))
                self.spin_count += 1
            if direction == "left_up":
                self.x -= self.speed
                self.y -= self.speed
                self.range -= self.speed
                window.blit(images.tornado[self.spin_count // 2], (self.x, self.y))
                self.spin_count += 1
            if direction == "left_down":
                self.x -= self.speed
                self.y += self.speed
                self.range -= self.speed
                window.blit(images.tornado[self.spin_count // 2], (self.x, self.y))
                self.spin_count += 1
            if direction == "right":
                self.x += self.speed
                self.range -= self.speed
                window.blit(images.tornado[self.spin_count // 2], (self.x, self.y))
                self.spin_count += 1
            if direction == "right_up":
                self.x += self.speed
                self.y -= self.speed
                window.blit(images.tornado[self.spin_count // 2], (self.x, self.y))
                self.spin_count += 1
            if direction == "right_down":
                self.x += self.speed
                self.y += self.speed
                self.range -= self.speed
                window.blit(images.tornado[self.spin_count // 2], (self.x, self.y))
                self.spin_count += 1
            if direction == "up":
                self.y -= self.speed
                self.range -= self.speed
                window.blit(images.tornado[self.spin_count // 2], (self.x, self.y))
                self.spin_count += 1
            if direction == "down":
                self.y += self.speed
                self.range -= self.speed
                window.blit(images.tornado[self.spin_count // 2], (self.x, self.y))
                self.spin_count += 1
        else:
            rules.tornados = []


class Explosion(object):
    """Explosion and all its information."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wight = 100
        self.height = 100
        self.animation = 17

    def redraw(self, window):
        """Draw explosion."""
        if self.animation in [17, 16]:
            window.blit(images.explosion1, (self.x, self.y))
        if self.animation in [15, 14]:
            window.blit(images.explosion2, (self.x, self.y))
        if self.animation in [13, 12]:
            window.blit(images.explosion3, (self.x, self.y))
        if self.animation in [11, 10]:
            window.blit(images.explosion4, (self.x, self.y))
        if self.animation in [9, 8]:
            window.blit(images.explosion5, (self.x, self.y))
        if self.animation in [7, 6]:
            window.blit(images.explosion6, (self.x, self.y))
        if self.animation in [5, 4]:
            window.blit(images.explosion7, (self.x, self.y))
        if self.animation in [3, 2]:
            window.blit(images.explosion8, (self.x, self.y))
        if self.animation in [1, 0]:
            window.blit(images.explosion9, (self.x, self.y))


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
        if rules.enemy_frozen_ticker == 0:
            window.blit(images.enemy, (self.x, self.y))
        else:
            window.blit(images.enemy_frozen, (self.x, self.y))


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
player2 = Player(200, 200, 64, 64)
ammo_kit = AmmoKit(rules.screen_wight // 2, rules.screen_height // 2)
hearth = Life()
game_over = GameOver()
explosions = []


def menu_redraw():
    run = True

    # Choose game type
    single = rules.font_big.render(
        f"Single", True, "black")
    double = rules.font_big.render(
        f"Double", True, "black")
    rules.window.blit(images.bg, (0, 0))

    while run:
        pygame.time.Clock().tick(27)
        question_2_player = rules.font_big.render(
            f"Do you want to play single player or multi player?", True, "black")
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    single = rules.font_big.render(
                        f"Single", True, "white")
                    double = rules.font_big.render(
                        f"Double", True, "black")
                    print(event)
                if event.key == pygame.K_RIGHT:
                    single = rules.font_big.render(
                        f"Single", True, "black")
                    double = rules.font_big.render(
                        f"Double", True, "white")
                    print(event)

                if event.key == pygame.K_SPACE:
                    run = False
                    print(event)

        rules.window.blit(
            question_2_player, (rules.screen_wight // 2 - 500, rules.screen_height // 2 - 100)
        )
        rules.window.blit(
            single, (rules.screen_wight // 2 - 300, rules.screen_height // 2 + 100)
        )
        rules.window.blit(
            double, (rules.screen_wight // 2 + 100, rules.screen_height // 2 + 100)
        )
        pygame.display.update()


def full_redraw(projectiles, tornados):
    """Redraw all objects, projectiles etc."""
    # Draw background
    rules.window.blit(images.bg, (0, 0))
    level = rules.font_big.render(f"Level - {rules.level}", True, "black")
    rules.window.blit(level, (rules.screen_wight // 2, 10))
    # End game
    if hearth.count == 0:
        game_over.redraw(rules.window)
        survive = rules.font.render(
            f"You have survived {round(rules.score, 1)}", True, "black"
        )
        kills = rules.font.render(f"And killed {rules.kills} robbers", True, "black")
        score = rules.font.render(
            f"Final score: {rules.kills + round(rules.score, 1)}", True, "black"
        )
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

        # Cooldown skill draw
        cooldown_tornado = rules.font.render(f"{rules.tornado_ticker}", True, (0, 0, 0))
        cooldown_snow = rules.font.render(f"{rules.freeze_ticker}", True, (0, 0, 0))
        cooldown_explosion = rules.font.render(
            f"{rules.explosive_ammo_ticker}", True, (0, 0, 0)
        )
        if rules.tornado_ticker == 0:
            rules.window.blit(images.tornado_small, (rules.screen_wight - 50, 50))
        else:
            rules.window.blit(images.tornado_bw, (rules.screen_wight - 50, 50))
        rules.window.blit(cooldown_tornado, (rules.screen_wight - 50, 100))
        if rules.freeze_ticker == 0:
            rules.window.blit(images.snow, (rules.screen_wight - 50, 150))
        else:
            rules.window.blit(images.snow_bw, (rules.screen_wight - 50, 150))
        rules.window.blit(cooldown_snow, (rules.screen_wight - 50, 200))
        if rules.explosive_ammo_ticker == 0:
            rules.window.blit(images.explosion_small, (rules.screen_wight - 50, 250))
        else:
            rules.window.blit(images.explosion_bw, (rules.screen_wight - 50, 250))
        rules.window.blit(cooldown_explosion, (rules.screen_wight - 50, 300))

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

        # Loop for tornado
        for t in tornados:

            t["tornado"].redraw(rules.window, t["direction"])
            if (
                0 >= t["tornado"].x >= rules.screen_wight
                or 0 >= t["tornado"].y >= rules.screen_height
            ):
                tornados.remove(t)

        # Loop for changing enemies positions
        for e in rules.enemies:

            # Move when not frozen
            if rules.enemy_frozen_ticker == 0:
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

            # Getting killed
            if (
                player.x + rules.mistake >= e.x >= player.x - rules.mistake
                and player.y + rules.mistake >= e.y >= player.y - rules.mistake
            ) and rules.enemy_frozen_ticker == 0:
                hearth.count -= 1
                rules.enemies = []
                rules.max_ammo += 5
                rules.count_projectiles = rules.max_ammo
                rules.explosive_ammo = 0
                rules.zombie_spawn = 0
                rules.level = 1

            # Check if projectile hit enemy, remove both when hit
            for p in projectiles:
                if (e.x + rules.mistake) > p["arrow"].x > (e.x - rules.mistake) and (
                    e.y + rules.mistake
                ) > p["arrow"].y > (e.y - rules.mistake):

                    rules.kills += 1
                    # Sometimes if two projectiles hit one enemy it tried to remove same enemy twice
                    if rules.explosive_ammo == 0:
                        projectiles.remove(p)
                        try:
                            rules.enemies.remove(e)
                        except ValueError:
                            print("Same enemy hit twice")
                    if rules.explosive_ammo > 0:
                        explosion = Explosion(p["arrow"].x - 50, p["arrow"].y - 50)
                        explosions.append(explosion)
                        projectiles.remove(p)

            for explode in explosions:
                if (e.x + rules.mistake) > explode.x > (
                    e.x - (rules.mistake + 200)
                ) and (e.y + rules.mistake) > explode.y > (e.y - (rules.mistake + 200)):
                    try:
                        rules.enemies.remove(e)
                    except ValueError:
                        print("Same enemy hit twice")
            # Check if tornado hits enemy
            for t in tornados:
                if (e.x + rules.mistake * 2) > t["tornado"].x > (
                    e.x - rules.mistake * 2
                ) and (e.y + rules.mistake * 2) > t["tornado"].y > (
                    e.y - rules.mistake * 2
                ):
                    try:
                        rules.enemies.remove(e)
                    except ValueError:
                        print("Same enemy hit twice")

        # Draw explosions
        for explode in explosions:
            if explode.animation >= 2:
                explode.redraw(rules.window)
                explode.animation -= 1
            if explode.animation < 2:
                explosions.remove(explode)

        # Draw ammo and ammo kit
        ammo_kit.redraw(rules.window)
        ammo_text = rules.font_big.render(
            f"{rules.count_projectiles} / {rules.max_ammo}", True, (0, 0, 0)
        )
        rules.window.blit(
            ammo_text, (rules.screen_wight - 200, rules.screen_height - 100)
        )
        # Draw player
        player.redraw(rules.window)

    # Update window
    pygame.display.update()


def start_game():
    """Start game"""
    first_upgrade = False
    second_upgrade = False
    rules.arrow_ticker = 0
    run = True

    menu_redraw()

    # Main loop
    while run:
        rules.clock.tick(27)

        # Ticks
        if rules.arrow_ticker > 0:
            rules.arrow_ticker -= 1
        if rules.spawn_ticker > 0:
            rules.spawn_ticker -= 1
        if rules.tornado_ticker > 0:
            rules.tornado_ticker -= 1
        if rules.freeze_ticker > 0:
            rules.freeze_ticker -= 1
        if rules.enemy_frozen_ticker > 0:
            rules.enemy_frozen_ticker -= 1
        if rules.explosive_ammo_ticker > 0:
            rules.explosive_ammo_ticker -= 1
        rules.zombie_spawn += 0.1

        # Score count
        if not rules.game_over:
            rules.score += 0.1

        # Upgrade ammo
        if rules.kills == 50 and not first_upgrade:
            rules.max_ammo += 5
            first_upgrade = True
        if rules.kills == 100 and not second_upgrade:
            rules.max_ammo += 5
            second_upgrade = True

        # Game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if joysticks:
                if event.type == JOYBUTTONUP:
                    if (
                        event.button == 0
                        and rules.tornado_ticker == 0
                        and not player.standing
                    ):
                        tornado = Tornado(player.x, player.y)
                        direction = check_direction(player)
                        rules.tornados.append(
                            {
                                "tornado": tornado,
                                "direction": direction,
                            }
                        )
                        rules.tornado_ticker = 1000
                    if (
                        event.button == 1
                        and rules.freeze_ticker == 0
                        and not player.standing
                    ):
                        rules.enemy_frozen_ticker = 125
                        rules.freeze_ticker = 3000
                    if (
                        event.button == 2
                        and rules.explosive_ammo_ticker == 0
                        and not player.standing
                    ):
                        rules.explosive_ammo = rules.max_ammo + 1
                        rules.explosive_ammo_ticker = 5000
                        rules.count_projectiles = rules.max_ammo
                    if (
                        event.button == 5
                        and not player.standing
                        and rules.arrow_ticker == 0
                        and not rules.game_over
                    ):
                        arrow_shot(player, rules, Projectile)
                if event.type == JOYHATMOTION:
                    # Right
                    if event.value == (1, 0):
                        player.right = True
                        player.right_up = False
                        player.right_down = False
                        player.left = False
                        player.left_up = False
                        player.left_down = False
                        player.up = False
                        player.down = False
                        player.standing = False
                        player.move = True
                        # Left
                    if event.value == (-1, 0):
                        player.right = False
                        player.right_up = False
                        player.right_down = False
                        player.left = True
                        player.left_up = False
                        player.left_down = False
                        player.up = False
                        player.down = False
                        player.standing = False
                        player.move = True
                        # Down
                    if event.value == (0, -1):
                        player.right = False
                        player.right_up = False
                        player.right_down = False
                        player.left = False
                        player.left_up = False
                        player.left_down = False
                        player.up = False
                        player.down = True
                        player.standing = False
                        player.move = True
                    # Up
                    if event.value == (0, 1):
                        player.right = False
                        player.right_up = False
                        player.right_down = False
                        player.left = False
                        player.left_up = False
                        player.left_down = False
                        player.up = True
                        player.down = False
                        player.standing = False
                        player.move = True
                    # Right-down
                    if event.value == (1, -1):
                        player.right = False
                        player.right_up = False
                        player.right_down = True
                        player.left = False
                        player.left_up = False
                        player.left_down = False
                        player.up = False
                        player.down = False
                        player.standing = False
                        player.move = True
                    # Right-up
                    if event.value == (1, 1):
                        player.right = False
                        player.right_up = True
                        player.right_down = False
                        player.left = False
                        player.left_up = False
                        player.left_down = False
                        player.up = False
                        player.down = False
                        player.standing = False
                        player.move = True
                    # Left-down
                    if event.value == (-1, -1):
                        player.right = False
                        player.right_up = False
                        player.right_down = False
                        player.left = False
                        player.left_up = False
                        player.left_down = True
                        player.up = False
                        player.down = False
                        player.standing = False
                        player.move = True
                    # Left-up
                    if event.value == (-1, 1):
                        player.right = False
                        player.right_up = False
                        player.right_down = False
                        player.left = False
                        player.left_up = True
                        player.left_down = False
                        player.up = False
                        player.down = False
                        player.standing = False
                        player.move = True
                    if event.value == (0, 0):
                        player.move = False
        # Movements
        if player.move:
            if player.right and player.x < rules.screen_wight - player.wight:
                player.x += player.speed
            if (
                player.right_up
                and player.x < rules.screen_wight - player.wight
                and player.y > 0
            ):
                player.x += player.speed
                player.y -= player.speed
            if (
                player.right_down
                and player.x < rules.screen_wight - player.wight
                and player.y < rules.screen_height - player.height
            ):
                player.x += player.speed
                player.y += player.speed
            if player.left and player.x > 0:
                player.x -= player.speed
            if player.left_up and player.x > 0 and player.y > 0:
                player.x -= player.speed
                player.y -= player.speed
            if (
                player.left_down
                and player.x > 0
                and player.y < rules.screen_height - player.height
            ):
                player.x -= player.speed
                player.y += player.speed
            if player.up and player.y > 0:
                player.y -= player.speed
            if player.down and player.y < rules.screen_height - player.height:
                player.y += player.speed

        # Collecting ammo kit
        if (ammo_kit.x + rules.mistake // 2) >= player.x >= (
            ammo_kit.x - rules.mistake * 2
        ) and (ammo_kit.y + rules.mistake // 2) >= player.y >= (
            ammo_kit.y - rules.mistake * 2
        ):
            rules.count_projectiles = rules.max_ammo
            ammo_kit.x = random.randint(
                rules.mistake, rules.screen_wight - rules.mistake * 2
            )
            ammo_kit.y = random.randint(
                rules.mistake, rules.screen_height - rules.mistake * 2
            )

        # No more lives
        if hearth.count == 0:
            rules.game_over = True
        keys = pygame.key.get_pressed()
        k_up_rule = keys[pygame.K_UP] and player.y > 0
        k_down_rule = (
            keys[pygame.K_DOWN] and player.y < rules.screen_height - player.height
        )
        k_right_rule = (
            keys[pygame.K_RIGHT] and player.x < rules.screen_wight - player.wight
        )
        k_left_rule = keys[pygame.K_LEFT] and player.x > 0
        if not joysticks:
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
                and rules.arrow_ticker == 0
                and not rules.game_over
            ):
                arrow_shot(player, rules, Projectile)

            # Tornado skill
            if (keys[pygame.K_q]) and rules.tornado_ticker == 0 and not player.standing:
                tornado = Tornado(player.x, player.y)
                direction = check_direction(player)
                rules.tornados.append(
                    {
                        "tornado": tornado,
                        "direction": direction,
                    }
                )
                rules.tornado_ticker = 1000

            # Freeze skill
            if (keys[pygame.K_w]) and rules.freeze_ticker == 0 and not player.standing:
                rules.enemy_frozen_ticker = 125
                rules.freeze_ticker = 3000

            # Explosive arrow skill
            if (
                (keys[pygame.K_e])
                and rules.explosive_ammo_ticker == 0
                and not player.standing
            ):
                rules.explosive_ammo = rules.max_ammo + 1
                rules.explosive_ammo_ticker = 5000
                rules.count_projectiles = rules.max_ammo

        # Spawn enemy
        if (
            rules.spawn_ticker == 0
            and not rules.game_over
            and rules.enemy_frozen_ticker == 0
            and len(rules.enemies) < 61
        ):
            # Make sure enemy won't spawn too close to player
            x = random.randint(rules.mistake, rules.screen_wight - rules.mistake)
            y = random.randint(rules.mistake, rules.screen_height - rules.mistake)
            if (player.x + rules.mistake * 3 >= x >= player.x - rules.mistake * 3) and (
                player.y + rules.mistake * 3 >= y >= player.y - rules.mistake * 3
            ):
                if player.x > 600:
                    x -= rules.mistake * 8
                if player.x < 600:
                    x += rules.mistake * 8
            enemy = Enemy(
                x,
                y,
                64,
                64,
                random.uniform(1, 2),
            )
            rules.enemies.append(enemy)
            if rules.zombie_spawn < 150:
                rules.spawn_ticker = 20
            if 300 > rules.zombie_spawn > 150:
                rules.spawn_ticker = 15
                rules.level = 2
            if (450 > rules.zombie_spawn > 300) and hearth.count <= 2:
                rules.spawn_ticker = 10
                rules.level = 3

        full_redraw(rules.projectiles, rules.tornados)
