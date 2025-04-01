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
draw_order = []  # Список для порядка отрисовки
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
            elif event.key == pygame.K_s:
                mode = 'square'
            elif event.key == pygame.K_q:
                mode = 'right_triangle'
            elif event.key == pygame.K_h:
                mode = 'rhombus'
            elif event.key == pygame.K_i:
                mode = 'equilateral_triangle'

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos  # Запоминаем начальную точку
            last_pos = start_pos   # Запоминаем последнюю точку для рисования линий
        
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            end_pos = event.pos
            if mode == 'draw' and last_pos is not None:
                draw_order.append(('line', last_pos, end_pos, current_color, radius))
                last_pos = end_pos  # Обновляем последнюю позицию для линии
            elif mode == 'erase':
                draw_order = [item for item in draw_order if not (
                    (item[0] == 'line' and ((item[1][0] - end_pos[0]) ** 2 + (item[1][1] - end_pos[1]) ** 2) <= radius ** 2) or 
                    (item[0] == 'circle' and ((item[1][0] - end_pos[0]) ** 2 + (item[1][1] - end_pos[1]) ** 2) <= item[3] ** 2) or
                    (item[0] == 'rect' and pygame.Rect(min(item[1][0], item[2][0]), min(item[1][1], item[2][1]), abs(item[2][0] - item[1][0]), abs(item[2][1] - item[1][1])).collidepoint(end_pos)) or
                    (item[0] == 'square' and pygame.Rect(item[1][0], item[1][1], item[2], item[2]).collidepoint(end_pos)) or
                    (item[0] == 'right_triangle' and pygame.draw.polygon(screen, (0, 0, 0), [item[1], (item[1][0], item[2][1]), item[2]]).collidepoint(end_pos)) or
                    (item[0] == 'rhombus' and pygame.draw.polygon(screen, (0, 0, 0), [
                        (item[1][0], item[1][1] - item[2]),
                        (item[1][0] + item[3], item[1][1]),
                        (item[1][0], item[1][1] + item[2]),
                        (item[1][0] - item[3], item[1][1])
                    ]).collidepoint(end_pos)) or
                    (item[0] == 'equilateral_triangle' and pygame.draw.polygon(screen, (0, 0, 0), [
                        (item[1][0], item[1][1]),
                        (item[1][0] - item[2] // 2, item[1][1] + item[2]),
                        (item[1][0] + item[2] // 2, item[1][1] + item[2])
                    ]).collidepoint(end_pos))
                )]
            else:
                screen.fill((0, 0, 0))
                for item in draw_order:
                    if item[0] == 'line':
                        pygame.draw.line(screen, item[3], item[1], item[2], item[4])
                    elif item[0] == 'circle':
                        pygame.draw.circle(screen, item[2], item[1], item[3])
                    elif item[0] == 'rect':
                        start, end, color = item[1], item[2], item[3]
                        pygame.draw.rect(screen, color, (min(start[0], end[0]), min(start[1], end[1]), abs(end[0] - start[0]), abs(end[1] - start[1])))
                    elif item[0] == 'square':
                        start, side, color = item[1], item[2], item[3]
                        pygame.draw.rect(screen, color, (start[0], start[1], side, side))
                    elif item[0] == 'right_triangle':
                        start, end, color = item[1], item[2], item[3]
                        pygame.draw.polygon(screen, color, [start, (start[0], end[1]), end])
                    elif item[0] == 'rhombus':
                        center, half_width, half_height, color = item[1], item[2], item[3], item[4]
                        pygame.draw.polygon(screen, color, [
                            (center[0], center[1] - half_height),
                            (center[0] + half_width, center[1]),
                            (center[0], center[1] + half_height),
                            (center[0] - half_width, center[1])
                        ])
                    elif item[0] == 'equilateral_triangle':
                        start, height, color = item[1], item[2], item[3]
                        pygame.draw.polygon(screen, color, [
                            (start[0], start[1]),
                            (start[0] - height // 2, start[1] + height), 
                            (start[0] + height // 2, start[1] + height) 
                        ])
                
                if mode == 'square':
                    side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], side, side))
                elif mode == 'right_triangle':
                    pygame.draw.polygon(screen, current_color, [start_pos, (start_pos[0], end_pos[1]), end_pos])
                elif mode == 'rhombus':
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    half_width = abs(end_pos[0] - start_pos[0]) // 2
                    half_height = abs(end_pos[1] - start_pos[1]) // 2
                    pygame.draw.polygon(screen, current_color, [
                        (center[0], center[1] - half_height),
                        (center[0] + half_width, center[1]), 
                        (center[0], center[1] + half_height),
                        (center[0] - half_width, center[1])
                    ])
                elif mode == 'equilateral_triangle':
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(screen, current_color, [
                        (start_pos[0], start_pos[1]),
                        (start_pos[0] - height // 2, start_pos[1] + height),
                        (start_pos[0] + height // 2, start_pos[1] + height)
                    ])
                
                pygame.display.flip()
        
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if mode == 'square':
                side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                draw_order.append(('square', start_pos, side, current_color))
            elif mode == 'right_triangle':
                draw_order.append(('right_triangle', start_pos, end_pos, current_color))
            elif mode == 'rhombus':
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                draw_order.append(('rhombus', center, abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2, current_color))
            elif mode == 'equilateral_triangle':
                height = abs(end_pos[1] - start_pos[1])
                draw_order.append(('equilateral_triangle', start_pos, height, current_color))

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
        elif item[0] == 'square':
            start, side, color = item[1], item[2], item[3]
            pygame.draw.rect(screen, color, (start[0], start[1], side, side))
        elif item[0] == 'right_triangle':
            start, end, color = item[1], item[2], item[3]
            pygame.draw.polygon(screen, color, [start, (start[0], end[1]), end])
        elif item[0] == 'rhombus':
            center, half_width, half_height, color = item[1], item[2], item[3], item[4]
            pygame.draw.polygon(screen, color, [
                (center[0], center[1] - half_height),
                (center[0] + half_width, center[1]),
                (center[0], center[1] + half_height),
                (center[0] - half_width, center[1]) 
            ])
        elif item[0] == 'equilateral_triangle':
            start, height, color = item[1], item[2], item[3]
            pygame.draw.polygon(screen, color, [
                (start[0], start[1]),
                (start[0] - height // 2, start[1] + height),
                (start[0] + height // 2, start[1] + height)
            ])
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()