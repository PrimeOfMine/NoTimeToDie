import tkinter
import pygame
import pyautogui as pg
from tkinter import *
import time 
import sys
from PIL import ImageTk, Image, ImageGrab
from pygame import image
from pygame.constants import GL_ACCUM_RED_SIZE, NOFRAME
from pygame.locals import QUIT, KEYDOWN
from tkinter import filedialog
import pyautogui as pg
import os


pygame.init()

x = 200 # 새로 늘릴 x축 
# setting display     
Surface = pygame.display.set_mode((200+1000, 750))

#setting fps
FPSCLOCK  = pygame.time.Clock()

# naming 
pygame.display.set_caption("For Handwriting")

# Not edited img
img_spoid = pygame.image.load("spoid.png")
img_spoid_click = pygame.image.load("spoid_click.png")
img_eraser = pygame.image.load("eraser.png")
img_eraser_click = pygame.image.load("eraser_click.png")
img_search = pygame.image.load("search.png")
img_search_click = pygame.image.load("search_click.png")

# User image   
userImg = None
# img_number 
global NUM
NUM = 0
#image size transform (weith, height)
image_scale_spoid = pygame.transform.scale(img_spoid, (250, 250))
image_scale_spoid_click = pygame.transform.scale(img_spoid_click, (250, 250))
image_scale_eraser = pygame.transform.scale(img_eraser, (250, 250))
image_scale_eraser_click = pygame.transform.scale(img_eraser_click, (250, 250))
image_scale_search = pygame.transform.scale(img_search, (250, 250))
image_scale_search_click = pygame.transform.scale(img_search_click, (250, 250))
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

# user_img 배열
def img_load(): 
  global userImg
  userImg = []
  root = tkinter.Tk()
  root.withdraw()
  dir_path = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
  file_list = os.listdir(dir_path)

  for i in range(0, len(file_list)):
    userImg.append(dir_path + '/' + file_list[i])
 
# 이미지 불러오는 배열 순서 변경 
def change_num(i):
  NUM = i
  
  print("호출")


 
   
# 캡쳐가 전 화면 단위로 이루어지기 떄문에 일일이 클릭해야 할 것 같다. 
class spoid: 
  def __init__(self):
    time.sleep(1)  
    while True:
      screen = ImageGrab.grab() # 화면 캡처
    
      for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONUP: # position 포인터로 리턴
            rgb = screen.getpixel(pg.position())
            print(rgb)
            print(pg.position())
            time.sleep(.2)
            
          elif event.type == pygame.KEYDOWN: 
            return None



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
    pygame.draw.rect(Surface, (255, 255, 255), (0, 0, 200, 750))

    # Button option  
    Spoid_Buttom = Button(image_scale_spoid, x+750, 0, 250, 250, image_scale_spoid_click, x+750, 0, spoid) # Surface.blit(image_scale_spoid, (860, 50))
    Eraser_Buttom = Button(image_scale_eraser, x+750, 250, 250, 250, image_scale_eraser_click, x+750, 250, None) # Surface.blit(image_scale_eraser, (860, 570))
    Search_Buttom = Button(image_scale_search, x+750, 500, 250, 250, image_scale_search_click, x+750, 500, img_load) # Surface.blit(img_pen, (860 , 310))

    # load image  
    
    if userImg is not None: 
      use_image = []
      scale_use_image = []
      
      for i in range(0, len(userImg)):
        use_image.append(pygame.image.load(userImg[i])) 
        scale_use_image.append(pygame.transform.scale(use_image[i], (750, 750)))
      scale_use_image[NUM]
      Surface.blit(scale_use_image[NUM], (200, 0))
      # 이미지 버튼 구현: blit 함수에서 무엇인가 오류가 발생하는 듯 하다..
      
      if len(scale_use_image) >= 1: 
        img0 = pygame.transform.scale(scale_use_image[0], (100, 100))
        if len(scale_use_image) >= 2: 
          img1 = pygame.transform.scale(scale_use_image[1], (100, 100))
          if len(scale_use_image) >= 3: 
            img2 = pygame.transform.scale(scale_use_image[1], (100, 100))
            if len(scale_use_image) >= 4: 
              img3 = pygame.transform.scale(scale_use_image[1], (100, 100))
              if len(scale_use_image) >= 5: 
                img4 = pygame.transform.scale(scale_use_image[1], (100, 100))

# 반복 변수 사용 방법이 뭘까 
      for i in range(0, len(scale_use_image)):          
        temp = 'img_h{}'.format(i) 
        temp = Button("img{0}".format(i), 50, 25, 100, 100, "img{0}".format(i), 50, 25, change_num(i))
        # img2_button = Button(img1, 50, 25+150, 100, 100, img1, 50, 25+150, change_num(1))
        # img3_button = Button(img2, 50, 175+150, 100, 100, img2, 50, 175+150, change_num(2))
        # img4_button = Button(img3, 50, 225+150, 100, 100, img3, 50, 225+150, change_num(3))
        # img5_button = Button(img4, 50, 375+150, 100, 100, img4, 50, 375+150, change_num(4))
    



        

    # show display
    pygame.display.update()
    FPSCLOCK.tick(30)

if __name__ == '__main__': 
    main()

