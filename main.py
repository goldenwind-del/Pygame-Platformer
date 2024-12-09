import sys,pygame,game_classes,level_data

# Core Elements and variables
pygame.init()
width, height = 960, 540
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
game_active = True

font = pygame.font.Font(None, 50)

player = game_classes.Player(0, 490, 25, 25, (255, 0, 0),width, height)

current_level = 1
current_level_data = level_data.levels[current_level]

platforms = [game_classes.Platform(*data) for data in current_level_data["platforms"]]
walls = [game_classes.Wall(*data) for data in current_level_data["walls"]]
finnish = game_classes.Finnish(*current_level_data["finnish"][0])
player = game_classes.Player(*current_level_data["player"][0])
all_sprites = pygame.sprite.Group()
all_sprites.add(finnish, platforms, walls, player)


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

    if player.rect.colliderect(finnish.rect):
                
        if current_level >= len(level_data.levels):
            finnish_message = font.render(f"You beat level {current_level}, press enter to move onto the next level", True, 'white', None)
            finnish_rect = finnish_message.get_rect(center=(480, 270))
            screen.blit(finnish_message, finnish_rect)
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                current_level += 1
                current_level_data = level_data.level_gen()
                platforms = [game_classes.Platform(*data) for data in current_level_data["platforms"]]
                walls = [game_classes.Wall(*data) for data in current_level_data["walls"]]
                finnish = game_classes.Finnish(*current_level_data["finnish"][0])
                player = game_classes.Player(*current_level_data["player"][0])
                all_sprites.empty()
                all_sprites.add(finnish, *platforms, *walls, player)
            

        elif current_level < len(level_data.levels):
            finnish_message = font.render(f"You beat level {current_level}, press enter to move onto the next level", True, 'white', None)
            finnish_rect = finnish_message.get_rect(center=(480, 270))
            screen.blit(finnish_message, finnish_rect)
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                current_level += 1
                current_level_data = level_data.levels[current_level]
                platforms = [game_classes.Platform(*data) for data in current_level_data["platforms"]]
                walls = [game_classes.Wall(*data) for data in current_level_data["walls"]]
                finnish = game_classes.Finnish(*current_level_data["finnish"][0])
                player = game_classes.Player(*current_level_data["player"][0])
                all_sprites.empty()
                all_sprites.add(finnish, *platforms, *walls, player)


    pygame.display.flip()
    clock.tick(60)
    



    