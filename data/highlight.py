import numpy as np
import random
import cv2

x=list()

#highlighting at most 3 highlights 
def img_with_highlighter(img_gau):
    ret, img_gau=cv2.threshold(img_gau,5,255,cv2.THRESH_BINARY)
    #append gaussian map start pixel in x
    for i in range(8):
        if [10+30*i,30] not in x and img_gau[10+30*i,30]==255:
            x.append([10+30*i,30])
            
    img_zeros=np.zeros((256,256,3),dtype=np.uint8)
    
    img_zeros=random_highlight_length(img_gau,img_zeros)
    if len(x)>1:
        img_zeros=random_highlight_length(img_gau,img_zeros)
    if len(x)>2:
        img_zeros=random_highlight_length(img_gau,img_zeros)

    return img_zeros

#find highlight length and eliminate overlap
def random_highlight_length(img_gau,img_zeros):
    #get a random pixel coordination
    x_rand,y_rand=random.choice(x)
    #get a random color
    rgb=get_complementary_bgr()
    #1 charactor pixel size
    q=17
    #fine gaussian map length
    while(img_gau[x_rand,y_rand+q]!=0):
        q+=1
    #randomly get 2 pixel coordinations
    q1=random.randint(0,q-17)
    q2=q1+17
    q2=random.randint(q2,q)

    img_zeros[x_rand-5:x_rand+15,y_rand+q1:y_rand+q2]=rgb
    x.remove([x_rand,y_rand])

    return img_zeros

#randomly color choice
def get_complementary_bgr():
    bgr=[[62,62,4],[115,49,2],[115,4,2],[115,2,42],[115,2,85],[51,100,2],[2,107,115],[2,62,115],[2,26,115],[55,2,115]]
    
    return random.choice(bgr)

def op_img_with_highlight(img,img_gau):
    #bitwise_not is for highlight image 
    img=cv2.bitwise_not(img)
    #create highlight image
    img_hl=img_with_highlighter(img_gau)
    #combine highlight image and text image
    added_img=cv2.addWeighted(img,0.9,img_hl,1.2,0)

    added_img = cv2.bitwise_not(added_img)

    return added_img

def execution():
    for a in range(1001):
        #gaussian image
        img_gau=cv2.imread(r'images\gaussian_jpg\%d.jpg' %(a),cv2.IMREAD_GRAYSCALE)
        #text image with note
        img=cv2.imread(r'images\synthesized\img%d.jpg' %(a))

        added_img=op_img_with_highlight(img,img_gau)

        #save result image
        cv2.imwrite(r"result\%d.jpg" %(a),added_img)

        #initialize list x_only for loop
        x=[]