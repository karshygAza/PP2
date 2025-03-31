import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

blue  = (0, 0, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

screen_height = 600
screen_width = 400
speed = 5
score = 0
coins_collected = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

background = pygame.image.load("/Users/azamat/Documents/GitHub/PP2/LAB/lab8/AnimatedStreet.png")

displaysurf = pygame.display.set_mode((screen_width, screen_height))
displaysurf.fill(white)
pygame.display.set_caption("Racer")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/azamat/Documents/GitHub/PP2/LAB/lab8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
        
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 600:
            score += 2
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0)
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/azamat/Documents/GitHub/PP2/LAB/lab8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/azamat/Documents/GitHub/PP2/LAB/lab8/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
        
    def move(self):
        global coins_collected
        self.rect.move_ip(0, 1)
        if self.rect.bottom > screen_height:
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), random.randint(0, screen_height // 2))
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
        
P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

pygame.mixer.music.load('/Users/azamat/Documents/GitHub/PP2/LAB/lab8/background.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.35)

while True:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    displaysurf.blit(background, (0, 0))
    
    scores = font_small.render(str(score), True, black)
    displaysurf.blit(scores, (10, 10))
    
    coins_display = font_small.render(str(coins_collected), True, black)
    displaysurf.blit(coins_display, (screen_width - 100, 10))
    
    if random.random() < 0.005:
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
        
    for coin in coins:
        coin.move()
        coin.draw(displaysurf)        
    
    for entity in all_sprites:
        entity.move()
        displaysurf.blit(entity.image, entity.rect)
        
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for _ in collected_coins:
        coins_collected += 1
        
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('/Users/azamat/Documents/GitHub/PP2/LAB/lab8/crash.wav').play()
        time.sleep(1)

        displaysurf.fill(red)
        displaysurf.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()         

    pygame.display.update()
    FramePerSec.tick(FPS)