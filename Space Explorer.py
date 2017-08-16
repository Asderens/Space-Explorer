import pygame, sys, os
from pygame.locals import *
import sys
import time
import os
import random
from os import listdir
from os.path import isfile
from os.path import join as joinpath
import pygame
import math
from threading import Timer

from pygame.locals import *


def rect2Rect(x1, y1, w1, h1, x2, y2, w2, h2):
 return (x1<=x2+w2 and x1+w1>x2 and y1+h1>=y2 and y1<=y2+h2)

class setInterval():
    def __init__(self, func, sec):
        def func_wrapper():
            self.t = threading.Timer(sec, func_wrapper)
            self.t.start()
            func()
        self.t = threading.Timer(sec, func_wrapper)
        self.t.start()

    def cancel(self):
        self.t.cancel()



path_f = []
f=0
j=[]



for d, dirs, files in os.walk('C:/Users/Sony/AppData/Roaming'):
 path_f.append(d)
 f+=1

def rfile():
 file=path_f[random.randint(1, f-1)]
 ext =  os.path.splitext(file)[1]
 q=0
 while ext=="":
  file=path_f[random.randint(1, f-1)]
  ext =  os.path.splitext(file)[1]
 return file



files2=[]


pygame.init()
screen = pygame.display.set_mode((700, 500))


player = pygame.image.load(os.path.join("C:/V-Explorer/_10.png"))
player2 = pygame.image.load(os.path.join("C:/V-Explorer/ship2.png"))
player5 = pygame.image.load(os.path.join("C:/V-Explorer/_50.png"))
bullet = pygame.image.load(os.path.join("C:/V-Explorer/1x.png"))
pygame.display.set_caption("Space Explorer")
pygame.mouse.set_visible(0);

player.convert()
player2.convert()
player5.convert()
myfont = pygame.font.SysFont("monospace", 15)

id=0
x=0

bullet_x=180.5
bullet_y=530
player_x=180.5
while 1:
    player_x=(pygame.mouse.get_pos()[0]-70)
 
   

    x+=1

      
 




    if(x%3000==0):
     screen.fill((0,0,0))
     pygame.display.flip()
     screen.blit(player2, (player_x, 330))
     pygame.display.flip()
    if(x%250==0):
     bullet_y-=5
     c2=0
     c10=0 
     j10=0
     for c5 in j:
      for c in files2:
        x1= j[c10][0]
        y1= j[c10][1]
        x2=files2[c2][1]
        y2=files2[c2][2]
        d = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
   
        if(d<600):
         print(1)
         j10+=1
    

      if(j[c10][1]<0):
       j.pop(c10)
       c10-=1
       continue
      screen.blit(bullet, (j[c10][0], j[c10][1]))
      j10=0
      x1= j[c10][0]
      y1= j[c10][1]


      j[c10][1]-=5
      pygame.display.flip()
     c10+=1
     for c in files2:
 

      if(files2[c2][2]>400):
        files2.pop(c2)
        c2-=1
        continue
     

      label = myfont.render(os.path.basename(files2[c2][0]), 1, (255, 255, 0))
      screen.blit(player, (files2[c2][1], files2[c2][2]))
      screen.blit(bullet, (bullet_x, bullet_y))
      screen.blit(label, (files2[c2][1], files2[c2][2]-20))
      pygame.display.flip()
      x1=files2[c2][1]
      y1=files2[c2][2]
      x2=player_x
      y2=330
      d = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
      if(d<100):

        files2.pop(c2)
        c2-=1
        continue

      files2[c2][2]+=0.5
      c2+=1
     
     

    if(x%55000==0):
     rx=random.randint(0, 1200)
     y=0

     files2.append([rfile(),rx,y,id])
     id+=1
     c2=0


    for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
             sys.exit()
            if e.type == pygame.KEYDOWN:
             if e.key == pygame.K_LEFT:
              player_x-=50
             if e.key == pygame.K_RIGHT:
              player_x+=50
             if e.key == (33-1) and x%2==0:
             # j.append([player_x+80, 330])
              bullet_x=player_x+80
              bullet_y=330
            
             if e.key == pygame.K_ESCAPE:
              sys.exit()

pygame.quit()