import pygame
import time
import threading
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
color = 255, 255, 255
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
game_over = False

def change_speed():
    global speed
    speed = [speed[0]+1, speed[1]+1]
    timer = threading.Timer(2.0, change_speed)
    timer.start()

def affichage():
    screen.fill(color)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    timer2 = threading.Timer(0.007, affichage)
    timer2.start()

def calcul():
    global ballrect
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    timer3 = threading.Timer(0.007, calcul)
    timer3.start()

change_speed()
calcul()
affichage()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()
