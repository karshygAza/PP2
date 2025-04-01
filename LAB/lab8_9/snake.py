import pygame
import random
import time

pygame.init()

# Размеры экрана и блока
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
# Цвета
WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0)
# Настройки экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
font = pygame.font.SysFont("Arial", 25)

clock = pygame.time.Clock()
snake_speed = 10  # Начальная скорость змеи

def display_text(text, color, x, y):
    screen.blit(font.render(text, True, color), (x, y))
# Функция для генерации случайного положения еды
def generate_food(timer_based=True):
    return {
        "x": random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
        "y": random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE,
        "weight": random.choice([1, 2, 3]),  # Вес еды
        "spawn_time": time.time(),
        "timer_based": timer_based
    }

def gameLoop():
    global snake_speed 
    game_over, game_close = False, False

    x1, y1 = WIDTH // 2, HEIGHT // 2
    x1_change, y1_change = 0, 0
    snake_List = []
    Length_of_snake = 1

    food_timer = generate_food(True)
    food_permanent = generate_food(False)
    food_lifetime = 5
    score, level = 0, 1

    level_threshold = 30  # Порог для повышения уровня
    last_level_up_score = 0  # Следим за последним достижением уровня

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            display_text("Press C or Q", BLACK, WIDTH // 2.7, HEIGHT // 2.1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change, y1_change = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change, y1_change = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change, y1_change = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change, y1_change = 0, BLOCK_SIZE

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(WHITE)

        if food_timer["timer_based"] and time.time() - food_timer["spawn_time"] > food_lifetime:
            food_timer = generate_food(True)

        # Рисуем еду с размерами в зависимости от ее веса
        food_timer_size = BLOCK_SIZE + food_timer["weight"] * 5
        pygame.draw.rect(screen, GREEN, [food_timer["x"], food_timer["y"], food_timer_size, food_timer_size])

        food_permanent_size = BLOCK_SIZE + food_permanent["weight"] * 5
        pygame.draw.rect(screen, RED, [food_permanent["x"], food_permanent["y"], food_permanent_size, food_permanent_size])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for block in snake_List[:-1]:
            if block == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(screen, BLACK, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])

        if x1 == food_timer["x"] and y1 == food_timer["y"]:
            food_timer = generate_food(True)
            Length_of_snake += food_timer["weight"]
            score += 10 * food_timer["weight"]

        if x1 == food_permanent["x"] and y1 == food_permanent["y"]:
            food_permanent = generate_food(False)
            Length_of_snake += food_permanent["weight"]
            score += 10 * food_permanent["weight"]

        if score >= last_level_up_score + level_threshold:
            level += 1
            last_level_up_score = score
            snake_speed += 1 
            
        display_text(f"Score: {score} Level: {level}", BLACK, 10, 10)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()

gameLoop()