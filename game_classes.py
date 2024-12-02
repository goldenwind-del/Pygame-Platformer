import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, screen_width, screen_height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.velocity_x = 5
        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = -20
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.is_on_ground = False

    def move(self, keys, platforms, walls):
        # Horizontal movement with boundary checks
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= self.velocity_x
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < self.screen_width:
            self.rect.x += self.velocity_x

        for platform in platforms:
            if self.rect.colliderect(platform.rect) and not (keys[pygame.K_DOWN] or keys[pygame.K_s]):
                if self.rect.right > platform.rect.left and self.rect.left <platform.rect.centerx and self.rect.left > 0:
                    self.rect.right = platform.rect.left
                elif self.rect.left < platform.rect.right and self.rect.right > platform.rect.centerx and self.rect.right < self.screen_width:
                    self.rect.left = platform.rect.right
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.rect.right > wall.rect.left and self.rect.left < wall.rect.centerx:
                    self.rect.right = wall.rect.left
                elif self.rect.left < wall.rect.right and self.rect.right > wall.rect.centerx:
                    self.rect.left = wall.rect.right

        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Reset ground state
        self.is_on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform.rect) and not (keys[pygame.K_DOWN] or keys[pygame.K_s]):
                if self.velocity_y > 0 and self.rect.bottom <= platform.rect.bottom:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.is_on_ground = True
                

                elif self.velocity_y < 0 and self.rect.top >= platform.rect.top:
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.velocity_y > 0 and self.rect.bottom <= wall.rect.bottom:
                    self.rect.bottom = wall.rect.top
                    self.velocity_y = 0
                    self.is_on_ground = True
                

                elif self.velocity_y < 0 and self.rect.top >= wall.rect.top:
                    self.rect.top = wall.rect.bottom
                    self.velocity_y = 0            

        if self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height
            self.velocity_y = 0
            self.is_on_ground = True

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.is_on_ground:
            self.velocity_y = self.jump_strength

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.rect = pygame.Rect(x, y,width,height)
        self.color = color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.rect = pygame.Rect(x, y,width,height)
        self.color = color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
