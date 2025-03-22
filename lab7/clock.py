import pygame
import datetime

pygame.init()
clock = pygame.time.Clock()

width, height = 1100, 800
pygame.display.set_caption("Mickey's clock")

backround = pygame.image.load("clock.png")
backround = pygame.transform.scale(backround, (1050, 800))
p_hand = pygame.image.load("min_hand.png")
p_hand = pygame.transform.scale(p_hand, (1050, 800))
l_hand = pygame.image.load("sec_hand.png")
l_hand = pygame.transform.scale(l_hand, (1050, 800))

screen = pygame.display.set_mode((width, height))
screen.fill("White")
isRunning = True
center_x = width // 2
center_y = height // 2

while isRunning:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    now = datetime.datetime.now()
    minute = now.minute
    second = now.second
    
    anglefs = -6 * second + 57
    anglefm = -6 * minute - 47

    rotated_sec = pygame.transform.rotate(l_hand, anglefs)
    rotated_min = pygame.transform.rotate(p_hand, anglefm)

    sec_pos = (center_x - rotated_sec.get_width() // 2, center_y - rotated_sec.get_height() // 2)
    min_pos = (center_x - rotated_min.get_width() // 2, center_y - rotated_min.get_height() // 2)

    screen.blit(backround, (10, 0))
    screen.blit(rotated_sec, sec_pos)
    screen.blit(rotated_min, min_pos)

    pygame.display.update()

pygame.quit()
