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
            
    img=img[min(m)+3:max(m)+3,min(n)+3:max(n)+3]
    img=cv2.resize(img,dsize=(12,12),interpolation=cv2.INTER_AREA)
    
    return img

def random_pixel(img,img_note):
    data=np.load(r'C:\Users\dbelr\OneDrive\바탕 화면\박진정\images\gaussian_map\0.npy')
    img_gau=data[0]
    x=[]

    img_gau=cv2.bitwise_not(img_gau)
    ret, img_gau=cv2.threshold(img_gau,0,255,cv2.THRESH_BINARY_INV)
    
    for i in range(2,img_gau.shape[0]-14):
        for j in range(2,img_gau.shape[1]-14):
            a=0
            for k in range(16):    
                if all(img_gau[i+k-2,j-2:j+14]==[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]):
                    a+=1
            if a==16:
                x.append([i,j])
    
    x_rand,y_rand=random.choice(x)
    img[x_rand:x_rand+12,y_rand:y_rand+12]=img_note
    
    return img

def img_with_note(img_txt,img):
    img_note=noteimg_crop(img)
    img=random_pixel(img_txt,img_note)
    pyplot.imshow(img,cmap='gray')
    return img
    
img_txt0=cv2.imread(r'images\TLGAN\0.jpg')
img_txt1=cv2.imread(r'images\TLGAN\1.jpg')
img_txt2=cv2.imread(r'images\TLGAN\2.jpg')
img_txt3=cv2.imread(r'images\TLGAN\3.jpg')
img_txt4=cv2.imread(r'images\TLGAN\4.jpg')
img_txt5=cv2.imread(r'images\TLGAN\5.jpg')
img_txt6=cv2.imread(r'images\TLGAN\6.jpg')
img_txt7=cv2.imread(r'images\TLGAN\7.jpg')
img_txt8=cv2.imread(r'images\TLGAN\8.jpg')
img_txt9=cv2.imread(r'images\TLGAN\9.jpg')
img_txt10=cv2.imread(r'images\TLGAN\10.jpg')
img_txt11=cv2.imread(r'images\TLGAN\11.jpg')
img_txt12=cv2.imread(r'images\TLGAN\12.jpg')
'''
img_note0=cv2.imread(r'imageTransparent\translated0.png')
img_note1=cv2.imread(r'imageTransparent\translated1.png')
img_note2=cv2.imread(r'imageTransparent\translated2.png')
img_note3=cv2.imread(r'imageTransparent\translated3.png')
img_note4=cv2.imread(r'imageTransparent\translated4.png')
img_note5=cv2.imread(r'imageTransparent\translated5.png')
img_note6=cv2.imread(r'imageTransparent\translated6.png')
img_note7=cv2.imread(r'imageTransparent\translated7.png')
img_note8=cv2.imread(r'imageTransparent\translated8.png')
img_note9=cv2.imread(r'imageTransparent\translated9.png')
img_note10=cv2.imread(r'imageTransparent\translated10.png')
img_note11=cv2.imread(r'imageTransparent\translated11.png')
img_note12=cv2.imread(r'imageTransparent\translated12.png')
img_note13=cv2.imread(r'imageTransparent\translated13.png')
img_note14=cv2.imread(r'imageTransparent\translated14.png')
img_note15=cv2.imread(r'imageTransparent\translated15.png')
img_note16=cv2.imread(r'imageTransparent\translated16.png')
img_note17=cv2.imread(r'imageTransparent\translated17.png')
img_note18=cv2.imread(r'imageTransparent\translated18.png')
img_note19=cv2.imread(r'imageTransparent\translated19.png')
img_note20=cv2.imread(r'imageTransparent\translated20.png')
img_note21=cv2.imread(r'imageTransparent\translated21.png')
img_note22=cv2.imread(r'imageTransparent\translated22.png')
img_note23=cv2.imread(r'imageTransparent\translated23.png')
img_note24=cv2.imread(r'imageTransparent\translated24.png')
img_note25=cv2.imread(r'imageTransparent\translated25.png')
'''
img_note26=cv2.imread(r'imageTransparent\translated26.png')
img_note27=cv2.imread(r'imageTransparent\translated27.png')
img_note28=cv2.imread(r'imageTransparent\translated28.png')
img_note29=cv2.imread(r'imageTransparent\translated29.png')
img_note30=cv2.imread(r'imageTransparent\translated30.png')
img_note31=cv2.imread(r'imageTransparent\translated31.png')
img_note32=cv2.imread(r'imageTransparent\translated32.png')
img_note33=cv2.imread(r'imageTransparent\translated33.png')
img_note34=cv2.imread(r'imageTransparent\translated34.png')
img_note35=cv2.imread(r'imageTransparent\translated35.png')
img_note36=cv2.imread(r'imageTransparent\translated36.png')
img_note37=cv2.imread(r'imageTransparent\translated37.png')
img_note38=cv2.imread(r'imageTransparent\translated38.png')
'''
img_note39=cv2.imread(r'imageTransparent\translated39.png')
img_note40=cv2.imread(r'imageTransparent\translated40.png')
img_note41=cv2.imread(r'imageTransparent\translated41.png')
img_note42=cv2.imread(r'imageTransparent\translated42.png')
img_note43=cv2.imread(r'imageTransparent\translated43.png')
img_note44=cv2.imread(r'imageTransparent\translated44.png')
img_note45=cv2.imread(r'imageTransparent\translated45.png')
img_note46=cv2.imread(r'imageTransparent\translated46.png')
img_note47=cv2.imread(r'imageTransparent\translated47.png')
img_note48=cv2.imread(r'imageTransparent\translated48.png')
img_note49=cv2.imread(r'imageTransparent\translated49.png')
img_note50=cv2.imread(r'imageTransparent\translated50.png')
img_note51=cv2.imread(r'imageTransparent\translated51.png')
img_note52=cv2.imread(r'imageTransparent\translated52.png')
img_note53=cv2.imread(r'imageTransparent\translated53.png')
img_note54=cv2.imread(r'imageTransparent\translated54.png')
img_note55=cv2.imread(r'imageTransparent\translated55.png')
img_note56=cv2.imread(r'imageTransparent\translated56.png')
img_note57=cv2.imread(r'imageTransparent\translated57.png')
img_note58=cv2.imread(r'imageTransparent\translated58.png')
img_note59=cv2.imread(r'imageTransparent\translated59.png')
img_note60=cv2.imread(r'imageTransparent\translated60.png')
img_note61=cv2.imread(r'imageTransparent\translated61.png')
img_note62=cv2.imread(r'imageTransparent\translated62.png')
img_note63=cv2.imread(r'imageTransparent\translated63.png')
img_note64=cv2.imread(r'imageTransparent\translated64.png')
img_note65=cv2.imread(r'imageTransparent\translated65.png')
img_note66=cv2.imread(r'imageTransparent\translated66.png')
img_note67=cv2.imread(r'imageTransparent\translated67.png')
img_note68=cv2.imread(r'imageTransparent\translated68.png')
img_note69=cv2.imread(r'imageTransparent\translated69.png')
img_note70=cv2.imread(r'imageTransparent\translated70.png')
img_note71=cv2.imread(r'imageTransparent\translated71.png')
img_note72=cv2.imread(r'imageTransparent\translated72.png')
img_note73=cv2.imread(r'imageTransparent\translated73.png')
img_note74=cv2.imread(r'imageTransparent\translated74.png')
img_note75=cv2.imread(r'imageTransparent\translated75.png')
img_note76=cv2.imread(r'imageTransparent\translated76.png')
img_note77=cv2.imread(r'imageTransparent\translated77.png')
img_note78=cv2.imread(r'imageTransparent\translated78.png')
img_note79=cv2.imread(r'imageTransparent\translated79.png')
img_note80=cv2.imread(r'imageTransparent\translated80.png')
img_note81=cv2.imread(r'imageTransparent\translated81.png')
img_note82=cv2.imread(r'imageTransparent\translated82.png')
img_note83=cv2.imread(r'imageTransparent\translated83.png')
img_note84=cv2.imread(r'imageTransparent\translated84.png')
img_note85=cv2.imread(r'imageTransparent\translated85.png')
img_note86=cv2.imread(r'imageTransparent\translated86.png')
img_note87=cv2.imread(r'imageTransparent\translated87.png')
img_note88=cv2.imread(r'imageTransparent\translated88.png')
img_note89=cv2.imread(r'imageTransparent\translated89.png')
img_note90=cv2.imread(r'imageTransparent\translated90.png')
img_note91=cv2.imread(r'imageTransparent\translated91.png')
img_note92=cv2.imread(r'imageTransparent\translated92.png')
img_note93=cv2.imread(r'imageTransparent\translated93.png')
img_note94=cv2.imread(r'imageTransparent\translated94.png')
img_note95=cv2.imread(r'imageTransparent\translated95.png')
img_note96=cv2.imread(r'imageTransparent\translated96.png')
img_note97=cv2.imread(r'imageTransparent\translated97.png')
img_note98=cv2.imread(r'imageTransparent\translated98.png')
img_note99=cv2.imread(r'imageTransparent\translated99.png')
img_note100=cv2.imread(r'imageTransparent\translated100.png')
img_note101=cv2.imread(r'imageTransparent\translated101.png')
img_note102=cv2.imread(r'imageTransparent\translated102.png')
img_note103=cv2.imread(r'imageTransparent\translated103.png')
img_note104=cv2.imread(r'imageTransparent\translated104.png')
img_note105=cv2.imread(r'imageTransparent\translated105.png')
img_note106=cv2.imread(r'imageTransparent\translated106.png')'''

img0=img_with_note(img_txt0,img_note26)
cv2.imwrite('391.jpg',img0)
img1=img_with_note(img_txt1,img_note27)
cv2.imwrite('392.jpg',img1)
img2=img_with_note(img_txt2,img_note28)
cv2.imwrite('393.jpg',img2)
img3=img_with_note(img_txt3,img_note29)
cv2.imwrite('394.jpg',img3)
img4=img_with_note(img_txt4,img_note30)
cv2.imwrite('395.jpg',img4)
img5=img_with_note(img_txt5,img_note31)
cv2.imwrite('396.jpg',img5)
img6=img_with_note(img_txt6,img_note32)
cv2.imwrite('397.jpg',img6)
img7=img_with_note(img_txt7,img_note33)
cv2.imwrite('398.jpg',img7)
img8=img_with_note(img_txt8,img_note34)
cv2.imwrite('399.jpg',img8)
img9=img_with_note(img_txt9,img_note35)
cv2.imwrite('400.jpg',img9)
img10=img_with_note(img_txt10,img_note36)
cv2.imwrite('401.jpg',img10)
img11=img_with_note(img_txt11,img_note37)
cv2.imwrite('402.jpg',img11)
img12=img_with_note(img_txt12,img_note38)
cv2.imwrite('403.jpg',img12)
