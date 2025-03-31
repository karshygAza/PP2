import time
import pygame 
import math

pygame.init()

screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption('Mickey clock')

mickey = pygame.image.load('/Users/azamat/Documents/GitHub/PP2/LAB/lab7/clock.png')
right_hand = pygame.image.load('/Users/azamat/Documents/GitHub/PP2/LAB/lab7/right_hand.png')
left_hand = pygame.image.load('/Users/azamat/Documents/GitHub/PP2/LAB/lab7/left_hand.png')

right_hand = pygame.transform.scale(right_hand, (1400, 1050))
left_hand = pygame.transform.scale(left_hand, (63, 1050))

center_x = 450
center_y = 450

running = True
while running:
    screen.fill((255, 255, 255))
    
    current_time = time.localtime()
    sec = current_time.tm_sec
    minute = current_time.tm_min
    
    sec_angle = math.radians(6 * sec - 90)
    min_angle = math.radians(6 * minute - 90)
    
    right_hand_rotate = pygame.transform.rotate(right_hand, -(minute * 6))
    right_hand_rect = right_hand_rotate.get_rect(center=(center_x, center_y))
    
    left_hand_rotate = pygame.transform.rotate(left_hand, -(sec * 6))
    left_hand_rect = left_hand_rotate.get_rect(center=(center_x, center_y))
    
    screen.blit(mickey, (center_x - mickey.get_width() // 2, center_y - mickey.get_height() // 2))
    screen.blit(right_hand_rotate, right_hand_rect)
    screen.blit(left_hand_rotate, left_hand_rect)    
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()          