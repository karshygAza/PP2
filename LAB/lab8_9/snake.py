import pygame
import random

# Инициализация pygame
pygame.init()

# Размеры экрана и блока
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# Цвета
WHITE, BLACK, GREEN = (255, 255, 255), (0, 0, 0), (0, 255, 0)

# Настройки экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
font = pygame.font.SysFont("Arial", 25)

clock = pygame.time.Clock()
snake_speed = 10

# Функция для отображения текста на экране
def display_text(text, color, x, y):
    screen.blit(font.render(text, True, color), (x, y))

# Функция для генерации случайного положения еды
def generate_food():
    return (random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE, 
            random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE)

# Основная игровая функция
def gameLoop():
    game_over, game_close = False, False

    # Начальная позиция змейки
    x1, y1 = WIDTH // 2, HEIGHT // 2
    x1_change, y1_change = 0, 0

    # Тело змеи
    snake_List = []
    Length_of_snake = 1

    # Создание первой еды
    foodx, foody = generate_food()
    score, level = 0, 1

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            display_text("Press C or Q", BLACK, WIDTH // 4, HEIGHT // 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        # Обработка нажатий клавиш
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

        # Проверка на столкновение со стенами
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(WHITE)

        # Отрисовка еды
        pygame.draw.rect(screen, GREEN, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])

        # Обновление позиции змеи
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение с самой собой
        for block in snake_List[:-1]:
            if block == snake_Head:
                game_close = True

        # Отрисовка змеи
        for x in snake_List:
            pygame.draw.rect(screen, BLACK, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])

        # Проверка на съедение еды
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()
            Length_of_snake += 1
            score += 10  # Увеличение очков

            # Увеличение уровня каждые 30 очков
            if score % 30 == 0:
                level += 1
                global snake_speed
                snake_speed += 2  # Ускорение змеи

        # Отображение счета и уровня
        display_text(f"Score: {score} Level: {level}", BLACK, 10, 10)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()

gameLoop()