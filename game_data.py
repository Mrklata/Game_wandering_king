import pygame


class Rules:
    """General information about the game."""

    def __init__(self):
        self.arrow_ticker = 10
        self.clock = pygame.time.Clock()
        self.screen_wight = 1600
        self.screen_height = 900
        self.window = pygame.display.set_mode((self.screen_wight, self.screen_height))
        self.enemies = []
        self.projectiles = []
        self.tornados = []
        self.tornado_ticker = 0
        self.freeze_ticker = 0
        self.max_ammo = 5
        self.count_projectiles = 5
        self.mistake = 32
        self.score = 0.0
        self.kills = 0
        self.font = pygame.font.SysFont("Times New Roman", 18)
        self.font_big = pygame.font.SysFont("Times New Roman", 50)
        self.spawn_ticker = 50
        self.enemy_frozen_ticker = 0
        self.explosive_ammo = 0
        self.explosive_ammo_ticker = 0
        self.zombie_spawn = 0
        self.level = 1
        self.game_over = False


class Images:
    """All images."""

    def __init__(self):
        self.walk = {
            "left": [
                pygame.image.load("static_files/walk_left/1.png"),
                pygame.image.load("static_files/walk_left/2.png"),
                pygame.image.load("static_files/walk_left/3.png"),
                pygame.image.load("static_files/walk_left/4.png"),
                pygame.image.load("static_files/walk_left/5.png"),
                pygame.image.load("static_files/walk_left/6.png"),
            ],
            "left_up": [
                pygame.image.load("static_files/walk_left_up/1.png"),
                pygame.image.load("static_files/walk_left_up/2.png"),
                pygame.image.load("static_files/walk_left_up/3.png"),
                pygame.image.load("static_files/walk_left_up/4.png"),
                pygame.image.load("static_files/walk_left_up/5.png"),
                pygame.image.load("static_files/walk_left_up/6.png"),
            ],
            "left_down": [
                pygame.image.load("static_files/walk_left_down/1.png"),
                pygame.image.load("static_files/walk_left_down/2.png"),
                pygame.image.load("static_files/walk_left_down/3.png"),
                pygame.image.load("static_files/walk_left_down/4.png"),
                pygame.image.load("static_files/walk_left_down/5.png"),
                pygame.image.load("static_files/walk_left_down/6.png"),
            ],
            "right": [
                pygame.image.load("static_files/walk_right/1.png"),
                pygame.image.load("static_files/walk_right/2.png"),
                pygame.image.load("static_files/walk_right/3.png"),
                pygame.image.load("static_files/walk_right/4.png"),
                pygame.image.load("static_files/walk_right/5.png"),
                pygame.image.load("static_files/walk_right/6.png"),
            ],
            "right_up": [
                pygame.image.load("static_files/walk_right_up/1.png"),
                pygame.image.load("static_files/walk_right_up/2.png"),
                pygame.image.load("static_files/walk_right_up/3.png"),
                pygame.image.load("static_files/walk_right_up/4.png"),
                pygame.image.load("static_files/walk_right_up/5.png"),
                pygame.image.load("static_files/walk_right_up/6.png"),
            ],
            "right_down": [
                pygame.image.load("static_files/walk_right_down/1.png"),
                pygame.image.load("static_files/walk_right_down/2.png"),
                pygame.image.load("static_files/walk_right_down/3.png"),
                pygame.image.load("static_files/walk_right_down/4.png"),
                pygame.image.load("static_files/walk_right_down/5.png"),
                pygame.image.load("static_files/walk_right_down/6.png"),
            ],
            "up": [
                pygame.image.load("static_files/walk_up/1.png"),
                pygame.image.load("static_files/walk_up/2.png"),
                pygame.image.load("static_files/walk_up/3.png"),
                pygame.image.load("static_files/walk_up/4.png"),
                pygame.image.load("static_files/walk_up/5.png"),
                pygame.image.load("static_files/walk_up/6.png"),
            ],
            "down": [
                pygame.image.load("static_files/walk_down/1.png"),
                pygame.image.load("static_files/walk_down/2.png"),
                pygame.image.load("static_files/walk_down/3.png"),
                pygame.image.load("static_files/walk_down/4.png"),
                pygame.image.load("static_files/walk_down/5.png"),
                pygame.image.load("static_files/walk_down/6.png"),
            ],
        }
        self.standing = pygame.image.load("static_files/walk_down/1.png")
        self.bg = pygame.image.load("static_files/bg_pro.png")
        self.arrow_left = pygame.transform.scale(
            pygame.image.load("static_files/arrow/AL.png"), (50, 50)
        )
        self.arrow_left_up = pygame.transform.scale(
            pygame.image.load("static_files/arrow/ALU.png"), (25, 25)
        )
        self.arrow_left_down = pygame.transform.scale(
            pygame.image.load("static_files/arrow/ALD.png"), (25, 25)
        )
        self.arrow_right = pygame.transform.scale(
            pygame.image.load("static_files/arrow/AR.png"), (50, 50)
        )
        self.arrow_right_up = pygame.transform.scale(
            pygame.image.load("static_files/arrow/ARU.png"), (25, 25)
        )
        self.arrow_right_down = pygame.transform.scale(
            pygame.image.load("static_files/arrow/ARD.png"), (25, 25)
        )
        self.arrow_up = pygame.transform.scale(
            pygame.image.load("static_files/arrow/AU.png"), (50, 50)
        )
        self.arrow_down = pygame.transform.scale(
            pygame.image.load("static_files/arrow/AD.png"), (50, 50)
        )
        self.ammo_kit = pygame.transform.scale(
            pygame.image.load("static_files/ammokit.png"), (40, 40)
        )
        self.enemy = pygame.transform.scale(
            pygame.image.load("static_files/enemy.png"), (64, 64)
        )
        self.enemy_frozen = pygame.transform.scale(
            pygame.image.load("static_files/enemy_frozen.png"), (64, 64)
        )
        self.hearth_3 = pygame.image.load("static_files/life/3.png")
        self.hearth_2 = pygame.image.load("static_files/life/2.png")
        self.hearth_1 = pygame.image.load("static_files/life/1.png")
        self.game_over = pygame.image.load("static_files/game_over.png")
        self.boomerang1 = pygame.transform.scale(
            pygame.image.load("static_files/boomerang/1.png"), (50, 50)
        )
        self.boomerang2 = pygame.transform.scale(
            pygame.image.load("static_files/boomerang/2.png"), (50, 50)
        )
        self.boomerang3 = pygame.transform.scale(
            pygame.image.load("static_files/boomerang/3.png"), (50, 50)
        )
        self.boomerang4 = pygame.transform.scale(
            pygame.image.load("static_files/boomerang/4.png"), (50, 50)
        )
        self.tornado = [
            pygame.transform.scale(
                pygame.image.load("static_files/tornado/1.png"), (80, 80)
            ),
            pygame.transform.scale(
                pygame.image.load("static_files/tornado/2.png"), (80, 80)
            ),
        ]
        self.tornado_small = pygame.transform.scale(
            pygame.image.load("static_files/tornado/1.png"), (50, 50)
        )
        self.tornado_bw = pygame.transform.scale(
            pygame.image.load("static_files/tornado/bw.png"), (50, 50)
        )
        self.snow = pygame.transform.scale(
            pygame.image.load("static_files/snow/1.png"), (50, 50)
        )
        self.snow_bw = pygame.transform.scale(
            pygame.image.load("static_files/snow/bw.png"), (50, 50)
        )
        self.explosion_small = pygame.transform.scale(
            pygame.image.load("static_files/explosion/1.png"), (50, 50)
        )
        self.explosion1 = pygame.transform.scale(
            pygame.image.load("static_files/explosion/1.png"), (200, 200)
        )
        self.explosion2 = pygame.transform.scale(
            pygame.image.load("static_files/explosion/2.png"), (200, 200)
        )
        self.explosion3 = pygame.transform.scale(
            pygame.image.load("static_files/explosion/3.png"), (200, 200)
        )
        self.explosion4 = pygame.transform.scale(
            pygame.image.load("static_files/explosion/4.png"), (200, 200)
        )
        self.explosion5 = pygame.transform.scale(
            pygame.image.load("static_files/explosion/5.png"), (200, 200)
        )
        self.explosion6 = pygame.transform.scale(
            pygame.image.load("static_files/explosion/6.png"), (200, 200)
        )
        self.explosion7 = pygame.transform.scale(
            pygame.image.load("static_files/explosion/7.png"), (200, 200)
        )
        self.explosion8 = pygame.transform.scale(
            pygame.image.load("static_files/explosion/8.png"), (200, 200)
        )
        self.explosion9 = pygame.transform.scale(
            pygame.image.load("static_files/explosion/9.png"), (200, 200)
        )
        self.bomb = [
            pygame.transform.scale(
                pygame.image.load("static_files/bomb/1.png"), (50, 50)
            ),
            pygame.transform.scale(
                pygame.image.load("static_files/bomb/2.png"), (50, 50)
            ),
            pygame.transform.scale(
                pygame.image.load("static_files/bomb/3.png"), (50, 50)
            ),
            pygame.transform.scale(
                pygame.image.load("static_files/bomb/4.png"), (50, 50)
            ),
        ]
        self.explosion_bw = pygame.transform.scale(
            pygame.image.load("static_files/explosion/bw.png"), (50, 50)
        )


def check_direction(player):
    if player.right:
        return "right"
    if player.right_up:
        return "right_up"
    if player.right_down:
        return "right_down"
    if player.left:
        return "left"
    if player.left_up:
        return "left_up"
    if player.left_down:
        return "left_down"
    if player.up:
        return "up"
    if player.down:
        return "down"
    else:
        return None


def arrow_shot(player, rules, projectile):
    rules.arrow_ticker = 10
    direction = check_direction(player)
    if rules.count_projectiles > 0:
        rules.count_projectiles -= 1
        rules.projectiles.append(
            {
                "arrow": projectile(player.x, player.y, 20, 20),
                "direction": direction,
            }
        )
    if rules.explosive_ammo > 0:
        rules.explosive_ammo -= 1