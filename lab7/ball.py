import pygame

pygame.init() # initializies all
# pygame submodules

# create our game window (game surface)
WIDTH = 800
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True # variable responsible for our game loop

is_yellow = False

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

mov_speed = 20

clock = pygame.time.Clock()

FPS = 60 # Frames per second

# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_yellow = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                is_yellow = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and circle_y - 25 - mov_speed >= 0:  # Adjust for top boundary
     circle_y -= mov_speed
    if keys[pygame.K_DOWN] and circle_y + 25 + mov_speed <= HEIGHT:  # Adjust for bottom boundary
     circle_y += mov_speed
    if keys[pygame.K_RIGHT] and circle_x + 25 + mov_speed <= WIDTH:  # Adjust for right boundary
     circle_x += mov_speed
    if keys[pygame.K_LEFT] and circle_x - 25 - mov_speed >= 0:  # Adjust for left boundary
     circle_x -= mov_speed


    # fill the screen with a color to wipe away anything from last frame
    circle_pos = (circle_x, circle_y)
    if is_yellow:
        screen.fill("red")
        pygame.draw.circle(screen, "white", circle_pos, 25)
    else:
        screen.fill("white")
        pygame.draw.circle(screen, "red", circle_pos, 25)


    # updates the screen (game window)
    pygame.display.flip()

    clock.tick(FPS) # set the FPS limit for the game