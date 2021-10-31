import tkinter
import pygame
from tkinter import *
import time 
import sys
from PIL import ImageTk, Image
from pygame import image
from pygame.constants import GL_ACCUM_RED_SIZE
from pygame.locals import QUIT
from tkinter import filedialog
pygame.init()

# setting display     
Surface = pygame.display.set_mode((1000, 700))

#setting fps
FPSCLOCK  = pygame.time.Clock()

# naming 
pygame.display.set_caption("For Handwriting")

# Not edited img
img_spoid = pygame.image.load("spoid.png")
img_spoid_click = pygame.image.load("spoid_click.png")
img_pen = pygame.image.load("pen.png")
img_pen_click = pygame.image.load("pen_click.png")
img_eraser = pygame.image.load("eraser.png")
img_eraser_click = pygame.image.load("eraser_click.png")
img_button =  pygame.image.load("image.png")

# User image   
userImg = None

#image size transform (weith, height)
image_scale_spoid = pygame.transform.scale(img_spoid, (80, 80))
image_scale_spoid_click = pygame.transform.scale(img_spoid_click, (80, 80))
image_scale_pen = pygame.transform.scale(img_pen, (80, 80))
image_scale_pen_click = pygame.transform.scale(img_pen_click, (80, 80))
image_scale_eraser = pygame.transform.scale(img_eraser, (80, 80))
image_scale_eraser_click = pygame.transform.scale(img_eraser_click, (80, 80))

# 버튼: action(기능)

class Button:
  def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y: 
      Surface.blit(img_act, (x_act, y_act))
      if click[0] and action != None: 
        time.sleep(1)
        action()
    else: 
        Surface.blit(img_in, (x, y))

def img_load(): 
  global userImg
  root = tkinter.Tk()
  root.withdraw()
  root.filename =  filedialog.askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
  userImg = root.filename
 
  
# main 
def main():
                                                 
    while True: 
      
      # display color
      Surface.fill((0, 0, 0))
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      
      # side window 
      pygame.draw.rect(Surface, (255, 255, 255), (800, 0, 200, 700))

      # Button option  
      Spoid_Buttom = Button(image_scale_spoid, 860, 50, 80, 80, image_scale_spoid_click, 860, 50, None) # Surface.blit(image_scale_spoid, (860, 50))
      Pen_Buttom = Button(image_scale_pen, 860, 310, 80, 80, image_scale_pen_click, 860, 310, None) # Surface.blit(img_pen, (860 , 310))
      Eraser_Buttom = Button(image_scale_eraser, 860, 570, 80, 80, image_scale_eraser_click, 860, 570, None) # Surface.blit(image_scale_eraser, (860, 570))
      load_Buttom = Button(img_button, 870, 650, 80, 80, img_button, 870, 650, img_load)

      # load image  
      if userImg is not None: 
        
        use_image = pygame.image.load(userImg)
        scale_use_image = pygame.transform.scale(use_image, (800, 700))
        Surface.blit(scale_use_image, (0, 0)) # pygame.draw.rect(dir_path, (255, 255, 255), (800, 0, 200, 700))
        

      # show display
      pygame.display.update()
      FPSCLOCK.tick(30)

if __name__ == '__main__': 
    main()

