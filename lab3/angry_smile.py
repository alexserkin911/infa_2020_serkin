import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption('Angry Smile')
screen.fill((125, 125, 125))

icon = pygame.image.load('kisspng-facebook-like-button-emoticon-computer-icons-react-angry-emoji-5ac1ab6825b399.7744776515226417681544.png')
pygame.display.set_icon(icon)

circle(screen, (255, 255, 0), (300, 300), 150)
circle(screen, (0, 0, 0), (300, 300), 150, 5)

circle(screen, (255, 0, 0), (240, 250), 30)
circle(screen, (0, 0, 0), (240, 250), 30, 3)
circle(screen, (0, 0, 0), (240, 250), 15)

circle(screen, (255, 0, 0), (350, 250), 33)
circle(screen, (0, 0, 0), (350, 250), 33, 3)
circle(screen, (0, 0, 0), (350, 250), 12)

rect(screen, (0, 0, 0), (240, 360, 120, 20))
polygon(screen, (0, 0, 0), [(140,150), (120,170), (280,235), (290, 215)])

polygon(screen, (0, 0, 0), [(425,138), (440, 160), (315, 233), (300,210)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True



pygame.quit()