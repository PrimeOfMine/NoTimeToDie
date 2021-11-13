import tkinter
import pygame
from tkinter import *
import time 
import sys
import numpy as np
import cv2
import pyautogui as pg # 좌표 출력 
import os
from pygame import image
from pygame.constants import GL_ACCUM_RED_SIZE, MOUSEBUTTONUP, NOFRAME
from pygame.locals import QUIT, KEYDOWN
from tkinter import filedialog
from pathlib import Path


pygame.init()

x = 200 # 새로 늘릴 x축 

# setting display     
Surface = pygame.display.set_mode((200+1000, 750))

#setting fps
FPSCLOCK  = pygame.time.Clock()

# naming 
pygame.display.set_caption("For Handwriting")

# Not edited img

img_eraser = pygame.image.load("eraser.png")
img_eraser_click = pygame.image.load("eraser_click.png")
img_handwriteEraser = pygame.image.load("handwriteEraser.png")
img_handwriteEraser_click = pygame.image.load("handwriteEraser_click.png")
img_search = pygame.image.load("search.png")
img_search_click = pygame.image.load("search_click.png")
img_main = pygame.image.load("main.png")

# 기능 이미지 사진
image_scale_handwriteEraser = pygame.transform.scale(img_handwriteEraser, (250, 250))
image_scale_handwriteEraser_click = pygame.transform.scale(img_handwriteEraser_click, (250, 250))
image_scale_eraser = pygame.transform.scale(img_eraser, (250, 250))
image_scale_eraser_click = pygame.transform.scale(img_eraser_click, (250, 250))
image_scale_search = pygame.transform.scale(img_search, (250, 250))
image_scale_search_click = pygame.transform.scale(img_search_click, (250, 250))
img_scale_main = pygame.transform.scale(img_main, (750, 750))

# User image(사용할 이미지)   
imgPath = list() # 이미지 path 
mainImg = list() # 이미지 file
scale_mainImg = list() # scale 이미지 file
small_img = list() # 버튼 이미지
global show_main





# 버튼 클릭시 action을 실행한다.
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
  global imgPath
  
  
  root = tkinter.Tk()
  root.withdraw()
  dir_path = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
  file_list = os.listdir(dir_path)

  for i in range(0, len(file_list)):
    imgPath.append(dir_path + '/' + file_list[i]) # 이미지 주소 
    mainImg.append(pygame.image.load(imgPath[i])) # 이미지 파일
    scale_mainImg.append(pygame.transform.scale(mainImg[i], (750, 750))) # 화면 비율에 맞춘 이미지 
    small_img.append(pygame.transform.scale(scale_mainImg[i], (100, 100))) # 좌측 버튼 이미지 
  print(type(scale_mainImg))
  
# 리스트 번호 
index = 0


# 메인에 화면 송출
def main_screen(i):
  if  i == 0:
    Surface.blit(img_scale_main, (200, 0)) # 기본은 검은 화면 
  if i == 1: 
    Surface.blit(scale_mainImg[0], (200, 0)) # 첫번째 이미지(1)
  if i == 2: 
    Surface.blit(scale_mainImg[1], (200, 0)) # (2)  
  if i == 3: 
    Surface.blit(scale_mainImg[2], (200, 0)) # (3)
  if i == 4: 
    Surface.blit(scale_mainImg[3], (200, 0)) # (4)
  if i == 5: 
    Surface.blit(scale_mainImg[4], (200, 0))# (5)


  
 
   

# 작은 이미지 버튼 클릭 시 사진 출력 (parameter가 없어야 정상적으로 작동하는 것 같다) --> 깔끔하진 않지만 정상작동한다.
def main_img1(): 
  global index
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      index = 1

def main_img2(): 
  global index
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      index = 2        

def main_img3(): 
  global index
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      index = 3  

def main_img4(): 
  global index
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      index = 4   

def main_img5(): 
  global index
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      index = 5                           
      
# kmeans
def kmeans_color_quantization(image, clusters=2, rounds=1): # parameter => 경로 
   
    h, w = image.shape[:2]
    samples = np.zeros([h*w,3], dtype=np.float32)
    
    count = 0
    for x in range(h):
        for y in range(w):
            samples[count] = image[x][y]
            count += 1

    compactness, labels, centers = cv2.kmeans(samples,
            clusters, 
            None,
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001), 
            attempts = rounds, 
            flags = cv2.KMEANS_PP_CENTERS)

    ceters = np.uint8(centers)
    res = centers[labels.flatten()]
    return res.reshape((image.shape))

# 실행 코드

def execute(): 
  highlight_erasedImg = list()
  surf = list()
  tmp = list()
  global scale_mainImg

  for ele in imgPath: # 경로에 한글이 들어가지 않도록 주의
    highlight_erasedImg.append(kmeans_color_quantization(cv2.imread(ele)))

  for i in range(0, len(highlight_erasedImg)):
    surf.append(pygame.surfarray.make_surface(highlight_erasedImg[i]))
    highlight_erasedImg[i] = pygame.transform.scale(surf[i], (750, 750))
    mainImg[i] = highlight_erasedImg[i]
    tmp.append(pygame.transform.scale(mainImg[i], (750, 750)))
  
  for i in range(0, len(tmp)):
    tmp[i] = pygame.transform.flip(tmp[i], True, False)
    tmp[i] = pygame.transform.rotate(tmp[i], 90)
    scale_mainImg[i] = tmp[i]   

# main 
def main():
  while True: 
    
    
    
    # display color
    Surface.fill((255, 255, 255))
    main_screen(index)
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      
    
    # 왼쪽 이미지 리스트 구역 
    pygame.draw.rect(Surface, (255, 255, 255), (0, 0, 200, 750))
    
    
    
    # 기능 버튼 
    highlightEraser_Buttom = Button(image_scale_eraser, x+750, 0, 250, 250, image_scale_eraser_click, x+750, 0, execute) # Surface.blit(image_scale_spoid, (860, 50))
    handWriteEraser_Buttom = Button(image_scale_handwriteEraser, x+750, 250, 250, 250, image_scale_handwriteEraser_click, x+750, 250, execute) # Surface.blit(image_scale_eraser, (860, 570))
    Search_Buttom = Button(image_scale_search, x+750, 500, 250, 250, image_scale_search_click, x+750, 500, img_load) # Surface.blit(img_pen, (860 , 310))
    
    # 작은 이미지 버튼 
    if len(scale_mainImg) >= 1: 
      img0_button = Button(small_img[0], 50, 25, 100, 100, small_img[0], 50, 25, main_img1) 
      if len(scale_mainImg) >= 2: 
        img1_button = Button(small_img[1], 50, 25+150, 100, 100, small_img[1], 50, 25+150, main_img2)
        if len(scale_mainImg) >= 3:
          img2_button = Button(small_img[2], 50, 175+150, 100, 100, small_img[2], 50, 175+150, main_img2)
          if len(scale_mainImg) >= 4: 
            img3_button = Button(small_img[3], 50, 225+150, 100, 100, small_img[3], 50, 225+150, main_img2)
            if len(scale_mainImg) >= 5: 
              img4_button = Button(small_img[4], 50, 375+150, 100, 100, small_img[4], 50, 375+150, main_img2)
   
    pygame.display.update()
    FPSCLOCK.tick(30)  
    

if __name__ == '__main__': 
    main()

