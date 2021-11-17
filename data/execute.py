import numpy as np
import matplotlib.pyplot as pyplot
import cv2
import argparse
import os
import glob
import sys
import csv
import math
from PIL import ImageFont, ImageDraw, Image
from pathlib import Path

import split_txt
import generate_dataset
import generate_gau_map
import gaussian_npy2jpg
import noting
import highlight

def makedirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
#텍스트 폴더 생성-생성된 txt 폴더에 a.txt 직접 사용자가 넣기
makedirectory("images\gaussian_jpg")
makedirectory("images\synthesized")
makedirectory("result")

split()
generate()
generate_gau()
npy2jpg()
synthesize_note()
execution()
'''
images          txt       imageTransparent  result
gaussian_npy    a.txt
TLGAN           crawling.txt
gaussian_jpg
synthesized'''