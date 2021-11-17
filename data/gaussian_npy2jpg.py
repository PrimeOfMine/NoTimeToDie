import numpy as np
import matplotlib.pyplot as pyplot
import cv2

def npy2jpg():
    a=0
    while(a<1001):
        data=np.load(r'images\gaussian_npy\%d.npy' %(a))
        img=data[0]
        img=np.array(img,dtype=np.uint8)
        cv2.imwrite(r"images\gaussian_jpg\%d.jpg" %(a),img)
        a+=1