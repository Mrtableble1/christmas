import pygame
import time

pygame.init()
HEIGHT = 800
WIDTH = 800
TITLE = "Merry christmas"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

hello = 0

image1 = pygame.image.load("image/merrychristmas.jpeg")
image1 = pygame.transform.scale(image1,(800,800))

image2 = pygame.image.load("image/santaclaus.jpeg")
image2 = pygame.transform.scale(image2,(800,800))


image3 = pygame.image.load("image/merrychristmas.jpeg")
image3 = pygame.transform.scale(image3,(800,800))


while hello == 0:
    screen.blit(image1,(0,0))
    font = pygame.font.SysFont("Arial",50)
    msg1 = font.render("ho ho ho!",True,"red")
    screen.blit(msg1,(240,260))
    pygame.display.update()
    time.sleep(5)

    screen.blit(image2,(0,0))
    font = pygame.font.SysFont("Arial",50)
    msg2 = font.render("Do you want good presents!",True,"green")
    screen.blit(msg2,(220,100))
    pygame.display.update()
    time.sleep(5)

    screen.blit(image3,(0,0))
    font = pygame.font.SysFont("Arial",50)
    msg3 = font.render("then be a good child",True,"blue")
    screen.blit(msg3,(220,100))
    pygame.display.update()
    time.sleep(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hello = 1
    



    
    
    
    
    
    pygame.display.update()