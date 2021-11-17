import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import cv2
import numpy as np
import os

from copy import deepcopy

import torch
import torchvision.transforms as transforms

from models.tlgan.tlgan import Generator
from data.datasets import channel_first, channel_last

def make_axis(img):

    img = img.astype(np.uint8)
    contour2, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    axis_list = []
    for axis in contour2:
        if len(axis) > 10:
            axis = axis.squeeze()
            axis = axis.tolist()
            axis.sort()
            axis_list.append([axis[0], axis[-1]])

    return axis_list

def tlgan_infer(img, weight_path="./weights/generator.pt", img_col_size=60, img_row_size=256, left_margin=20):
    # img shape 256,256,3
    # image input for torch => channel first
    x = torch.tensor(channel_first(img))
    x = torch.unsqueeze(x, dim=0)

    netG = Generator()
    netG.load_state_dict(torch.load(weight_path, map_location="cpu"))

    x = netG(x)
    x = x.detach().numpy()[0]
    x = x > 0.2
    x = channel_last(x)
    
    # axis - 출력물 영역
    axis = sorted(make_axis(x), key=lambda x : x[0][1])

    result = []
    for (min, max) in axis:
        # croppging
        tmp = img[min[1]-2:max[1]+20, min[0]:max[0], :]

        # check the amount of padding
        up_magin = (img_col_size - (max[1]-min[1]))//2 - 2
        down_magin = img_col_size - (max[1] - min[1]) - up_magin - 2
        left_magin = left_margin
        right_margin = img_row_size-left_magin-(max[0]-min[0])

        # append pad img
        tmp = np.pad(tmp, ((up_magin, down_magin), (left_magin, right_margin), (0, 0)), 'constant', constant_values=0)
        result.append(tmp)

    return result, axis

## Inference code 완료
def remove_handwriting(img_path):    
    tlgan_model_path = "C:\\Users\\dongj\\Desktop\\git_test\\NoTimeToDie\\weights\\generator_15epoch.pt"
    path_to_img = img_path

    img = cv2.imread(path_to_img).astype(np.float32)
    img_int = cv2.imread(path_to_img)
    result, axes = tlgan_infer(img, weight_path=tlgan_model_path)

    croped_img_list = []
    croped_img_axis = []

    font_max_size = 15
    font_min_len = 20
    corrected_size = 10

    for ele in axes:
        # 1글자 길이보다 작은 경우 제외
        if ele[1][0] - ele[0][0] < font_min_len:
            pass

        else:
            # y축의 시작점만 가져오고 fontsize hardcoding

            # 예측 지점이 순서가 바뀌어 추론되는 경우가 있어서 해당 오류를 if 문으로 처리 한다.
            if ele[0][1] <= ele[1][1]:
                # cropped image ploting
                # show_with_matplotlib(img_int[ele[0][1]-corrected_size:ele[0][1]+font_max_size, ele[0][0]:ele[1][0]], 'title')

                # cropped image save in array
                croped_img_list.append(img_int[ele[0][1]-corrected_size:ele[0][1]+font_max_size, ele[0][0]:ele[1][0]])
                croped_img_axis.append(ele)

            # 예측 지점이 순서가 바뀌어 추론되는 경우가 있어서 해당 오류를 if 문으로 처리 한다.(아래가 바뀐경우라 2번째의 x좌표를 가져온다.)
            else:
                # cropped image ploting
                # show_with_matplotlib(img_int[ele[1][1]-corrected_size:ele[1][1]+font_max_size, ele[0][0]:ele[1][0]], 'title')

                # cropped image save in array
                croped_img_list.append(img_int[ele[1][1]-corrected_size:ele[1][1]+font_max_size, ele[0][0]:ele[1][0]])
                croped_img_axis.append(ele)
            
        print(ele[0][1],ele[1][1], ele[0][0],ele[1][0])

    # 흰색 이미지 생성
    img_output = np.full((256, 256, 3), 255, dtype=np.uint8)

    #cropped image 붙여넣기
    for i in range(len(croped_img_axis)):
        if croped_img_axis[i][0][1] <= croped_img_axis[i][1][1]:
            img_output[croped_img_axis[i][0][1]-corrected_size:croped_img_axis[i][0][1]+font_max_size, croped_img_axis[i][0][0]:croped_img_axis[i][1][0]] = croped_img_list[i]
        else:
            img_output[croped_img_axis[i][1][1]-corrected_size:croped_img_axis[i][1][1]+font_max_size, croped_img_axis[i][0][0]:croped_img_axis[i][1][0]] = croped_img_list[i]

    return img_output
