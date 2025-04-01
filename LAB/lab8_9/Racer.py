import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Настройки игры
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
blue  = (0, 0, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Размеры экрана и параметры
screen_height = 600
screen_width = 400
speed = 5
score = 0
coins_collected = 0
COIN_THRESHOLD = 5

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

# Загрузка фона
background = pygame.image.load("/Users/azamat/Documents/GitHub/PP2/LAB/lab8_9/AnimatedStreet.png")

displaysurf = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racer")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/azamat/Documents/GitHub/PP2/LAB/lab8_9/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
        
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom > screen_height:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/azamat/Documents/GitHub/PP2/LAB/lab8_9/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1, 2, 3])
        self.image = pygame.image.load("/Users/azamat/Documents/GitHub/PP2/LAB/lab8_9/coin.png")
        size = 20 + (self.weight * 5)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
        self.speed = random.randint(1, 3)
        
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > screen_height:
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), random.randint(0, screen_height // 2))
        
# Инициализация объектов
P1 = Player()
E1 = Enemy()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)
coins = pygame.sprite.Group()

# Таймер
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

# Загрузка музыки
pygame.mixer.music.load('/Users/azamat/Documents/GitHub/PP2/LAB/lab8_9/background.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.35)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    displaysurf.blit(background, (0, 0))
    displaysurf.blit(font_small.render(str(score), True, black), (10, 10))
    displaysurf.blit(font_small.render(str(coins_collected), True, black), (screen_width - 100, 10))
    
    if random.random() < 0.01:
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
        
    for coin in coins:
        coin.move()
        displaysurf.blit(coin.image, coin.rect)
    
    for entity in all_sprites:
        entity.move()
        displaysurf.blit(entity.image, entity.rect)
        
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        coins_collected += coin.weight
        if coins_collected % COIN_THRESHOLD == 0:
            speed += 0.5
        
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('/Users/azamat/Documents/GitHub/PP2/LAB/lab8_9/crash.wav').play()
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