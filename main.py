import sys, random, time
import pygame
import game_classes


# Core Elements and variables
pygame.init()
width, height = 960, 540
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
game_active = True

player = game_classes.Player(0, 490, 25, 25, (255, 0, 0),width, height)
platforms = [
        game_classes.Platform(850, 200, 120, 20, (0, 255, 0)),
    game_classes.Platform(525, 200, 100, 20, (0, 255, 0)),
    game_classes.Platform(325, 300, 100, 20, (0, 255, 0)),
    game_classes.Platform(125, 400, 100, 20, (0, 255, 0)),
]
walls = [
    game_classes.Wall(800,200,50, 400, (0, 0, 255)),
]

all_sprites = pygame.sprite.Group()
all_sprites.add(player, platforms, walls)

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()
    player.move(keys, platforms,walls)
    screen.fill((0,0,0))


    for sprite in all_sprites:
        sprite.draw(screen)

    pygame.display.flip()
    clock.tick(60)
    



    