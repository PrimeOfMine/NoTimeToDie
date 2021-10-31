import pyautogui as pg
import time
from PIL import ImageGrab
import pygame

# 좌표 
while True:
    screen = ImageGrab.grab() # 전체화면 캡처, 나중에 창으로 치환
    print(pg.position())
    for event in pygame.event.get():
        if pygame.MOUSEBUTTONUP: # position 포인터로 리턴
            rgb = screen.getpixel(pg.position())
            print(rgb)
# 지속적으로 마우스 커서 위치 추적 
# 클릭 입력 시 rgb 추출 