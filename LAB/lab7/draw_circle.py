import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Circle")
ball_radius = 25
ball_color = (255, 0, 0)
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 20

clock = pygame.time.Clock()

while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if ball_y - ball_radius > 0:
            ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        if ball_y + ball_radius < HEIGHT:
            ball_y += ball_speed
    if keys[pygame.K_LEFT]:
        if ball_x - ball_radius > 0:
            ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        if ball_x + ball_radius < WIDTH:
            ball_x += ball_speed

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.update()

    clock.tick(60)