import numpy as np
import random
import cv2
import matplotlib.pyplot as pyplot
from PIL import Image

def noteimg_crop(img):
    m=[]
    n=[]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if all(img[i,j]!=[255,255,255]):
                m.append(i)
                n.append(j)
            
    img=img[min(m)+30:max(m)-70,min(n)+180:max(n)-120]#이거는 102.png일 때 직접 맞춰 놓은 픽셀
    img=cv2.resize(img,dsize=(256,256),interpolation=cv2.INTER_AREA)
    
    return img


img_hl=cv2.imread(r'images\HIGHLIGHT_IMG\1111111.jpg')
img=cv2.imread(r'images\TLGAN\0.jpg')
added_img=cv2.addWeighted(img,0.9,img_hl,1.2,0)
cv2.imwrite('img_with_highlight.jpg',added_img)

'''
img[100:130,100:200]=img[100:130,100:200]+img_hl
img=cv2.bitwise_not(img)
pyplot.imshow(img)
pyplot.show()'''
'''roi=img[100:100+30,100:100+100]
roi=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
img_hl=cv2.cvtColor(img_hl,cv2.COLOR_BGR2GRAY)
ret, note_mask=cv2.threshold(img_hl,220,255,cv2.THRESH_BINARY)
note_mask_inv=cv2.bitwise_not(note_mask)

img_bg=cv2.bitwise_and(roi, roi,mask=note_mask)
img_fg=cv2.bitwise_and(img_hl, img_hl,mask=note_mask_inv)

dst=cv2.bitwise_or(img_bg,img_fg)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img[100:100+30,100:100+100]=dst
pyplot.imshow(img,cmap='gray')
pyplot.show()'''