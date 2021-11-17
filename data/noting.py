#텍스트 이미지에 필기 한 자 합성
import numpy as np
import random
import cv2

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

def random_pixel(img,img_note,data):
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

def img_with_note(img_txt,data):
    img_note=cv2.imread(r"imageTransparent\translated%d.png" %(random.randrange(0, 107)))
    img_note=noteimg_crop(img_note)
    img=random_pixel(img_txt,img_note,data)
    
    num=random.randrange(1,6)
    for i in range(num):
        img_note=cv2.imread(r"imageTransparent\translated%d.png" %(random.randrange(0, 107)))
        img_note=noteimg_crop(img_note)
        img=random_pixel(img,img_note,data)
    
    return img

def synthesize_note():
    for num in range(1001):

        img_txt0 = cv2.imread(r'images\TLGAN\%d.jpg' %(num))
        data0 = np.load(r'images\gaussian_npy\%d.npy' %(num))

        img0=img_with_note(img_txt0,data0)

        cv2.imwrite(r"images\synthesized\img%d.jpg" %(num),img0)

    
#폴더 만들기
'''
TRANSPARENT//있어야 하는거
TLGAN IMG
GAUSSIAN_MAP_NPY
//generate_dataset.py 돌리면 나오는 거
GAUSSIAN_MAP IMG//npy2jpg.py 돌리면 나오는거>>폴더 필요
NOTING IMG>>폴더 필요
RESULT IMG>>폴더 필요
//새 파이썬 파일
'''
