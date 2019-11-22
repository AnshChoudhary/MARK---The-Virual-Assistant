import pygame
from pygame.locals import *
from sys import exit

#initalizing variables (setting up the stage) 
pygame.init()
screen=pygame.display.set_mode((1120,480),0,24)
pygame.display.set_caption("ZIRA")
create=pygame.font.SysFont("courier new",30)
f=create.render("Hello! I am your personal assistant ZIRA",True,(0,0,0),(255,255,255))
img=pygame.image.load("apollo.png").convert()


#main loop which displays the hello world in visual mode
while True:
 for i in pygame.event.get():
    
  if i.type==QUIT:
   exit()

 screen.blit(img,(0,0))
 screen.blit(f,(200,200))
 pygame.display.update()