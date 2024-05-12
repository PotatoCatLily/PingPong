import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from pygame.sprite import Group
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super(Paddle, self).__init__()
        self.surf = pygame.Surface((17, 200))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(25, 0)
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((36, 36))
        self.surf.fill((0, 0, 0))
        pygame.draw.circle(self.surf, (0, 255, 0), (18, 18), 18)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.speedx = 1
        self.speedy = 0
    def update(self):
        self.rect.move_ip(-self.speedx, self.speedy)
        if self.rect.top < 0:
            self.speedy = 1
        if self.rect.bottom > SCREEN_HEIGHT:
            self.speedy = -1
class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((17, SCREEN_HEIGHT))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(SCREEN_WIDTH - 17, 0)
class Diewall(pygame.sprite.Sprite):
    def __init__(self):
        super(Diewall, self).__init__()
        self.surf = pygame.Surface((17, SCREEN_HEIGHT))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(0, 0)
diewall = Diewall()
wall = Wall()
ball = Ball()
paddle = Paddle()
ball_group = pygame.sprite.GroupSingle()
ball_group.add(ball)
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle)
all_sprites.add(ball)
all_sprites.add(wall)
all_sprites.add(diewall)
Paddlepoints = 0
font = pygame.font.Font('freesansbold.ttf', 30)
text = font.render("Player's Points: " + str(Paddlepoints), True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (600, 15)
 
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            if event.key == K_ESCAPE:
                 running = False
    pressed_keys = pygame.key.get_pressed()
    paddle.update(pressed_keys)
    ball.update()
    screen.fill((0, 0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    screen.blit(text, textRect)
    if pygame.sprite.spritecollideany(paddle, ball_group):
        ball.speedx = -1 * ball.speedx
        ball.speedy = random.randint(-1, 1)
        Paddlepoints += 1
        text = font.render("Player's Points: " + str(Paddlepoints), True, (255, 255, 255))
    if pygame.sprite.spritecollideany(wall, ball_group):
        ball.speedx = -1 * ball.speedx
        ball.speedy = random.randint(-1, 1)
        text = font.render("Player's Points: " + str(Paddlepoints), True, (255, 255, 255))
    if pygame.sprite.spritecollideany(diewall, ball_group):  
                textpoint = font.render("You got " + str(Paddlepoints) + " point(s)!", True, (255, 255, 255))
                textpointRect = textpoint.get_rect()
                textpointRect.center = (600, 250)
                screen.blit(textpoint, textpointRect)
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False
    
    pygame.display.flip()