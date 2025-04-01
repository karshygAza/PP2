import pygame
import random

# Инициализация pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

# Начальные параметры
radius = 12
mode = 'draw'
current_color = (0, 0, 255)
points = []  # Список для порядка отрисовки
last_pos = None  # Для хранения предыдущей позиции

# Основной цикл
running = True
start_pos = None
while running:
    pressed = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                current_color = (255, 0, 0)
            elif event.key == pygame.K_g:
                current_color = (0, 255, 0) 
            elif event.key == pygame.K_b:
                current_color = (0, 0, 255)
            elif event.key == pygame.K_e:
                mode = 'erase'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_t:
                mode = 'rect' 
            elif event.key == pygame.K_d:
                mode = 'draw'
            elif event.key == pygame.K_UP:
                radius = min(100, radius + 5)
            elif event.key == pygame.K_DOWN:
                radius = max(5, radius - 5)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos  # Запоминаем начальную точку
            last_pos = start_pos   # Запоминаем последнюю точку для рисования линий
        
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            end_pos = event.pos
            if mode == 'draw' and last_pos is not None:
                points.append(('line', last_pos, end_pos, current_color, radius))
                last_pos = end_pos  # Обновляем последнюю позицию для линии
            elif mode == 'erase':
                points = [item for item in draw_order if not (
                    (item[0] == 'line' and ((item[1][0] - end_pos[0]) ** 2 + (item[1][1] - end_pos[1]) ** 2) <= radius ** 2) or 
                    (item[0] == 'circle' and ((item[1][0] - end_pos[0]) ** 2 + (item[1][1] - end_pos[1]) ** 2) <= item[3] ** 2) or
                    (item[0] == 'rect' and pygame.Rect(min(item[1][0], item[2][0]), min(item[1][1], item[2][1]), abs(item[2][0] - item[1][0]), abs(item[2][1] - item[1][1])).collidepoint(end_pos))
                )]
            elif mode == 'circle':
                draw_order.append(('circle', end_pos, current_color, radius))
            elif mode == 'rect':
                draw_order.append(('rect', start_pos, end_pos, current_color))
    
    # Очистка экрана
    screen.fill((0, 0, 0))
    
    # Отрисовка всех элементов в порядке их добавления
    for item in draw_order:
        if item[0] == 'line':
            pygame.draw.line(screen, item[3], item[1], item[2], item[4])
        elif item[0] == 'circle':
            pygame.draw.circle(screen, item[2], item[1], item[3])
        elif item[0] == 'rect':
            start, end, color = item[1], item[2], item[3]
            pygame.draw.rect(screen, color, (min(start[0], end[0]), min(start[1], end[1]), abs(end[0] - start[0]), abs(end[1] - start[1])))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()