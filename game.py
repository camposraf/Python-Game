import pygame

pygame.init

display_width = 1920
display_height = 1080

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Python Game')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
charImg = pygame.image.load('character.png')

def char(x,y):
    gameDisplay.blit(charImg, (x,y))

x = (display_width * 0.45)
y = (display_height *0.8)
x_change = 0
y_change = 0
char_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -5
            elif event.key == pygame.K_d:
                x_change = 5
            if event.key == pygame.K_w:
                y_change = -5
            elif event.key == pygame.K_s:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                y_change = 0

    x += x_change
    y += y_change

    gameDisplay.fill(white)
    char(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()